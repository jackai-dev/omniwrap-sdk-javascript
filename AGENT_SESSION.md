# Bounded SDK agent sessions

This opt-in module runs in the process consuming this exact SDK. Any caller-chosen
provider can implement `omniwrap.agent-provider/v1`; no model vendor, harness, MCP
transport or hosted service is required. `agent-session.json` maps exact operation
IDs to SDK methods, argument schemas, effect signatures and `api.md` references.
Operation intent is contract-derived data, never provider instructions or permission grants.
TypeScript and JavaScript packages export typed `ToolCall` proposals from `./agent-session`; Python exports
operation-specific `Arguments_*` and `Call_*` TypedDicts from `agent_session`.

Supply an already configured SDK client, provider identity and version, the SHA-256
of the exact installed npm archive or wheel, all nine positive limits, a checkpoint,
an explicit write-approval callback and an approved result-persistence projection.
The operation allowlist is caller-granted, persisted in the binding and immutable during a session. The client fixes authentication and destination; proposals cannot set client options,
credentials, headers, retries or wider access. Contract arguments still use the SDK's
normal serialization and validation. Each SDK invocation disables automatic retries.
Writes require caller approval of the operation ID and argument hash before execution.
Unsafe HTTP methods and explicit source-effect writes both require approval, including a GET operation declared to write.

Provider `propose(context, remaining[, signal])` returns exactly either
`{usage: {tokens, cost}, calls: [{id, tool, arguments}]}` or
`{usage: {tokens, cost}, final: value}`. Python uses `async propose` and `async aclose`;
TypeScript and JavaScript use `async propose` and `async close`. Provider context includes the
version, original input, exact registry and prior receipts in proposal order.
Only validated structured results from the persistence projection are reinjected.
Every call ID must be unique for the session. A full batch validates before effects;
its size cannot exceed concurrency. A size of one gives sequential execution.

Mandatory limits: `turns`, `model_calls`, `tool_calls`, `tokens`, `cost`,
`elapsed_seconds`, `concurrency`, `input_bytes`, `output_bytes`. Count limits are
integers. Tokens and cost are adapter-attested: the module cannot inspect or sandbox
arbitrary provider code. Providers must honor remaining budgets and cancellation,
close their own resources, and avoid starting unbounded external work. Input byte
accounting includes serialized provider contexts and proposals; output accounting
includes projected receipts/finals. SDK response buffers are bounded per request.
Parallel transport buffers can reach concurrency times the remaining response bound.
Python cancellation uses task cancellation; TypeScript and JavaScript accept an AbortSignal.
Callback cleanup is cooperative and cleanup timeout errors must be surfaced.

`AtomicCheckpoint(path, key)` requires an external secret key of at least 32 bytes.
Keep it outside the checkpoint and model context. Files use HMAC-SHA256 authentication,
atomic replacement, an exclusive write lock and compare-and-swap revision checking.
Checkpoint bindings include protocol, semantic source, exact archive, registry,
provider and all limits. Receipts form a SHA-256 hash chain. Checkpoints contain no
provider reasoning, authentication configuration, original input or tool arguments;
arguments are represented only by hashes. API results may contain secrets: the caller
must supply and test a projection that removes them before persistence/reinjection.
This callback is a trusted policy boundary, not automatic secret detection.

Resume reconstructs the session with identical bindings/key. A completed final result
returns without another call. Any persisted in-flight call is `InDoubt`, including a
mutation whose server effect occurred before its response/checkpoint acknowledgement.
The runtime never blindly retries it. Inspect the external system and explicitly call
`reconcile(callId, knownResult)`; the approved projection and new receipt are persisted.
An acknowledged call ID cannot be reused. Corruption, config/provider/registry/archive
drift or concurrent checkpoint writes fail closed. An abandoned `.lock` requires
operator verification that the writer has stopped before manual recovery; it is never
silently deleted. A durable deadline prevents resume from resetting elapsed budgets.

SDK failures retain their native structured errors for caller diagnosis; error messages
are retained as causes of a non-retryable `agent_session_in_doubt` failure when a mutation outcome is unresolved. Session refusals have code `agent_session_refused` and `retryable=false`. Error messages
and exceptions are not copied into checkpoints. A failed batch can leave completed
external effects in doubt. Reconcile them before continuing, and inspect native SDK
remediation metadata rather than automatically retrying a model proposal.

```python
from pathlib import Path
from your_sdk import AsyncClient
from your_sdk.agent_session import AgentSession, AtomicCheckpoint

# Provider implements version='omniwrap.agent-provider/v1', identity, propose/aclose.
# archive_sha256 and checkpoint_key come from the caller's verified installation.
session = AgentSession(AsyncClient(base_url=approved_url), provider,
    artifact_hash=archive_sha256, allowed_tools=approved_operation_ids, limits=limits,
    checkpoint=AtomicCheckpoint(Path('session.json'), checkpoint_key),
    persist_result=approved_projection, approve_write=approve_operation_hash)
result = await session.run({'goal': 'Read an approved resource'})
```

```typescript
import { AgentSession, AtomicCheckpoint } from 'your-sdk/agent-session';
const session = new AgentSession(client, provider, {
  artifactHash: archiveSha256, allowedTools: approvedOperationIds, limits,
  checkpoint: new AtomicCheckpoint('session.json', checkpointKey),
  persistResult: approvedProjection, approveWrite: approveOperationHash,
});
const result = await session.run({goal: 'Read an approved resource'}, signal);
```

Regex-constrained arguments are refused before SDK execution because arbitrary regex evaluation is not safely preemptible. Use separately qualified caller-controlled SDK execution; ordinary SDK generation/calls remain available.

These examples require caller implementations and explicit policies; they do not claim
a live hosted-model run. See the source repository's installed-consumer regressions
and shared behavioral vectors for actual loopback and recovery qualification.

Session inputs are plain finite JSON and integers must fit the JavaScript safe-integer range. Model-supplied header/cookie arguments, stream/upload operations, unqualified formats and unsupported schema constraints are refused before effects. These are explicit session-core gaps; the underlying SDK keeps its broader native API. Reported provider usage, including an overrun, is recorded separately from admitted budget usage.
