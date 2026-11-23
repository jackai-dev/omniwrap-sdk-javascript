# OmniWrap JavaScript API

<!-- omniwrap-api-reference eyJjb250cmFjdF9maW5nZXJwcmludCI6IjIyODliY2IwZDY2MWJkZWE2ZGQ0N2M3OTY3ZjM3YWFjZTdkM2ExNTJlMThlN2QyZjY0YzA4NTE0ZmI3M2U3OTUiLCJvcGVyYXRpb25fY291bnQiOjE2LCJyZW5kZXJlciI6ImphdmFzY3JpcHQiLCJ2ZXJzaW9uIjoiMS41LjAifQ -->

This generated index is tied to Semantic IR `1.14.0` and contract fingerprint `2289bcb0d661bdea6dd47c7967f37aace7d3a152e18e7d2f64c08514fb73e795`. Every operation below is rendered from the same semantic contract and artifact-attested public member allocation as the SDK.

SDK maturity: **verified**  
Artifact evidence: [`omniwrap-artifact.json`](omniwrap-artifact.json) binds this file by SHA-256 and is revalidated by the package gate.

## Client hooks and tracing

`new Client({ hooks })` registers four callbacks. Every attempt starts with `beforeRequest` and ends with exactly one of `onRetry` (another attempt follows), `afterResponse` (the success the call returns) or `onError` (the failure the call reports). Each receives the operation id, the HTTP method, the URL, the request headers, the attempt number (from 1), the time elapsed since the call started and, once the server answered, the HTTP status. No context carries a credential: `Authorization`, `Proxy-Authorization`, `Cookie`, every API-key header and API-key query parameter, and any configured credential value read `[redacted]`. `beforeRequest` is the one hook that may change the request (the documented per-request credential contract, which also reads credentials masked); the other three receive frozen `HookContext` copies.

`new Client({ tracer })` opens one span per call through the tracer interface this SDK defines, named after the operation id, with `http.request.method`, `http.response.status_code` and `http.request.resend_count`. It needs no tracing library; README.md maps it onto the OpenTelemetry API.

## Shared types

- `ApiError`
- `Artifact`
- `CancelRequest`
- `CancellationReceipt`
- `ConfigurationRequest`
- `ConfigurationRevision`
- `Cursor`
- `Diagnostic`
- `ErrorDetail`
- `EventPage`
- `Evidence`
- `EvidenceBinding`
- `EvidencePage`
- `ExecutionBinding`
- `GateReport`
- `GateStatus`
- `LogEntry`
- `LogPage`
- `ObservedPhase`
- `OpaqueId`
- `Preview`
- `PreviewEvent`
- `PreviewInputs`
- `PreviewPage`
- `PreviewRequest`
- `PreviewState`
- `PrimaryArtifacts`
- `ProfileId`
- `Project`
- `ProjectPage`
- `Sha256`
- `SourceRevision`
- `StrongEtag`
- `Timestamp`
- `UserContext`

## Resource `artifacts`

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJhcnRpZmFjdHMuZ2V0IiwibWV0aG9kIjoiR0VUIiwib3BlcmF0aW9uX2lkIjoiZ2V0QXJ0aWZhY3QiLCJwYXRoIjoiL3YxL3Byb2plY3RzL3twcm9qZWN0SWR9L2FydGlmYWN0cy97YXJ0aWZhY3RJZH0iLCJyZXNvdXJjZSI6ImFydGlmYWN0cyIsInNlY3Rpb25fc2hhMjU2IjoiZWIxMmQ1MjFjYTc2ZWU5MWJkODYyNWVlZDhkOWIzZGQxZWEyYjY5YzVmN2M0MGZiZTNiMDNjZTVhZTkyZGI0MiIsInNpZ25hdHVyZV9zaGEyNTYiOiI3Yzg5OTNiYWM3YjVjMzRmYzU5NjM3ZTM4ZjhiYmRhZDM5MzQzYzFlZDFlZWM1YjZjZDlmYzZiZjM1ZWY5YjRlIn0 -->
### `client.artifacts.get`

Operation ID: `getArtifact`  
Route: `GET` `/v1/projects/{projectId}/artifacts/{artifactId}`  
Equivalent member: `client.getArtifact`  

#### Signature

```javascript
client.artifacts.get(projectId, artifactId, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `artifactId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `200` | Authorized resource snapshot. | application/json (Artifact) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    },
    {
      "in": "path",
      "name": "artifactId",
      "value": "example"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.artifacts.get("example", "example");
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJnZXRBcnRpZmFjdCJ9 -->

## Resource `configurations`

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJjb25maWd1cmF0aW9ucy5jcmVhdGVSZXZpc2lvbiIsIm1ldGhvZCI6IlBPU1QiLCJvcGVyYXRpb25faWQiOiJjcmVhdGVDb25maWd1cmF0aW9uUmV2aXNpb24iLCJwYXRoIjoiL3YxL3Byb2plY3RzL3twcm9qZWN0SWR9L2NvbmZpZ3VyYXRpb24tcmV2aXNpb25zIiwicmVzb3VyY2UiOiJjb25maWd1cmF0aW9ucyIsInNlY3Rpb25fc2hhMjU2IjoiMDQ4NTA1NDFmY2E4OGRiYmIzYWQ2NGJiNjY4ZThmMTA1YmZiNGYwOWE0MTBhOGNkZGZjMTllZGJmNzY2ZmQ1YSIsInNpZ25hdHVyZV9zaGEyNTYiOiI1MDczMzA4MjU1ZTJhMjE4ZDZjYmJlMGQxZjkzMjhhOGQyZWRmMWUxYjdkMWJjYTQxMWExOGY2MThiZjliMTI5In0 -->
### `client.configurations.createRevision`

Operation ID: `createConfigurationRevision`  
Route: `POST` `/v1/projects/{projectId}/configuration-revisions`  
Equivalent member: `client.createConfigurationRevision`  

#### Signature

```javascript
client.configurations.createRevision(projectId, If_Match, Idempotency_Key, X_CSRF_Token, body, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `If-Match` | `header` | yes | `StrongEtag` | Exactly one strong ETag. Configuration activation and preview creation compare the current Project ETag, including first activation. Cancellation compares the Preview ETag. Stale = 412; absent = 428. Wildcard, weak tags and lists are rejected. |
| `Idempotency-Key` | `header` | yes | `string` | Required on every mutation. Scope = organization + project + operation; fingerprint includes raw body bytes, media type, resource and If-Match. Same key/content replays the same receipt; changed content is 409. Retained for 86400 seconds; reconcile an ambiguous outcome within retention before retry, never silently allocate a new key. |
| `X-CSRF-Token` | `header` | yes | `string` | Session-bound synchronizer token from the trusted BFF bootstrap, independent of the unreadable session cookie. Validate same-origin Origin and CSRF before mutation. This contract does not implement or provision the session/CSRF exchange. |
| `body` | body | yes | `ConfigurationRequest` |  |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `201` | Created and atomically activated after admitted engine resolution; response ETag identifies the immutable configuration. Reload Project to obtain the new Project ETag. | application/json (ConfigurationRevision) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `409` | idempotency_conflict/reconcile_idempotency, binding_conflict/refresh_snapshot, or retry_requires_reconciliation/refresh_snapshot. No additional effect. | application/json (allOf&lt;ApiError, object&gt;) |
| `412` | precondition_failed; recovery=refresh_snapshot. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `413` | request_too_large; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `415` | unsupported_media_type; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `428` | precondition_required; recovery=refresh_snapshot. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "body": {
    "profileId": "openapi-typescript-preview/1",
    "sourceRevisionId": "example"
  },
  "content_type": "application/json",
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    },
    {
      "in": "header",
      "name": "If-Match",
      "value": "\"A\""
    },
    {
      "in": "header",
      "name": "Idempotency-Key",
      "value": "AAAAAAAAAAAAAAAA"
    },
    {
      "in": "header",
      "name": "X-CSRF-Token",
      "value": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.configurations.createRevision("example", "\"A\"", "AAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", {"profileId": "openapi-typescript-preview/1", "sourceRevisionId": "example"}, { contentType: "application/json" });
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJjcmVhdGVDb25maWd1cmF0aW9uUmV2aXNpb24ifQ -->

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJjb25maWd1cmF0aW9ucy5nZXRSZXZpc2lvbiIsIm1ldGhvZCI6IkdFVCIsIm9wZXJhdGlvbl9pZCI6ImdldENvbmZpZ3VyYXRpb25SZXZpc2lvbiIsInBhdGgiOiIvdjEvcHJvamVjdHMve3Byb2plY3RJZH0vY29uZmlndXJhdGlvbi1yZXZpc2lvbnMve3JldmlzaW9uSWR9IiwicmVzb3VyY2UiOiJjb25maWd1cmF0aW9ucyIsInNlY3Rpb25fc2hhMjU2IjoiYjU4MGQ5NjkzYWJmMmZjYzQ5NjQyMDU4NGRiMmFjYmE4ZTE2ODdjOTAyMTdlYzliZjAzNTNiMmE1MDBiN2IzMCIsInNpZ25hdHVyZV9zaGEyNTYiOiIyZWNhZjkzZDgxNmE5Njg3ZjNmM2JkNDQxOGY4MzA3YzJkNTQ0OWUxZTk3ZDdiYjc4MWQ4MzM4NWQxNjIzYWE2In0 -->
### `client.configurations.getRevision`

Operation ID: `getConfigurationRevision`  
Route: `GET` `/v1/projects/{projectId}/configuration-revisions/{revisionId}`  
Equivalent member: `client.getConfigurationRevision`  

#### Signature

```javascript
client.configurations.getRevision(projectId, revisionId, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `revisionId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `200` | Authorized resource snapshot. | application/json (ConfigurationRevision) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    },
    {
      "in": "path",
      "name": "revisionId",
      "value": "example"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.configurations.getRevision("example", "example");
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJnZXRDb25maWd1cmF0aW9uUmV2aXNpb24ifQ -->

## Resource `context`

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJjb250ZXh0LmdldFVzZXIiLCJtZXRob2QiOiJHRVQiLCJvcGVyYXRpb25faWQiOiJnZXRVc2VyQ29udGV4dCIsInBhdGgiOiIvdjEvbWUvY29udGV4dCIsInJlc291cmNlIjoiY29udGV4dCIsInNlY3Rpb25fc2hhMjU2IjoiYjI5OTFlYmIxZTQ4YzQ4NDBlNzAzZGU5NjNiOGY2OGJmN2QzMDRhOWYwMjZjZTZmNmEyYjEyNzgyNjM5OGJkYyIsInNpZ25hdHVyZV9zaGEyNTYiOiJkNjBkNDdkNWMxMzc4NDZiMmJmNTdjZWYwMDg5YWJiYzA5YjE5MmY5MzE1MWJjYWZkYjgyODZiYjc5YjIyMmI4In0 -->
### `client.context.getUser`

Operation ID: `getUserContext`  
Route: `GET` `/v1/me/context`  
Equivalent member: `client.getUserContext`  

#### Signature

```javascript
client.context.getUser(requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| _none_ | | | | |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `200` | Authorized resource snapshot. | application/json (UserContext) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "parameters": []
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.context.getUser();
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJnZXRVc2VyQ29udGV4dCJ9 -->

## Resource `evidence`

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJldmlkZW5jZS5nZXQiLCJtZXRob2QiOiJHRVQiLCJvcGVyYXRpb25faWQiOiJnZXRFdmlkZW5jZSIsInBhdGgiOiIvdjEvcHJvamVjdHMve3Byb2plY3RJZH0vZXZpZGVuY2Uve2V2aWRlbmNlSWR9IiwicmVzb3VyY2UiOiJldmlkZW5jZSIsInNlY3Rpb25fc2hhMjU2IjoiNDFmOWNiNGM5ODdmNzJjMzg5NDJjMDA4MmNmNDQ2NjBlZGMyMDA2ZjZmZDQ2MmUxNjgzOGRlMTEyOTE4NDg5MCIsInNpZ25hdHVyZV9zaGEyNTYiOiJhZGRhOTlhOTA2ZjcyZWFmZTUzMDcxNjNlZTNlNmQ3ZjA0MmJhYmQ2YzM4MTVkOGM2MjgwMDU0ZTdlMDFlMTY3In0 -->
### `client.evidence.get`

Operation ID: `getEvidence`  
Route: `GET` `/v1/projects/{projectId}/evidence/{evidenceId}`  
Equivalent member: `client.getEvidence`  

#### Signature

```javascript
client.evidence.get(projectId, evidenceId, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `evidenceId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `200` | Authorized resource snapshot. | application/json (Evidence) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    },
    {
      "in": "path",
      "name": "evidenceId",
      "value": "example"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.evidence.get("example", "example");
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJnZXRFdmlkZW5jZSJ9 -->

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJldmlkZW5jZS5saXN0UHJldmlldyIsIm1ldGhvZCI6IkdFVCIsIm9wZXJhdGlvbl9pZCI6Imxpc3RQcmV2aWV3RXZpZGVuY2UiLCJwYXRoIjoiL3YxL3Byb2plY3RzL3twcm9qZWN0SWR9L3ByZXZpZXdzL3twcmV2aWV3SWR9L2V2aWRlbmNlIiwicmVzb3VyY2UiOiJldmlkZW5jZSIsInNlY3Rpb25fc2hhMjU2IjoiZjY1M2EzZWNkNDg3NGMxM2ZlZTRlMzE0MzU1MGQ4NWI5YWNjOGEyYjU5ZTIzOTczZDBlYWI0MWY0ZmQwNjg1ZCIsInNpZ25hdHVyZV9zaGEyNTYiOiI2YzhjODgzMjE0MTU1NzJmMmZjMjUyMzdhYjI2OWZjNTBiODA5ZmI4ZjhhMzQyNzNmZTNjMmZjMGRkNTRkYmE1In0 -->
### `client.evidence.listPreview`

Operation ID: `listPreviewEvidence`  
Route: `GET` `/v1/projects/{projectId}/previews/{previewId}/evidence`  
Equivalent member: `client.listPreviewEvidence`  

#### Signature

```javascript
client.evidence.listPreview(projectId, previewId, cursor?, limit?, gateId?, availability?, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `previewId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `cursor` | `query` | no | `Cursor` | Opaque scope-bound continuation, never an offset or authority token. Expired/gap = 410 refresh_snapshot; invalid/tampered/wrong filters = 422. Denied objects remain uniform404. |
| `limit` | `query` | no | `integer` | Maximum page size; default 50. |
| `gateId` | `query` | no | `string` |  |
| `availability` | `query` | no | `string` |  |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `200` | Authorized resource snapshot. | application/json (EvidencePage) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `410` | cursor_expired; recovery=refresh_snapshot. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    },
    {
      "in": "path",
      "name": "previewId",
      "value": "example"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.evidence.listPreview("example", "example");
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJsaXN0UHJldmlld0V2aWRlbmNlIn0 -->

## Resource `previews`

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJwcmV2aWV3cy5jYW5jZWwiLCJtZXRob2QiOiJQT1NUIiwib3BlcmF0aW9uX2lkIjoiY2FuY2VsUHJldmlldyIsInBhdGgiOiIvdjEvcHJvamVjdHMve3Byb2plY3RJZH0vcHJldmlld3Mve3ByZXZpZXdJZH0vY2FuY2VsIiwicmVzb3VyY2UiOiJwcmV2aWV3cyIsInNlY3Rpb25fc2hhMjU2IjoiZWRkYzZmODhhNjE4ZjAzOGRmODhlNzA0YmMwODUzZjIyMTU5MDVjMmMyMWFhZTYwMzM2N2MyZGRmZTVkMmJiMSIsInNpZ25hdHVyZV9zaGEyNTYiOiI5MDc3ZmU0MTZhNDAwMGQxODY5YTkyYTNmZmVkM2FmMDYxOGNiNDkwZWZkOGZmYzExZTU2N2Y0MGM2OGM5YmM5In0 -->
### `client.previews.cancel`

Operation ID: `cancelPreview`  
Route: `POST` `/v1/projects/{projectId}/previews/{previewId}/cancel`  
Equivalent member: `client.cancelPreview`  

#### Signature

```javascript
client.previews.cancel(projectId, previewId, If_Match, Idempotency_Key, X_CSRF_Token, body, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `previewId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `If-Match` | `header` | yes | `StrongEtag` | Exactly one strong ETag. Configuration activation and preview creation compare the current Project ETag, including first activation. Cancellation compares the Preview ETag. Stale = 412; absent = 428. Wildcard, weak tags and lists are rejected. |
| `Idempotency-Key` | `header` | yes | `string` | Required on every mutation. Scope = organization + project + operation; fingerprint includes raw body bytes, media type, resource and If-Match. Same key/content replays the same receipt; changed content is 409. Retained for 86400 seconds; reconcile an ambiguous outcome within retention before retry, never silently allocate a new key. |
| `X-CSRF-Token` | `header` | yes | `string` | Session-bound synchronizer token from the trusted BFF bootstrap, independent of the unreadable session cookie. Validate same-origin Origin and CSRF before mutation. This contract does not implement or provision the session/CSRF exchange. |
| `body` | body | yes | `CancelRequest` |  |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `202` | Accepted for asynchronous processing; not a completed effect. | application/json (CancellationReceipt) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `409` | idempotency_conflict/reconcile_idempotency, binding_conflict/refresh_snapshot, or retry_requires_reconciliation/refresh_snapshot. No additional effect. | application/json (allOf&lt;ApiError, object&gt;) |
| `412` | precondition_failed; recovery=refresh_snapshot. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `413` | request_too_large; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `415` | unsupported_media_type; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `428` | precondition_required; recovery=refresh_snapshot. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "body": {
    "reason": "user_requested"
  },
  "content_type": "application/json",
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    },
    {
      "in": "path",
      "name": "previewId",
      "value": "example"
    },
    {
      "in": "header",
      "name": "If-Match",
      "value": "\"A\""
    },
    {
      "in": "header",
      "name": "Idempotency-Key",
      "value": "AAAAAAAAAAAAAAAA"
    },
    {
      "in": "header",
      "name": "X-CSRF-Token",
      "value": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.previews.cancel("example", "example", "\"A\"", "AAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", {"reason": "user_requested"}, { contentType: "application/json" });
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJjYW5jZWxQcmV2aWV3In0 -->

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJwcmV2aWV3cy5jcmVhdGUiLCJtZXRob2QiOiJQT1NUIiwib3BlcmF0aW9uX2lkIjoiY3JlYXRlUHJldmlldyIsInBhdGgiOiIvdjEvcHJvamVjdHMve3Byb2plY3RJZH0vcHJldmlld3MiLCJyZXNvdXJjZSI6InByZXZpZXdzIiwic2VjdGlvbl9zaGEyNTYiOiI3YmQwZjEzYjBkMGY0Mjc2OWUyZTdhOWE2ZGRmMWIwZmY3Y2FiMmQyYTQzYWM4ZGNjMzk2OWEzZGZhYTg4ZDAwIiwic2lnbmF0dXJlX3NoYTI1NiI6IjAwNTkzMzUzNjExZDEyYjU5MTczNTc1YjY2Njg3Y2I4ODFkM2I5ODI1NTEzMzE3MjcyNDU0YWYzMjM2ZWU0NDAifQ -->
### `client.previews.create`

Operation ID: `createPreview`  
Route: `POST` `/v1/projects/{projectId}/previews`  
Equivalent member: `client.createPreview`  

#### Signature

```javascript
client.previews.create(projectId, If_Match, Idempotency_Key, X_CSRF_Token, body, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `If-Match` | `header` | yes | `StrongEtag` | Exactly one strong ETag. Configuration activation and preview creation compare the current Project ETag, including first activation. Cancellation compares the Preview ETag. Stale = 412; absent = 428. Wildcard, weak tags and lists are rejected. |
| `Idempotency-Key` | `header` | yes | `string` | Required on every mutation. Scope = organization + project + operation; fingerprint includes raw body bytes, media type, resource and If-Match. Same key/content replays the same receipt; changed content is 409. Retained for 86400 seconds; reconcile an ambiguous outcome within retention before retry, never silently allocate a new key. |
| `X-CSRF-Token` | `header` | yes | `string` | Session-bound synchronizer token from the trusted BFF bootstrap, independent of the unreadable session cookie. Validate same-origin Origin and CSRF before mutation. This contract does not implement or provision the session/CSRF exchange. |
| `body` | body | yes | `PreviewRequest` |  |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `202` | Accepted for asynchronous processing; not a completed effect. | application/json (Preview) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `409` | idempotency_conflict/reconcile_idempotency, binding_conflict/refresh_snapshot, or retry_requires_reconciliation/refresh_snapshot. No additional effect. | application/json (allOf&lt;ApiError, object&gt;) |
| `412` | precondition_failed; recovery=refresh_snapshot. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `413` | request_too_large; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `415` | unsupported_media_type; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `428` | precondition_required; recovery=refresh_snapshot. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "body": {
    "configurationRevisionId": "example"
  },
  "content_type": "application/json",
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    },
    {
      "in": "header",
      "name": "If-Match",
      "value": "\"A\""
    },
    {
      "in": "header",
      "name": "Idempotency-Key",
      "value": "AAAAAAAAAAAAAAAA"
    },
    {
      "in": "header",
      "name": "X-CSRF-Token",
      "value": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.previews.create("example", "\"A\"", "AAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", {"configurationRevisionId": "example"}, { contentType: "application/json" });
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJjcmVhdGVQcmV2aWV3In0 -->

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJwcmV2aWV3cy5nZXQiLCJtZXRob2QiOiJHRVQiLCJvcGVyYXRpb25faWQiOiJnZXRQcmV2aWV3IiwicGF0aCI6Ii92MS9wcm9qZWN0cy97cHJvamVjdElkfS9wcmV2aWV3cy97cHJldmlld0lkfSIsInJlc291cmNlIjoicHJldmlld3MiLCJzZWN0aW9uX3NoYTI1NiI6IjkyMmY5ODA0NDJhMGMwMzUyY2I2NzAzMzBjYzE1MDdkYTFmNWMxMzMxNzdmMTJlZDlhYWQ1Y2QwNzAyNzJiNjAiLCJzaWduYXR1cmVfc2hhMjU2IjoiODU4ODQyOWEzZmVlNzM3Y2Y4ZDgyM2E5NjYwZGQzZmFkMWE3OTY0OTQwZWNjMTEzNTNkYzMxYTU4NDIyYzlkZCJ9 -->
### `client.previews.get`

Operation ID: `getPreview`  
Route: `GET` `/v1/projects/{projectId}/previews/{previewId}`  
Equivalent member: `client.getPreview`  

#### Signature

```javascript
client.previews.get(projectId, previewId, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `previewId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `200` | Authorized resource snapshot. | application/json (Preview) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    },
    {
      "in": "path",
      "name": "previewId",
      "value": "example"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.previews.get("example", "example");
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJnZXRQcmV2aWV3In0 -->

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJwcmV2aWV3cy5nZXRFdmVudHMiLCJtZXRob2QiOiJHRVQiLCJvcGVyYXRpb25faWQiOiJnZXRQcmV2aWV3RXZlbnRzIiwicGF0aCI6Ii92MS9wcm9qZWN0cy97cHJvamVjdElkfS9wcmV2aWV3cy97cHJldmlld0lkfS9ldmVudHMiLCJyZXNvdXJjZSI6InByZXZpZXdzIiwic2VjdGlvbl9zaGEyNTYiOiJhZGQ1YzM2M2U1ZjI1MjY0NzFmNmNkNjRiNDQxOGJjNjc1YWEwZjlkYjgxZjUzYjEwMmM0MzMwMDlkYTEwNzdjIiwic2lnbmF0dXJlX3NoYTI1NiI6Ijc0MmZjMzA2ZTc5OTE4MTZmMzZiYTlhOTBhMDA0OTIwMDE0ZTkxNmJmYTVmY2RhNGNkNTU1ZTY3YTU5M2UzZDIifQ -->
### `client.previews.getEvents`

Operation ID: `getPreviewEvents`  
Route: `GET` `/v1/projects/{projectId}/previews/{previewId}/events`  
Equivalent member: `client.getPreviewEvents`  

#### Signature

```javascript
client.previews.getEvents(projectId, previewId, optionalArguments?, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `previewId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `cursor` | `query` | no | `Cursor` | Opaque scope-bound continuation, never an offset or authority token. Expired/gap = 410 refresh_snapshot; invalid/tampered/wrong filters = 422. Denied objects remain uniform404. |
| `limit` | `query` | no | `integer` | Maximum page size; default 50. |
| `Last-Event-ID` | `header` | no | `Cursor` | SSE resume cursor; replay begins strictly after it. If query cursor also occurs the two must match, otherwise 422. Reauthorization is mandatory on reconnect. |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `200` | Authorized resource snapshot. | application/json (EventPage), text/event-stream (string) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `410` | cursor_expired; recovery=refresh_snapshot. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    },
    {
      "in": "path",
      "name": "previewId",
      "value": "example"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.previews.getEvents("example", "example");
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJnZXRQcmV2aWV3RXZlbnRzIn0 -->

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJwcmV2aWV3cy5nZXRMb2dzIiwibWV0aG9kIjoiR0VUIiwib3BlcmF0aW9uX2lkIjoiZ2V0UHJldmlld0xvZ3MiLCJwYXRoIjoiL3YxL3Byb2plY3RzL3twcm9qZWN0SWR9L3ByZXZpZXdzL3twcmV2aWV3SWR9L2xvZ3MiLCJyZXNvdXJjZSI6InByZXZpZXdzIiwic2VjdGlvbl9zaGEyNTYiOiJkZTYyYzY0ZTI4OGJiOWYyY2Y1MGIzZjNlMTdhZWU4ZDVmOTJhYTdjYzhjNTlmYzM3OWQwYjViM2E3ZDIyZGU0Iiwic2lnbmF0dXJlX3NoYTI1NiI6IjQ4MDU2ZmFlZTEyN2U0OTBjNjNmMWVlOWNmMTRjOTRmMmUwMTNjMzNhODBkODE2YzY2NzI4MWVmZjM2ZTVkODUifQ -->
### `client.previews.getLogs`

Operation ID: `getPreviewLogs`  
Route: `GET` `/v1/projects/{projectId}/previews/{previewId}/logs`  
Equivalent member: `client.getPreviewLogs`  

#### Signature

```javascript
client.previews.getLogs(projectId, previewId, cursor?, limit?, level?, phaseId?, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `previewId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `cursor` | `query` | no | `Cursor` | Opaque scope-bound continuation, never an offset or authority token. Expired/gap = 410 refresh_snapshot; invalid/tampered/wrong filters = 422. Denied objects remain uniform404. |
| `limit` | `query` | no | `integer` | Maximum page size; default 50. |
| `level` | `query` | no | `string` |  |
| `phaseId` | `query` | no | `OpaqueId` |  |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `200` | Authorized resource snapshot. | application/json (LogPage) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `410` | cursor_expired; recovery=refresh_snapshot. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    },
    {
      "in": "path",
      "name": "previewId",
      "value": "example"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.previews.getLogs("example", "example");
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJnZXRQcmV2aWV3TG9ncyJ9 -->

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJwcmV2aWV3cy5saXN0IiwibWV0aG9kIjoiR0VUIiwib3BlcmF0aW9uX2lkIjoibGlzdFByZXZpZXdzIiwicGF0aCI6Ii92MS9wcm9qZWN0cy97cHJvamVjdElkfS9wcmV2aWV3cyIsInJlc291cmNlIjoicHJldmlld3MiLCJzZWN0aW9uX3NoYTI1NiI6IjQ5YTg0NzEyZjNkMzcxYTNiMzI5ZTBkZDM0MTc2MzY1YmQwMWRhMDkwZTNiZThiNTY2YmY4Mjg4YzI0MmQyNGEiLCJzaWduYXR1cmVfc2hhMjU2IjoiOTk2MjhlNTYxNDRiMTk5NzQ2Y2QwNjA1NTc2ZTQ3NmRjZWFiMWZiMzQxYzUzOTUxZjBjM2YxZjJiZmUwNjM2ZCJ9 -->
### `client.previews.list`

Operation ID: `listPreviews`  
Route: `GET` `/v1/projects/{projectId}/previews`  
Equivalent member: `client.listPreviews`  

#### Signature

```javascript
client.previews.list(projectId, cursor?, limit?, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `cursor` | `query` | no | `Cursor` | Opaque scope-bound continuation, never an offset or authority token. Expired/gap = 410 refresh_snapshot; invalid/tampered/wrong filters = 422. Denied objects remain uniform404. |
| `limit` | `query` | no | `integer` | Maximum page size; default 50. |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `200` | Authorized resource snapshot. | application/json (PreviewPage) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `410` | cursor_expired; recovery=refresh_snapshot. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.previews.list("example");
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJsaXN0UHJldmlld3MifQ -->

## Resource `projects`

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJwcm9qZWN0cy5nZXQiLCJtZXRob2QiOiJHRVQiLCJvcGVyYXRpb25faWQiOiJnZXRQcm9qZWN0IiwicGF0aCI6Ii92MS9wcm9qZWN0cy97cHJvamVjdElkfSIsInJlc291cmNlIjoicHJvamVjdHMiLCJzZWN0aW9uX3NoYTI1NiI6ImFhOGQyZWY4ZWNhNzkxNTc1MzM2OTAxODliODlkOGI0NmQ3OTliYjdhNTI2Y2NhOTNmYjRlNjg0NTA2ZmVmYmMiLCJzaWduYXR1cmVfc2hhMjU2IjoiMThhZjM5YWFiNDFmZWM4ZjY4Y2E5MzZlOTMzYTQzOTNmYTU0YWY2YmIwYzZjMGM3ODcxYzllNDVkOWU5MDYxNyJ9 -->
### `client.projects.get`

Operation ID: `getProject`  
Route: `GET` `/v1/projects/{projectId}`  
Equivalent member: `client.getProject`  

#### Signature

```javascript
client.projects.get(projectId, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `200` | Authorized resource snapshot. | application/json (Project) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.projects.get("example");
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJnZXRQcm9qZWN0In0 -->

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJwcm9qZWN0cy5saXN0IiwibWV0aG9kIjoiR0VUIiwib3BlcmF0aW9uX2lkIjoibGlzdFByb2plY3RzIiwicGF0aCI6Ii92MS9wcm9qZWN0cyIsInJlc291cmNlIjoicHJvamVjdHMiLCJzZWN0aW9uX3NoYTI1NiI6Ijc0NDRjNDUxNDdlMDkxMzJmYWQyMzU5MzYzMzFiMDJiZWEyOTJlMGJiNGU5ZTBjZjBjNzNkOTY4OGI5OWI0YTAiLCJzaWduYXR1cmVfc2hhMjU2IjoiYWFiYTY1OTE1NjgzMzU2NDBmMmNiYzZkZGE5YWZkZjVhYTZmNmFlMDU5NjU2ZDNhOGZlNDFkODA2YmQyM2M2ZiJ9 -->
### `client.projects.list`

Operation ID: `listProjects`  
Route: `GET` `/v1/projects`  
Equivalent member: `client.listProjects`  

#### Signature

```javascript
client.projects.list(cursor?, limit?, query?, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `cursor` | `query` | no | `Cursor` | Opaque scope-bound continuation, never an offset or authority token. Expired/gap = 410 refresh_snapshot; invalid/tampered/wrong filters = 422. Denied objects remain uniform404. |
| `limit` | `query` | no | `integer` | Maximum page size; default 50. |
| `query` | `query` | no | `string` | Display-name substring filter, case-insensitive Unicode NFC matching. Bound to pagination cursor. |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `200` | Authorized resource snapshot. | application/json (ProjectPage) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `410` | cursor_expired; recovery=refresh_snapshot. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "parameters": []
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.projects.list();
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJsaXN0UHJvamVjdHMifQ -->

## Resource `sources`

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJzb3VyY2VzLmNyZWF0ZVJldmlzaW9uIiwibWV0aG9kIjoiUE9TVCIsIm9wZXJhdGlvbl9pZCI6ImNyZWF0ZVNvdXJjZVJldmlzaW9uIiwicGF0aCI6Ii92MS9wcm9qZWN0cy97cHJvamVjdElkfS9zb3VyY2UtcmV2aXNpb25zIiwicmVzb3VyY2UiOiJzb3VyY2VzIiwic2VjdGlvbl9zaGEyNTYiOiJjNmUxM2NjMzY1MDdlN2Q5YmMzZjFiNjg3OGQ2Njk2Y2IxNjJmMTVhMjA1NmMxOWQzNDMwMTg3MTlkYTBlMzBiIiwic2lnbmF0dXJlX3NoYTI1NiI6IjNjOTM4Mzg1NGFkOGVhYTA3NTYyN2M0MDcxN2VmY2NhMGMzOThmNzE5ZTk1YjI1MTg2YjdkNjEwYTYzNDlkZTIifQ -->
### `client.sources.createRevision`

Operation ID: `createSourceRevision`  
Route: `POST` `/v1/projects/{projectId}/source-revisions`  
Equivalent member: `client.createSourceRevision`  

#### Signature

```javascript
client.sources.createRevision(projectId, Idempotency_Key, X_CSRF_Token, displayName, body, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `Idempotency-Key` | `header` | yes | `string` | Required on every mutation. Scope = organization + project + operation; fingerprint includes raw body bytes, media type, resource and If-Match. Same key/content replays the same receipt; changed content is 409. Retained for 86400 seconds; reconcile an ambiguous outcome within retention before retry, never silently allocate a new key. |
| `X-CSRF-Token` | `header` | yes | `string` | Session-bound synchronizer token from the trusted BFF bootstrap, independent of the unreadable session cookie. Validate same-origin Origin and CSRF before mutation. This contract does not implement or provision the session/CSRF exchange. |
| `displayName` | `query` | yes | `string` | Escaped display text only, never used as a filename or storage key; included in idempotency fingerprint. |
| `body` | body | yes | `any` |  |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `202` | Accepted for asynchronous processing; not a completed effect. | application/json (SourceRevision) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `409` | idempotency_conflict/reconcile_idempotency, binding_conflict/refresh_snapshot, or retry_requires_reconciliation/refresh_snapshot. No additional effect. | application/json (allOf&lt;ApiError, object&gt;) |
| `413` | request_too_large; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `415` | unsupported_media_type; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "body": "example",
  "content_type": "application/json",
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    },
    {
      "in": "header",
      "name": "Idempotency-Key",
      "value": "AAAAAAAAAAAAAAAA"
    },
    {
      "in": "header",
      "name": "X-CSRF-Token",
      "value": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    },
    {
      "in": "query",
      "name": "displayName",
      "value": "example"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.sources.createRevision("example", "AAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "example", "example", { contentType: "application/json" });
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJjcmVhdGVTb3VyY2VSZXZpc2lvbiJ9 -->

<!-- omniwrap-api-operation eyJleGFtcGxlX3JlYXNvbiI6bnVsbCwiZXhhbXBsZV9zdGF0dXMiOiJnZW5lcmF0ZWQiLCJtZW1iZXIiOiJzb3VyY2VzLmdldFJldmlzaW9uIiwibWV0aG9kIjoiR0VUIiwib3BlcmF0aW9uX2lkIjoiZ2V0U291cmNlUmV2aXNpb24iLCJwYXRoIjoiL3YxL3Byb2plY3RzL3twcm9qZWN0SWR9L3NvdXJjZS1yZXZpc2lvbnMve3JldmlzaW9uSWR9IiwicmVzb3VyY2UiOiJzb3VyY2VzIiwic2VjdGlvbl9zaGEyNTYiOiJiNWQ4NWMwODJjODJjYTgxOTY0M2VmZWYyMmEzOTM4ZDQ5OGE5YzU5ZTRmMWU3MjI5OWNhNzc3NjEzNTAwNTQyIiwic2lnbmF0dXJlX3NoYTI1NiI6IjRhNmYxZjJiMzI4ZWI2MTE0ZWVjMDMwZDhiOTc5MWY3NzhhYTJiZjYzNzBjNjI0NGEzNTU3OTU0Nzg1MTljNzcifQ -->
### `client.sources.getRevision`

Operation ID: `getSourceRevision`  
Route: `GET` `/v1/projects/{projectId}/source-revisions/{revisionId}`  
Equivalent member: `client.getSourceRevision`  

#### Signature

```javascript
client.sources.getRevision(projectId, revisionId, requestOptions?)
```

#### Parameters

| Name | In | Required | Contract type | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |
| `revisionId` | `path` | yes | `OpaqueId` | Opaque identity; authorize organization/project and verify every parent relation before lookup or mutation. Knowledge of an ID grants no access. |

#### Responses

| Status | Description | Content |
| --- | --- | --- |
| `200` | Authorized resource snapshot. | application/json (SourceRevision) |
| `401` | unauthenticated; recovery=authenticate. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `403` | forbidden; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `404` | not_found; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `406` | not_acceptable; recovery=none. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `422` | invalid_request, source_not_valid or cursor_invalid; never reinterpret an invalid source as ready. | application/json (allOf&lt;ApiError, object&gt;) |
| `429` | rate_limited; recovery=retry_same_request. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `500` | internal_error; recovery=reconcile_idempotency. See the normative error mapping and operation retry policy. | application/json (allOf&lt;ApiError, object&gt;) |
| `503` | configuration_required/configure_authority when approved JackAI exchange or product configuration is absent; authority_unavailable/retry_same_request on outage/timeout. No fallback identity, cached authorization or synthetic data. | application/json (allOf&lt;ApiError, object&gt;) |

#### Canonical required-input example

```json
{
  "parameters": [
    {
      "in": "path",
      "name": "projectId",
      "value": "example"
    },
    {
      "in": "path",
      "name": "revisionId",
      "value": "example"
    }
  ]
}
```

#### SDK call example

Example status: `generated`  
```javascript
const result = await client.sources.getRevision("example", "example");
```

<!-- omniwrap-api-operation-end eyJvcGVyYXRpb25faWQiOiJnZXRTb3VyY2VSZXZpc2lvbiJ9 -->

