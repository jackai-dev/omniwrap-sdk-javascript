"""Generated MCP Tasks (2026-07-28) state machine with fail-closed mutation reconciliation."""

from __future__ import annotations

from typing import Any, Dict, Mapping, Optional, Tuple

MCP_TASKS_SPEC_VERSION = "2026-07-28"
MCP_TASK_STATES: Tuple[str, ...] = (
    "working",
    "input_required",
    "completed",
    "failed",
    "cancelled",
    "reconciliation_required",
)
_READ_ONLY_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})
_IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})


class MCPTaskStateError(RuntimeError):
    """Raised on illegal MCP Tasks state transitions."""


class MCPTaskStateMachine:
    """MCP Tasks (2026-07-28) lifecycle and fail-closed mutation reconciliation guard."""

    SPEC_VERSION = MCP_TASKS_SPEC_VERSION
    VALID_STATES = MCP_TASK_STATES
    TERMINAL_STATES = frozenset(
        {"completed", "failed", "cancelled", "reconciliation_required"}
    )
    ALLOWED_TRANSITIONS: Dict[str, frozenset[str]] = {
        "working": frozenset(
            {
                "working",
                "input_required",
                "completed",
                "failed",
                "cancelled",
                "reconciliation_required",
            }
        ),
        "input_required": frozenset(
            {
                "working",
                "completed",
                "failed",
                "cancelled",
                "reconciliation_required",
            }
        ),
        "completed": frozenset(),
        "failed": frozenset(),
        "cancelled": frozenset(),
        "reconciliation_required": frozenset(),
    }

    def __init__(self, *, poll_interval_ms: int = 1000) -> None:
        if poll_interval_ms <= 0:
            raise ValueError("poll_interval_ms must be positive")
        self.poll_interval_ms = int(poll_interval_ms)
        self._tasks: Dict[str, Dict[str, Any]] = {}
        self._cancelled_tokens: set[str] = set()

    def create_task(
        self,
        task_id: str,
        operation_id: str,
        *,
        method: str = "GET",
        read_only: Optional[bool] = None,
        idempotent: Optional[bool] = None,
        cancellation_token: Optional[str] = None,
        poll_interval_ms: Optional[int] = None,
    ) -> Dict[str, Any]:
        upper_method = method.upper()
        is_read_only = (
            upper_method in _READ_ONLY_METHODS if read_only is None else bool(read_only)
        )
        is_idempotent = (
            upper_method in _IDEMPOTENT_METHODS
            if idempotent is None
            else bool(idempotent)
        )
        token = cancellation_token or f"cancel-{task_id}"
        record: Dict[str, Any] = {
            "taskId": task_id,
            "operationId": operation_id,
            "method": upper_method,
            "readOnly": is_read_only,
            "idempotent": is_idempotent,
            "state": "working",
            "pollIntervalMs": int(poll_interval_ms or self.poll_interval_ms),
            "cancellationToken": token,
            "requestDispatched": False,
            "responseConfirmed": False,
            "reconciliationRequired": False,
            "history": [{"from": None, "to": "working", "reason": "created"}],
            "result": None,
            "error": None,
        }
        self._tasks[task_id] = record
        return dict(record)

    def get_task(self, task_id: str) -> Dict[str, Any]:
        if task_id not in self._tasks:
            raise MCPTaskStateError(f"Unknown task_id: {task_id}")
        return dict(self._tasks[task_id])

    def mark_request_dispatched(self, task_id: str) -> Dict[str, Any]:
        task = self._require_mutable_task(task_id)
        task["requestDispatched"] = True
        return dict(task)

    def request_input(self, task_id: str, prompt: str = "Additional input required") -> Dict[str, Any]:
        return self._transition(task_id, "input_required", reason=prompt)

    def provide_input(self, task_id: str, input_data: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
        task = self._require_mutable_task(task_id)
        if task["state"] != "input_required":
            raise MCPTaskStateError(
                f"Task {task_id} is in state '{task['state']}', expected 'input_required'"
            )
        task["lastInput"] = dict(input_data or {})
        return self._transition(task_id, "working", reason="input_provided")

    def complete(self, task_id: str, result: Any = None) -> Dict[str, Any]:
        task = self._require_mutable_task(task_id)
        task["responseConfirmed"] = True
        task["result"] = result
        return self._transition(task_id, "completed", reason="confirmed_response")

    def fail(self, task_id: str, error: str, *, response_confirmed: bool = True) -> Dict[str, Any]:
        task = self._require_mutable_task(task_id)
        task["error"] = error
        task["responseConfirmed"] = bool(response_confirmed)
        if (
            not response_confirmed
            and not task["readOnly"]
            and not task["idempotent"]
        ):
            task["reconciliationRequired"] = True
            return self._transition(
                task_id,
                "reconciliation_required",
                reason=f"unconfirmed_non_idempotent_write:{error}",
            )
        return self._transition(task_id, "failed", reason=error)

    def cancel(
        self,
        task_id: str,
        *,
        cancellation_token: Optional[str] = None,
        reason: str = "cancelled_by_caller",
    ) -> Dict[str, Any]:
        task = self._require_mutable_task(task_id)
        if (
            cancellation_token is not None
            and cancellation_token != task["cancellationToken"]
        ):
            raise MCPTaskStateError("Invalid cancellation token")
        self._cancelled_tokens.add(task["cancellationToken"])
        if (
            task["requestDispatched"]
            and not task["responseConfirmed"]
            and not task["readOnly"]
            and not task["idempotent"]
        ):
            task["reconciliationRequired"] = True
            return self._transition(
                task_id,
                "reconciliation_required",
                reason="cancelled_in_flight_non_idempotent_write",
            )
        return self._transition(task_id, "cancelled", reason=reason)

    def interrupt_before_confirmation(
        self,
        task_id: str,
        *,
        reason: str = "transport_interrupted_before_response_confirmation",
    ) -> Dict[str, Any]:
        task = self._require_mutable_task(task_id)
        task["requestDispatched"] = True
        task["responseConfirmed"] = False
        task["error"] = reason
        if not task["readOnly"] and not task["idempotent"]:
            task["reconciliationRequired"] = True
            return self._transition(
                task_id,
                "reconciliation_required",
                reason=reason,
            )
        return self._transition(task_id, "cancelled", reason=reason)

    def _require_mutable_task(self, task_id: str) -> Dict[str, Any]:
        if task_id not in self._tasks:
            raise MCPTaskStateError(f"Unknown task_id: {task_id}")
        task = self._tasks[task_id]
        if task["state"] in self.TERMINAL_STATES:
            raise MCPTaskStateError(
                f"Task {task_id} is already in terminal state '{task['state']}'"
            )
        return task

    def _transition(self, task_id: str, target_state: str, *, reason: str) -> Dict[str, Any]:
        task = self._require_mutable_task(task_id)
        current = task["state"]
        allowed = self.ALLOWED_TRANSITIONS.get(current, frozenset())
        if target_state not in allowed:
            raise MCPTaskStateError(
                f"Illegal transition for task {task_id}: {current} -> {target_state}"
            )
        task["state"] = target_state
        task["history"].append({"from": current, "to": target_state, "reason": reason})
        return dict(task)
