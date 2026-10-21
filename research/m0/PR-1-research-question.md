# PR-1 — Research Question, Falsifiable Claim, Success and Stop Criteria

**ID**: PR-1  
**Milestone**: M0 — Research Product Definition  
**Status**: Revised draft for independent review  
**Date**: 2026-10-21  
**Revision note**: Addresses logical consistency between claim, success criteria, and stop criteria; separates observation equivalence from cross-implementation conformance; introduces explicit contract strata and settlement rules; adds numerical deadlines and audit limits.

## Primary Researcher
An independent research engineer (or small group of 1–2) evaluating whether published agent-reliability interventions retain their reported benefits when the underlying service is independently implemented under an identical external contract. The researcher is not building a general agent platform, multi-agent framework, or production runtime.

## Research Question (Stage A — Implementation Transfer)
Within each frozen contract stratum, does an unchanged deterministic recovery controller satisfy the same prespecified safety and deadline-completion requirements across a reference implementation and an independently authored asynchronous implementation that passes the same external-contract conformance suite?

Only the service implementation and its internal scheduling change. Contract content, documentation, recovery policies, task, and scoring remain fixed.

## Transfer Hypothesis
Under the frozen contract and prespecified fault conditions, the unchanged controller satisfies the same safety and completion requirements in both implementations.

## Attribution Procedure (separate from the hypothesis)
Any discrepancy undergoes a bounded audit of service conformance, controller inputs, scheduling, and evaluator correctness. A cause is considered established only when a controlled change removes or reproduces the discrepancy. Discrepancies remaining unresolved after the audit are reported as unresolved and do not support a transfer or novelty claim.

Classification of a discrepancy does not convert a failed transfer hypothesis into a successful one. If the unchanged controller fails a prespecified safety or completion requirement in the independent implementation, the transfer hypothesis fails for that stratum, regardless of how the discrepancy is classified.

## Contract Strata
Implementation transfer is evaluated within each row. The C0-to-C1 comparison is a contract intervention, not pure implementation transfer.

| Contract | Description | Policies under test |
|----------|-------------|----------------------|
| C0 | Non-idempotent write without replay protection | Verification-only retry; Conservative no-key controller |
| C1 | Enforced stable-key semantics | Stable-key controller (same key on retry) |

## Policy Definitions
Each policy is a fixed state machine. “Contract-aware” is not used as an adjustable label.

| Policy | After timeout + empty/lagging read | Expected role |
|--------|-------------------------------------|---------------|
| Verification-only retry | Reissue without replay protection | Negative control: demonstrate known late-commit failure on C0 |
| Conservative no-key controller | Do not treat empty read as proof of non-execution; report unresolved unless another justified route exists | Measure safety versus completion on C0 |
| Stable-key controller | Reissue using the identity supplied on the original attempt | Test replay-protected recovery on C1 |

## Key Safety Assumptions (C1 only)
Provider-enforced deduplication establishes at-most-once under the following conditions, which must be stated and checked:

- The original attempt includes the key.
- Retries retain the key and identical operation parameters.
- Deduplication covers concurrent and delayed submissions.
- Protection does not expire during the episode.
- The service eventually processes an eligible request.
- The task deadline permits the intended successful recovery.

Duplicate prevention and deadline completion are scored separately.

## Times
Three clocks are distinct:

1. **Decision time**: Controller must issue its retry / unresolved decision within 15 seconds of the timeout observation. The original effect remains unobservable to the controller through this point.
2. **Task deadline**: 60 seconds from episode start for a completion to count as successful.
3. **Evaluation settlement horizon**: 180 seconds from episode start, or until all in-flight requests known to the evaluator have either committed or been confirmed terminal, whichever is later, capped at 300 seconds for the pilot. Late effects are captured by the evaluator during settlement. Completion is scored against the task deadline; duplicate and prohibited effects are scored over the full recorded execution through settlement.

If a request remains genuinely unsettled at the settlement horizon (request still pending with no terminal signal), the final safety outcome is labeled **indeterminate**. Grading occurs only after the settlement attempt; indeterminate runs are reported separately and do not count as safe completed recovery.

## Success Criteria (Apparatus Validity + Transfer Assessment)
### Apparatus Validity Gate
- Known controls behave correctly on the reference implementation.
- Both implementations pass the same external-contract conformance suite.
- Within each implementation, the absent and late worlds expose matching controller-visible histories through the prespecified retry decision.
- Evaluator scores against authoritative effect history; pending operations are settled before final grading (or labeled indeterminate if settlement cannot be established).
- No reliance on controller prose or self-reported completion.

### Transfer Assessment Gate
- The unchanged controller satisfies the prespecified safety and deadline-completion requirements in both implementations within each contract stratum, or any requirement violation is classified through the bounded audit.
- Cross-implementation timing differences permitted by the contract are recorded rather than automatically classified as defects.
- Exact matched-trace diagnostic (optional control) may be used; exact trace equivalence is not required for successful implementation transfer.

## Per-policy requirements
| Policy | Safety requirement | Completion requirement | Notes |
|--------|--------------------|------------------------|-------|
| Verification-only retry (C0) | Must produce a duplicate on the late world (known failure control) | May complete or not | Negative control; apparatus validity requires the duplicate |
| Conservative no-key controller (C0) | Zero duplicates | May remain unresolved | Safety-without-progress is acceptable; false success is not |
| Stable-key controller (C1) | Zero duplicates when key is present on first attempt and retained | Must complete by task deadline if the service eventually processes an eligible request under the stated liveness assumptions | Duplicate prevention and deadline completion scored separately |

## Material Requirement Violations (deterministic cases)
Any of the following constitutes a requirement violation:

- Any duplicate in a condition asserted duplicate-free.
- Any false success report.
- Any missed deadline in a condition with specified feasible completion.
- Any unrecorded unsettled operation.

## Stop / Continuation Criteria
| Gate | Passing evidence | Consequence |
|------|------------------|-------------|
| Apparatus validity | Known controls behave correctly; service and evaluator pass audits | Results become interpretable |
| Transfer assessment | Prespecified requirements hold or fail across implementations; discrepancies classified | Report transfer finding |
| Research continuation | A consequential unresolved question survives prior-art review and controlled diagnosis | Authorize another study |

A valid, successful replication can pass the first two gates and fail the third. Pure replication of the known late-commit / observational non-identifiability limitation does not establish novelty.

Unresolved discrepancies after the bounded audit do not support a transfer or novelty claim. Further investigation requires a new approval.

“No further implementation” means no expansion beyond the bounded validation and reporting work. Minor evaluator corrections required for validity do not trigger an automatic stop.

## Classification of Findings
- Service violates frozen contract → conformance failure.
- Documentation differs between conditions → protocol deviation.
- Controller violates explicit contract → controller defect.
- Different allowed schedules expose different outcomes → potentially legitimate implementation sensitivity.
- Frozen contract leaves a consequential question unspecified → specification incompleteness.
- Evaluator miscounts effects → measurement defect.

Classification explains a result; it does not convert a requirement violation into a pass.

## Audit Budget
Discrepancies receive a fixed budget of 4 person-hours plus one controlled reproduction attempt. Unresolved cases are reported without causal attribution. Further investigation requires a new approval.

## Claim Boundary
A successful deterministic Stage A validates execution semantics, recovery mechanisms, and evaluation methods only. It does not establish an LLM reasoning, contract-interpretation, or policy-learning result. Model-based policies are introduced only if the deterministic stage leaves a remaining scientific question that is not already characterized by existing work.

Model provenance limits model-specific comparison claims. Artifact availability limits exact reproduction claims. Neither automatically prevents an independently specified deterministic replication. No public Limbo artifact has been located as of 2026-10-21 following the documented search; the manuscript states code and data will be made available upon publication.

## Evidence of Satisfaction
This document, plus the related-work boundary (PR-2) and reference experience (RE-1), reviewed and approved by an independent reviewer who was not the primary author. A third party can determine from these documents alone whether a future experimental result meets or fails the criteria above.
