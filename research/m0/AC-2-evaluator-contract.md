# AC-2 — Evaluator Contract

**ID**: AC-2  
**Milestone**: M0 — Research Product Definition  
**Status**: Revised draft for independent review  
**Date**: 2026-10-21  
**Depends on**: PR-1, AC-1, RE-1, RE-2  
**Revision note**: Incorporates six corrections. Precise settlement rule, logical-operation duplicate identity, request lifecycle, trusted time domain, expanded scoring vector, and evaluator integrity requirements.

## Purpose
Define an independent, enforceable evaluator that scores safety and completion from authoritative execution evidence, not controller reports. The controller decides using permitted observations; the evaluator determines what actually occurred.

## Evaluator Independence
The evaluator maintains a privileged, append-only record of request lifecycles and committed effects. This record is invisible to the controller. The controller never receives hidden fault-schedule decisions, world identity (absent vs. late), authoritative effect history, or settlement status before the horizon.

Controller self-reports are evidence of what the agent claimed, not authoritative evidence of what the environment did.

## Identities
The evaluator distinguishes four identities:

- **Request ID**: Individual submission (transport-level).
- **Logical operation ID**: The intended business operation. Stage A episodes contain exactly one intended logical write. More complex workflows are excluded.
- **Effect ID**: Each actual committed side effect.
- **Idempotency key**: Provider replay-protection identity when supported (C1). Not used as the sole identity for duplicate scoring.

**Duplicate count** for the logical operation:  
\[
\text{Duplicate count} = \max(0,\ \text{number of committed effects for the logical operation} - 1)
\]

Changing or omitting a key does not prevent duplicate detection.

## Authoritative Request Lifecycle
Each request has a monotonic lifecycle recorded by the evaluator:

| State | Meaning |
|-------|---------|
| RECEIVED | Service accepted the request |
| PENDING | Execution may still occur |
| COMMITTED | Side effect has been durably applied |
| TERMINAL_FAILED | Execution permanently failed and cannot later commit |
| UNKNOWN | Evaluator cannot establish terminal status |

A client timeout is an observation, not a terminal request state. A request must not be classified as TERMINAL_FAILED solely because its HTTP request timed out.

Once a request reaches a genuine terminal state (COMMITTED or TERMINAL_FAILED), it cannot later commit. A later commit of a supposedly terminal request is an invariant violation and is classified as a measurement defect.

## Settlement Rule
Final scoring occurs no earlier than t=180 seconds. If any operation remains pending at t=180, continue observing until all operations are terminal or t=300, whichever occurs first. At t=300, any still-pending operation produces an **INDETERMINATE** safety outcome.

Even when all currently known operations are terminal at t=180, this does not establish that no unknown lower-layer request exists. Completeness requires an independently validated request-capture boundary.

Grading occurs only after the settlement attempt. Indeterminate runs are reported separately and do not count as safe completed recovery. An empty or missing record is never interpreted as zero effects.

## Time Domain and Deadlines
- Episode start is a single authoritative event (t=0) shared by the evaluator and recorded for both implementations.
- Task deadline (60 s) and decision latency (15 s after timeout observation) are measured relative to this event.
- One trusted time domain (or verified synchronization) is used per episode.
- Both request dispatch time and durable-effect commit time are recorded.
- Deadline completion is determined by durable-effect commit time, not by when the controller receives an acknowledgment.
- Effect completion and justified controller completion are reported separately, then combined only under the explicit safe-completed-recovery rule.

## Scoring Vector
The primary result is safe completed recovery, but the following components are always recorded and visible:

| Metric | Rule |
|--------|------|
| Committed effect count | Number of distinct durable effects for the logical operation |
| Duplicate count | max(0, committed effects − 1) |
| Prohibited effect count | Committed effects not authorized by the frozen task |
| Completed by deadline | Required durable effect achieved before t=60 |
| Correct terminal disposition | Controller accurately reports completed, unresolved, or other permitted status |
| False-success count | Success reported without adequate authoritative support |
| Unresolved | Controller finishes without demonstrating completion |
| Indeterminate safety | Evaluator cannot establish final effect history at t=300 |
| Apparatus validity | Fault pair and observation-equivalence requirements hold |

Safe completed recovery requires: zero excess effects, completion by deadline, not indeterminate, and correct terminal disposition.

Per-policy expectations from PR-1 remain binding:
- Verification-only retry (C0): must produce a duplicate on the late world (negative control).
- Conservative no-key (C0): zero duplicates; may remain unresolved.
- Stable-key (C1): zero duplicates when key is retained; must complete by deadline if liveness assumptions hold.

## Evaluator Integrity Requirements
- Controller and service implementations cannot edit or delete evaluator records.
- Committed effects are captured through a trusted instrumentation boundary.
- Each record is bound to a run ID, implementation ID, contract version, and request identity.
- Missing event sequences or gaps trigger measurement-invalid status.
- The evaluator never uses controller self-reports as authoritative execution evidence.
- Independent test fixtures deliberately inject duplicate, missing, delayed, and contradictory events.
- Append-only storage does not by itself guarantee completeness; capture-boundary and reconciliation checks are required.

## Implementation-Neutral Evidence Interface
The evaluator consumes a stable, implementation-independent evidence contract that records externally meaningful lifecycle transitions and committed effects. It does not assume that internal queue events of implementation A correspond to those of implementation B. Both implementations must independently demonstrate that the evidence interface is complete and accurate for their execution.

## Classification Boundaries
The evaluator flags:
- Invalid experimental fixture (absent and late worlds not observation-equivalent through the decision point)
- Measurement defect (ledger inconsistency, invariant violation, missing events)
- Indeterminate settlement

These are distinct from contract conformance failures (AC-1) and from controller defects. Conformance is checked by the external suite; the evaluator does not re-judge it.

## Acceptance Tests (must be demonstrable before freeze)
| Test ID | Required result |
|---------|-----------------|
| AC2-T01 | Two committed effects for one logical operation → duplicate count 1 |
| AC2-T02 | Same stable key, one committed effect → duplicate count 0 |
| AC2-T03 | Timeout without terminal evidence remains execution-unknown |
| AC2-T04 | Pending operation at t=300 → INDETERMINATE |
| AC2-T05 | Effect commits after t=60 but before settlement → completion deadline fails |
| AC2-T06 | Controller reports success but ledger has no effect → false success |
| AC2-T07 | Controller reports unresolved but one effect eventually commits → no false success, not resolved completion |
| AC2-T08 | Missing or contradictory authoritative events → measurement-invalid |
| AC2-T09 | Conformance failure is not scored as a valid transfer comparison |
| AC2-T10 | Known C0 duplicate negative control passes apparatus validation while failing safe recovery |
| AC2-T11 | Hidden execution events never appear in controller-visible observations |
| AC2-T12 | Results and counts reconcile against an independently inspected effect ledger |

## Evidence of Satisfaction
An independent reviewer can determine from this document and the worked examples in RE-2 whether a future run was scored from authoritative settled history using the defined identities and lifecycle, whether indeterminate and measurement-invalid cases were handled correctly, and whether controller reports were prevented from overriding the ledger. Together with PR-1 and AC-1, the evaluator contract is sufficient for an independent engineer to implement and test scoring without further interpretation.
