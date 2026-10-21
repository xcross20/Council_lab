# AC-3 — Classification Table

**ID**: AC-3  
**Milestone**: M0 — Research Product Definition  
**Status**: Revised draft for independent review  
**Date**: 2026-10-21  
**Depends on**: PR-1, AC-1, AC-2, RE-1, RE-2  
**Revision note**: Replaces single exclusive categories with three independent dimensions (experiment validity, requirement outcome, cause attribution). Distinguishes INDETERMINATE from measurement invalid. Requires dual reporting populations.

## Purpose
Record three independent classifications for every episode so that experiment validity, requirement outcome, and cause attribution cannot overwrite one another. Classification explains a result; it does not convert a failed transfer hypothesis into a pass.

## Three Independent Classification Dimensions

| Dimension | Possible values | Question answered |
|-----------|-----------------|-------------------|
| Experiment validity | VALID, INVALID_FIXTURE, INVALID_MEASUREMENT, INDETERMINATE | Can this run support the intended comparison? |
| Requirement outcome | PASS, FAIL, NOT_ASSESSABLE | Did the controller satisfy the prespecified safety and completion requirements? |
| Cause attribution | SERVICE_CONFORMANCE, CONTROLLER_DEFECT, PERMITTED_SCHEDULING, SPECIFICATION_GAP, MEASUREMENT_DEFECT, UNRESOLVED (multiple allowed when independently supported) | What explains an observed discrepancy? |

Cause attribution may list multiple findings. A primary disposition may be chosen by precedence for operational convenience, but secondary defects are retained.

## Decision Procedure
1. Record the episode and immutable evidence references.
2. Evaluate service conformance independently (AC-1).
3. Validate the experimental fixture and observation-equivalence requirement.
4. Validate evaluator integrity and settlement completeness (AC-2).
5. Determine eligibility for the transfer contrast.
6. Score each prespecified safety, completion, and reporting requirement wherever evidence permits.
7. Record all observed discrepancies and conduct bounded causal attribution (AC-4).
8. Produce the transfer verdict without changing the underlying requirement outcome.
9. Preserve all invalid, unresolved, and excluded episodes in the study record.

## Key Distinctions
- A requirement violation establishes an outcome failure, not automatically a controller defect. Score the failed requirement first; then determine whether the controller violated its own prescribed decision rules.
- INDETERMINATE: complete and valid evidence of an unresolved request at the settlement cap. Not a measurement defect.
- INVALID_MEASUREMENT: missing, contradictory, or unreliable authoritative instrumentation.
- Invalid or ineligible comparisons are reported separately and cannot be counted as either success or failure of the scientific transfer contrast.
- A failed requirement in an eligible, valid transfer comparison counts against the prespecified hypothesis.

## Reporting Populations
- **Scheduled episodes**: Every prespecified episode, including invalid, cancelled, and indeterminate runs.
- **Eligible transfer comparisons**: Only episodes meeting the frozen apparatus and conformance prerequisites.

Both denominators and exclusion reasons are reported.

## Precondition Matrix (for eligibility)
- Contract stratum fixed?
- Both implementations conforming?
- Fault-pair fixture valid?
- Authoritative scoring reliable?
- Settlement completed or explicitly marked indeterminate?
- Unchanged policy and required input budget preserved?

## Evidence of Satisfaction
Two independent reviewers given the same evidence should produce identical eligibility, requirement, and attribution records—or identify precisely which field remains disputed.
