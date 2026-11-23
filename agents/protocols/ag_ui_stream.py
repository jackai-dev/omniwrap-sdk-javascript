"""Generated AG-UI protocol event emitter with deterministic sequencing and secret redaction."""

from __future__ import annotations

import json
import re
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

AG_UI_PROTOCOL_VERSION = "ag-ui/1.0"
AG_UI_EVENT_TYPES: Tuple[str, ...] = (
    "RUN_STARTED",
    "TOOL_CALL_START",
    "TOOL_CALL_ARGS",
    "TOOL_CALL_END",
    "STATE_DELTA",
    "TEXT_MESSAGE_CONTENT",
    "RUN_FINISHED",
    "RUN_ERROR",
)

_SECRET_KEY_PATTERN = re.compile(
    r"(authorization|proxy-authorization|x-api-key|api[-_]?key|access[-_]?token|"
    r"refresh[-_]?token|id[-_]?token|client[-_]?secret|secret|password|cookie|"
    r"set-cookie|bearer|private[-_]?key|session[-_]?token|token)",
    re.IGNORECASE,
)
_INLINE_BEARER_PATTERN = re.compile(
    r"\b(Bearer|Basic|Token)\s+[A-Za-z0-9._~+/=-]{4,}",
    re.IGNORECASE,
)


def redact_secrets(value: Any) -> Any:
    """Recursively redact secret headers and tokens as '[redacted]'."""
    if isinstance(value, Mapping):
        redacted: Dict[str, Any] = {}
        for k, v in value.items():
            key_str = str(k)
            if _SECRET_KEY_PATTERN.search(key_str):
                redacted[key_str] = "[redacted]"
            else:
                redacted[key_str] = redact_secrets(v)
        return redacted
    if isinstance(value, (list, tuple)):
        return [redact_secrets(item) for item in value]
    if isinstance(value, str) and _INLINE_BEARER_PATTERN.search(value):
        return "[redacted]"
    return value


class AGUIEventStream:
    """Deterministic AG-UI event emitter."""

    EVENT_TYPES = AG_UI_EVENT_TYPES

    def __init__(self, *, run_id: str = "run-1", thread_id: str = "thread-1") -> None:
        self.run_id = run_id
        self.thread_id = thread_id
        self._seq = 0
        self._events: List[Dict[str, Any]] = []

    @property
    def events(self) -> List[Dict[str, Any]]:
        return list(self._events)

    def emit(self, event_type: str, payload: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
        if event_type not in AG_UI_EVENT_TYPES:
            raise ValueError(f"Unsupported AG-UI event type: {event_type}")
        self._seq += 1
        event: Dict[str, Any] = {
            "protocol": AG_UI_PROTOCOL_VERSION,
            "seq": self._seq,
            "type": event_type,
            "runId": self.run_id,
            "threadId": self.thread_id,
            "payload": redact_secrets(dict(payload or {})),
        }
        self._events.append(event)
        return event

    def run_started(self, metadata: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
        return self.emit("RUN_STARTED", {"metadata": dict(metadata or {})})

    def tool_call_start(
        self,
        tool_call_id: str,
        tool_name: str,
        *,
        headers: Optional[Mapping[str, Any]] = None,
    ) -> Dict[str, Any]:
        data: Dict[str, Any] = {"toolCallId": tool_call_id, "toolName": tool_name}
        if headers is not None:
            data["headers"] = dict(headers)
        return self.emit("TOOL_CALL_START", data)

    def tool_call_args(self, tool_call_id: str, args: Mapping[str, Any]) -> Dict[str, Any]:
        return self.emit("TOOL_CALL_ARGS", {"toolCallId": tool_call_id, "args": dict(args)})

    def tool_call_end(
        self,
        tool_call_id: str,
        result: Any = None,
        *,
        headers: Optional[Mapping[str, Any]] = None,
    ) -> Dict[str, Any]:
        data: Dict[str, Any] = {"toolCallId": tool_call_id, "result": result}
        if headers is not None:
            data["headers"] = dict(headers)
        return self.emit("TOOL_CALL_END", data)

    def state_delta(self, delta: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
        return self.emit("STATE_DELTA", {"delta": list(delta)})

    def text_message_content(
        self,
        message_id: str,
        delta: str,
        *,
        role: str = "assistant",
    ) -> Dict[str, Any]:
        return self.emit(
            "TEXT_MESSAGE_CONTENT",
            {"messageId": message_id, "role": role, "delta": delta},
        )

    def run_finished(self, summary: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
        return self.emit("RUN_FINISHED", {"summary": dict(summary or {})})

    def run_error(
        self,
        message: str,
        *,
        code: str = "EXECUTION_ERROR",
        details: Optional[Mapping[str, Any]] = None,
    ) -> Dict[str, Any]:
        data: Dict[str, Any] = {"code": code, "message": message}
        if details is not None:
            data["details"] = dict(details)
        return self.emit("RUN_ERROR", data)

    def to_ndjson(self) -> str:
        return "\n".join(
            json.dumps(ev, ensure_ascii=False, sort_keys=True) for ev in self._events
        )
