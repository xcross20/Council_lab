# AC-4 — Continuation Gate

**ID**: AC-4  
**Milestone**: M0 — Research Product Definition  
**Status**: Revised draft for independent review  
**Date**: 2026-10-21  
**Depends on**: PR-1, PR-2, AC-3  
**Revision note**: Redefines gate outputs as precise decisions. Distinguishes unresolved causal attribution from a justified new scientific question. Clarifies audit budget boundaries.

## Purpose
Define the bounded audit process and the separate research-continuation decision so that a valid negative result, a broken apparatus, an unresolved incident, and a justified new hypothesis remain distinguishable.

## Three Gates with Precise Outputs
| Gate | Possible decision | Meaning |
|------|-------------------|---------|
| G1 — Apparatus validity | VALID / INVALID / PARTIAL | Are the relevant results interpretable? |
| G2 — Transfer assessment | SUPPORTED / NOT_SUPPORTED / INCONCLUSIVE | Did the unchanged controller meet the prespecified transfer requirements? |
| G3 — Research continuation | AUTHORIZE / NARROW / STOP / DEFER | Is another study justified? |

G2 can be NOT_SUPPORTED while G1 is VALID. A valid experiment that falsifies the transfer hypothesis is a scientifically useful outcome.

## Bounded Audit
Any discrepancy that is not immediately classified as a conformance failure, invalid fixture, or measurement defect receives a fixed audit budget:
- 4 person-hours
- One controlled reproduction or removal attempt

**Validity remediation** (correcting a known defective evaluator or invalid fixture, followed by revalidation) is distinct from **discrepancy attribution** (investigating an unexpected outcome in an otherwise valid experiment). Re-execution is recorded and cannot silently replace the original run. Material protocol changes require a new approved version.

A cause is considered established only when a controlled change removes or reproduces the discrepancy. Unresolved causal attribution after the budget does not support a novelty claim and does not automatically authorize continuation.

## Continuation Criteria
Research continuation requires an evidence-grounded, falsifiable follow-up question, supported by:
1. A validated observation (G1 VALID or PARTIAL with clear scope).
2. A documented prior-art gap (PR-2).
3. A feasible experiment that distinguishes at least two competing explanations.

Pure replication of known late-commit or stable-key results does not clear G3. An unresolved causal attribution alone does not justify continuation.

## Illustrative Continuation Decision Record
| Field | Example |
|-------|---------|
| Study | CT-001 (hypothetical) |
| Apparatus | VALID |
| Transfer finding | NOT_SUPPORTED |
| Observed difference | Conforming B misses a required deadline under an allowed schedule |
| Attribution | Controlled scheduling effect reproduced |
| Prior-art review | Additional review required |
| Continuation decision | DEFER |

Every continuation decision points to the relevant run evidence, audit record, literature assessment, and authorizing reviewer.

## Stop Rule
If no consequential, uncharacterized, falsifiable question survives the audit and prior-art review, Stage A ends after reporting. No expansion beyond the bounded validation and reporting work is authorized without a new decision.

## Evidence of Satisfaction
An independent reviewer can distinguish a scientifically valid negative result, a broken apparatus, an unresolved incident, and a justified new research hypothesis without granting automatic continuation.
