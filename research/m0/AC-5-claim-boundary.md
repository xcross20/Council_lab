# AC-5 — Claim Boundary

**ID**: AC-5  
**Milestone**: M0 — Research Product Definition  
**Status**: Revised draft for independent review  
**Date**: 2026-10-21  
**Depends on**: PR-1, PR-2, AC-3, AC-4  
**Revision note**: Tightens apparatus claims to tested cases. Adds permitted claims for negative and indeterminate results. Introduces evidence strength levels (L0–L3). Prohibits post-hoc redefinition of primary hypotheses.

## Purpose

Define the limits of what a Stage A result may claim, so that apparatus validation, implementation transfer, negative results, and research novelty remain distinct.

## Evidence Strength Levels

These are evidence-strength levels, not novelty rankings.

| Level | Description |
|-------|-------------|
| L0 | Illustrative / proposed. Documentation, synthetic worked examples, hypothetical traces, or unexecuted test cases. No empirical outcome claim. |
| L1 | Executed and validated. Observed behavior with independently checked apparatus and recorded evidence, limited to the specific tested conditions. |
| L2 | Independently replicated. The result survives a prespecified independent replication with appropriately separated implementation or evaluation. |
| L3 | Broader empirical support. Evidence survives additional implementations, relevant workflow families, and independent validation. Generalization remains bounded by the sampled conditions. |

An L3 replication of established work may still contain no novel contribution. An L1 observation may motivate a new hypothesis without establishing it.

## Permitted Claims by Result

| Experimental result | Permitted claim |
|---------------------|-----------------|
| Requirements hold in A and B | Transfer observed under the tested implementations, faults, and contract |
| Requirements hold in A but fail in conforming B | Transfer hypothesis not supported for that stratum |
| B violates the external contract | Service conformance failure; no eligible B transfer result |
| Fixture fails observation equivalence | Invalid experimental comparison |
| Safety remains indeterminate at settlement | Final safety not established for that episode |
| Only known late-commit effects reproduced | Independent replication; no new mechanism established |
| New audited interaction reproduced | Candidate scientific contribution, subject to prior-art and independent confirmation |

A failed transfer result can be scientifically more informative than a successful replication.

## What Stage A Can Establish

Stage A can demonstrate that the evaluator, settlement rules, and classification procedure correctly adjudicate the prespecified test cases within their independently validated evidence-capture and contract boundaries.

It can establish that the late-commit / observational non-identifiability limitation and the benefit of enforced stable-key semantics can be realized and measured under an independently implemented asynchronous service that passes the same frozen external contract.

## What Stage A Cannot Establish

- An LLM reasoning, contract-interpretation, or policy-learning result.
- Production validity or robustness under arbitrary real-world services, load, or failure modes beyond the frozen contract and prespecified faults.
- Novelty solely from independent implementation.
- That a violation of stated assumptions refutes a published result.
- General sufficiency of the evaluator for arbitrary future workflows.

## Post-Hoc Redefinition Prohibition

Primary hypotheses, required outcomes, deadlines, exclusions, and analysis criteria remain frozen throughout a study. Post hoc observations may motivate explicitly labeled exploratory findings or a newly preregistered experiment, but cannot retroactively redefine the original result.

## Novelty Gate

A result supports a novelty claim only when apparatus validity and transfer assessment are complete, the finding is not a pure replication of known results, the audited discrepancy is not already characterized by the relevant prior literature, and classification and the bounded audit have been applied. Unresolved cases do not support novelty.

## Evidence of Satisfaction

An independent reviewer can classify each proposed conclusion as permitted, prohibited, or requiring additional evidence, without consulting the author's intentions.
