# AC-1 — Frozen External Specification and Independent Authorship Plan

**ID**: AC-1  
**Milestone**: M0 — Research Product Definition  
**Status**: Revised draft for independent review  
**Date**: 2026-10-21  
**Depends on**: PR-1, PR-2, RE-1, RE-2  
**Revision note**: Addresses five material gaps. Adds precise behavioral semantics, C1 conflict rules, fixed read-consistency contract, stronger authorship boundary, conformance traceability, and explicit distinction between contract conformance and experimental fault control.

## Purpose
Define a testable, frozen external contract that two independent implementations can satisfy without further interpretation, and the authorship and material-separation rules required for a valid Stage A implementation-transfer experiment.

## Frozen External Contract (Stage A)

The external contract is the only interface visible to the controller. Internal scheduling, persistence, queues, and effect-ledger mechanics are not part of the contract and may differ. Contract content, documentation, recovery policies, task, and scoring remain fixed.

### Shared Behavioral Semantics (both strata)

**Operation creation**  
Request: `POST /operations`  
- `operation_id` (client-generated, optional correlation)  
- `idempotency_key` (required for C1; ignored or rejected for C0)  
- `parameters` (normalized map; exact fields defined by the task schema)  
- `payload` (opaque for the service)  

Response (immediate):  
- `202 Accepted` + `operation_id` (request accepted; outcome not yet known)  
- `400 Bad Request` (parameter validation failure)  
- `409 Conflict` (C1 only: key reuse with different normalized parameters)  

**Status lookup**  
Request: `GET /operations/{operation_id}`  
Response:  
- `200` + `{status: "PENDING" | "COMMITTED" | "FAILED", effect_ref: optional}`  
- `404 NOT_FOUND` (no record of this operation_id)  
- Timeout or empty body is permitted and does not prove non-execution.

**Status values**  
- `PENDING`: accepted but not yet committed or failed.  
- `COMMITTED`: effect has been applied; effect_ref present.  
- `FAILED`: permanent failure; no effect.  
- Empty / timeout / lagging read is observation-equivalent to both absent and late-commit worlds through the controller decision point. An empty response is **not** proof of terminal absence.

**Acknowledgment loss**  
A lost or delayed acknowledgment does not cancel a previously accepted operation. The operation remains PENDING until it commits, fails, or the evaluation settlement horizon is reached.

**Read consistency (fixed for Stage A)**  
- Visibility lag is bounded by 2 seconds for status and effect reads once an operation has committed.  
- Implementations may realize longer internal delays before commit, but once committed the effect must become visible within 2 s.  
- This bound is relative to the 15 s decision window so that both implementations present equivalent information to the controller.

**Timing constraints (from PR-1)**  
- Controller decision must be issued within 15 s of the timeout observation.  
- Task deadline: 60 s from episode start.  
- Evaluation settlement horizon: 180 s, extendable to 300 s.

### C0 — Non-idempotent write without replay protection

- `idempotency_key` is ignored or rejected.  
- Two successful identical writes produce two distinct effects.  
- No provider-side deduplication.  
- Effect ledger records each committed write as a distinct side effect.

### C1 — Enforced stable-key semantics

One key + one normalized parameter set identify one logical operation for the duration of the episode.

- Original attempt must include the key.  
- Retries that present the same key and identical normalized parameters are deduplicated.  
- Deduplication covers concurrent and delayed submissions and does not expire during the episode.  
- Same key with different normalized parameters → `409 Conflict`; no second effect.  
- Concurrent same-key/same-parameters submissions produce at most one effect.  
- If the original request commits after a retry arrives, only one effect is recorded.  
- Permanent failure of the logical operation is reported as `FAILED` and does not produce an effect.  
- Effect ledger records at most one committed effect per key.

## Conformance vs. Experimental Fault Control

These are distinct:

- **Contract conformance**: The implementation satisfies all public behavioral guarantees above when exercised through the external interface. Checked by the public conformance suite.
- **Experimental fault control**: The research harness successfully creates the specified absent-world and late-commit-world conditions with matching controller-visible observations through the decision point. Failure to produce the required observation-equivalent pair is an invalid experimental fixture, not a contract violation.

A service can pass conformance and still produce an invalid fixture for a particular run. Only conforming implementations that also produce valid fixtures are eligible for the transfer assessment.

## Conformance Traceability Matrix

| Contract requirement | Positive test | Negative / boundary test |
|----------------------|---------------|--------------------------|
| C0 non-idempotent writes | Two identical writes produce two effects | Single write produces one effect |
| C1 stable-key protection | Concurrent same-key/same-payload produce ≤1 effect | Same key + different payload → 409, no second effect |
| C1 key lifetime | Deduplication holds across delayed submissions within episode | Key reuse after episode end is out of scope |
| Read consistency | Committed effect visible within 2 s | Empty/timeout does not prove absence |
| Acknowledgment loss | Lost ack leaves operation PENDING | Lost ack does not cancel operation |
| Status semantics | PENDING / COMMITTED / FAILED / NOT_FOUND returned correctly | Empty response permitted and non-conclusive |
| Pending settlement | Unsettled at 300 s → indeterminate (evaluator) | Service does not silently drop PENDING |
| Durable identity | Restart preserves documented guarantees for in-flight operations | N/A (external observable) |

The conformance suite inspects only the external interface. It does not inspect internal queues or storage.

## Independent Authorship Plan

### Public implementation materials (given to both teams)
- This external specification (versioned, hashed).  
- Machine-readable API sketch (OpenAPI or equivalent) derived from the above.  
- Representative request/response examples that do not reveal private fault schedules.  
- Documented timing constraints (2 s visibility, 15 s / 60 s / 180–300 s).

### Independent evaluation materials (withheld from implementation teams)
- Private fault schedules and hidden outcome worlds.  
- Expected scored traces and oracle ledgers from RE-2.  
- Evaluator fixtures and settlement oracles.

### Authorship rules
1. Reference implementation is written first. Its internal scheduling and persistence are not published.  
2. Independent implementation is authored by a separate engineer/team who receives only the public materials above.  
3. Authorship log records exactly which documents, libraries, and generated code each team accessed.  
4. Both implementations must pass the same external conformance suite before any transfer assessment.  
5. Shared code is limited to the unchanged controller policies and the evaluator. Service implementations share no internal components that implement contract semantics.  
6. The independent team does not receive private fault schedules, expected hidden ledgers, or reference internals.

A failing conformance result excludes that implementation from the transfer assessment for the affected stratum and is recorded as a conformance failure (AC-3), not a controller defect.

## Evidence of Satisfaction
An independent reviewer can determine from this document alone whether two engineers can implement the same public API without further interpretation, whether C0 and C1 guarantees are precise enough to test without internals, whether timeout / delayed commit / read visibility / replay identity are unambiguous, and whether public materials are separated from private evaluation materials. The authorship log and conformance results complete the record.
