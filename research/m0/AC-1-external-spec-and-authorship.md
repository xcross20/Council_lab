# AC-1 — Frozen External Specification and Independent Authorship Plan

**ID**: AC-1  
**Milestone**: M0 — Research Product Definition  
**Status**: Draft for independent review  
**Date**: 2026-10-21  
**Depends on**: PR-1, PR-2, RE-1, RE-2

## Purpose

Define the frozen external contract that both implementations must satisfy and the authorship separation required so that implementation transfer is measured rather than assumed.

## Frozen External Contract (Stage A)

The external contract is frozen before either implementation is written. Only the service implementation and its internal scheduling may differ. Contract content, documentation, recovery policies, task, and scoring remain fixed.

### C0 — Non-idempotent write without replay protection

- Write operation accepts no idempotency key (or ignores any key supplied).
- A timeout followed by an empty or lagging read is observation-equivalent between the absent world and the late-commit world through the controller’s decision point.
- No provider-side deduplication of identical logical operations.
- Effect ledger records each committed write as a distinct side effect.

### C1 — Enforced stable-key semantics

- Write operation requires a stable idempotency key on the original attempt.
- Retries that present the same key and identical operation parameters are deduplicated by the provider.
- Deduplication covers concurrent and delayed submissions and does not expire during the episode.
- Effect ledger records at most one committed effect per key.

### Shared requirements (both strata)

- External request/response schemas, status codes, and error semantics are identical.
- Read-path visibility lag is bounded by the contract or explicitly declared.
- Task deadline (60 s from episode start) and evaluation settlement horizon (180 s, extendable to 300 s) are identical.
- Controller decision must be issued within 15 s of the timeout observation.

## Independent Authorship Plan

1. **Reference implementation** is written first against the frozen external specification. Its internal scheduling, queueing, and durable operation state are not published.

2. **Independent implementation** is authored by a separate engineer (or team) who receives only:
   - The frozen external specification (C0 or C1 as applicable).
   - The public request/response examples from RE-2.
   - The conformance suite.
   - No access to reference source, internal logs, or scheduling implementation.

3. **Conformance gate**  
   Both implementations must pass the same external-contract conformance suite before any transfer assessment. Failure of the independent implementation on the conformance suite is recorded as a conformance failure and excludes that run from the transfer hypothesis evaluation.

4. **No shared internals**  
   Shared code is limited to the controller policies under test (which remain unchanged) and the evaluator. Service implementations remain independent.

## Evidence of Satisfaction

A third party can determine from this document, the frozen specification, and the authorship log whether the two implementations were produced under the required separation and whether both passed the same conformance suite.
