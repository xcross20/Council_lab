# AC-3 — Classification Table

**ID**: AC-3  
**Milestone**: M0 — Research Product Definition  
**Status**: Draft for independent review  
**Date**: 2026-10-21  
**Depends on**: PR-1, AC-1, AC-2, RE-1, RE-2

## Purpose
Provide a mutually exclusive, auditable classification for every observed discrepancy so that a third party can determine whether a result is a conformance failure, a controller defect, an invalid experimental fixture, a measurement defect, a permitted implementation sensitivity, or a specification incompleteness. Classification explains a result; it does not convert a failed transfer hypothesis into a pass.

## Classification Categories

| Category | Definition | Primary evidence | Effect on transfer assessment |
|----------|------------|------------------|-------------------------------|
| Conformance failure | Service violates a guarantee in the frozen external contract (AC-1) | External conformance suite failure | Implementation excluded from transfer assessment for that stratum |
| Controller defect | Unchanged controller violates an explicit requirement of the frozen contract or PR-1 policy under a conforming service | Controller action or disposition contradicts the policy table or contract | Transfer hypothesis fails for that stratum |
| Invalid experimental fixture | Absent and late worlds do not present matching controller-visible histories through the decision point, or required fault conditions were not realized | Observation-equivalence check fails | Run is invalid; not used for transfer assessment |
| Measurement defect | Evaluator ledger is incomplete, inconsistent, or violates a monotonicity invariant (AC-2) | Missing events, contradictory records, or terminal-state violation | Run is measurement-invalid; not used for scientific claim |
| Permitted implementation sensitivity | Different allowed schedules or internal timings produce different outcomes while both implementations conform and fixtures are valid | Cross-implementation difference within contract-permitted variation | Recorded; does not automatically fail transfer |
| Specification incompleteness | Frozen contract leaves a consequential question unspecified that affected the outcome | Audit shows both implementations followed the written contract yet diverged on an underspecified point | Recorded; may justify a follow-on specification clarification |
| Unresolved | Bounded audit (AC-4) completed without establishing a cause | Audit log | Does not support transfer or novelty claim |

## Decision Procedure
1. Check external conformance (AC-1). Failure → Conformance failure. Stop for that implementation/stratum.
2. Check fixture validity (observation equivalence through decision point). Failure → Invalid experimental fixture.
3. Check evaluator integrity and settlement (AC-2). Failure → Measurement defect or Indeterminate.
4. Apply the unchanged controller against the settled ledger and PR-1 requirements. Violation → Controller defect (transfer hypothesis fails).
5. If both implementations conform, fixtures are valid, evaluator is sound, and outcomes differ within contract-permitted variation → Permitted implementation sensitivity.
6. If the difference is not explained by the written contract → Specification incompleteness or Unresolved after audit.

Classification is recorded with evidence pointers. It does not override the binary transfer-hypothesis outcome defined in PR-1.

## Evidence of Satisfaction
An independent reviewer can apply this table to any future run record and reach the same category, and can confirm that a classified discrepancy did not convert a failed transfer hypothesis into a successful one.
