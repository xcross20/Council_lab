# PR-2 — Related-Work Boundary

**ID**: PR-2  
**Milestone**: M0 — Research Product Definition  
**Status**: Revised draft for independent review  
**Date**: 2026-10-21  
**Depends on**: PR-1  
**Revision note**: Corrects HTTP distinction, removes imperfect-documentation claim from Stage A, qualifies statistical attribution, broadens novelty boundary, and softens artifact-reconstruction inference.

## Purpose
Define the precise prior-art boundary for Stage A so that a third party can determine whether a future result is a replication of known work, a measurement of already-characterized effects, or a potential contribution beyond the existing literature.

## Primary Reference: Limbo
**Paper**: Jiapeng Li, *Where Does Exactly-Once Live? Model, Harness, and Tool-Contract Effects on Duplicate Side Effects in LLM Agents*, arXiv:2609.29095v1, submitted 24 September 2026 (preprint).  
**Affiliation**: Microsoft.  
**Artifact status**: Manuscript states “Code and data will be made available upon publication.” No public artifact repository has been located as of 2026-10-21 following a documented search (locations: arXiv abstract page, author-affiliated pages, common code-hosting searches). Unless an original artifact becomes available and is used, Council Lab’s reference implementation will be described as an independent reconstruction of the described semantics, not an exact artifact reproduction. Artifact-search date and locations will be recorded in an evidence log.

### Core Result Relevant to Stage A
**Proposition 1 (late-commit impossibility)**: No verification-only policy can achieve exactly-once under late commits without a known bound on in-flight time. For a non-idempotent write that times out, and two observation-equivalent worlds (absent vs. late), any recovery policy that completes the absent world by re-issuing the write will also re-issue it in the late world if the delay exceeds the policy’s completion time plus the read-path visibility lag, leading to a duplicate with probability one.

**Observation equivalence** (Definition 1): Two outcome states are observation-equivalent for a response if the response probability and all pre-commit reads are identical. A timeout plus empty/lagging read can occur in both the absent and late worlds until the in-flight request commits.

**Empirical motivation** (model-based; not a deterministic reproduction target). The manuscript reports:  
- Frontier models instructed to act exactly once: ~0.5% duplicates on lost-acknowledgement faults (read-back can resolve).  
- Same models: ~56% duplicates on late-commit faults and ~74% on redelivery.  
- In the authors’ exploratory attribution analysis for faults not resolved by immediate read-back, contract accounted for 81% of the explained component, using their specified pseudo-R² (McFadden) / Shapley decomposition. The analysis concerns the studied factors and fault strata; the manuscript labels the stratified decomposition exploratory.  
- Offering a stable idempotency key on every write reduces overall duplicates from 28% to 4% (agents attach keys in 98% of episodes when available).  
- Agents reported success in 90% of episodes in which they had duplicated an effect.

These reported findings motivate the importance of the late-commit case and the value of contract-level mechanisms. They are not operational reproduction targets for the deterministic Stage A defined in PR-1, nor independently confirmed facts.

### Contract Variants in Limbo
Limbo distinguishes a native contract (optional keys, eventually consistent or missing read paths) from a “keys-everywhere” contract. Stage A of Council Lab mirrors this separation with C0 (no replay protection) and C1 (enforced stable-key semantics). Implementation transfer is measured within each stratum.

### What Limbo Does Not Establish
- Independent replication by a separate team under the same explicit, frozen external specification.  
- Transfer of the reported intervention benefits when the service implementation, scheduling mechanism, and effect ledger are independently authored.  
- Behavior under independently implemented asynchronous execution, durable operation state, and acknowledgment loss across actual execution boundaries, rather than simulator-controlled scheduling and effects. (Limbo runs its sandbox as a local HTTP service with an MCP adapter; HTTP transport itself is not the differentiator. Scheduling and service effects remain simulated.)  
- A general claim that any contract-aware controller will transfer; the paper focuses on where exactly-once should be enforced (model vs. harness vs. tool contract).

A violation of the stated assumptions does not refute the published result; it may instead demonstrate nonconformance, specification incompleteness, or limited applicability. Independent implementation alone establishes neither novelty nor production validity.

## Secondary References (boundary only)
**UndoBench**: Dolly Sah, Tanmay Sah, Harshul Jain, Tanya Sah, *UndoBench: Separating Task Competence from Recovery Capability in Tool-Using AI Agents*, arXiv:2610.05622, October 2026 (preprint). Separates nominal task competence from recovery capability via paired faulted/unfaulted trials and effect-history oracles. Relevant for competence-recovery gaps and phase-dependent recovery, but not the primary late-commit transfer target for Stage A.

**RetryBench**: You Liu, Yue Liu, Quanchao Lu, *RetryBench: Separating Retry Permission from Recovery Outcomes in GPT Tool Use*, arXiv:2610.15884, October 2026 (preprint). Separates whether a retry is justified by visible evidence from whether it produces a favorable outcome, using observation-compatible hidden worlds. Closely related to evidence-justified recovery decisions, but Stage A focuses on implementation transfer of deterministic controllers under fixed contracts rather than model retry permission.

**Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures**: Isham Kalappurackal Mansoor, Abhishek Phadke, Pratip Rana, arXiv:2608.02645, 2026 (preprint). Shows that a verify-before-retry wrapper plus replay protections can reduce duplicates under non-atomic failures. Stage A treats verify-before-retry as a negative control on C0 and tests whether the benefit of stable keys transfers under independent implementation.

Limbo itself identifies additional close predecessors, including *Did It Happen? Counterfactual Evaluation of LLM Agent Recovery from Ambiguous Tool Outcomes* (Sun, 2026) and IdempotencyBench (Gopnal Swamy, 2026). Their overlap should be checked before approving a novelty claim.

## Boundary Statement
Stage A tests whether the late-commit limitation and the benefit of enforced stable-key semantics (as characterized by Limbo) survive independent service implementation under a frozen external contract. A result that only reproduces the known impossibility of verification-only exactly-once under late commits, or the known benefit of stable keys when the service enforces them, is a replication. A contribution requires a consequential, audited interaction or transfer failure not already characterized by the relevant prior literature, including classical distributed-systems results and the closest agent-recovery studies.

## Evidence of Satisfaction
This document, reviewed alongside PR-1, allows an independent reviewer to determine whether a future Stage A result is a replication of Limbo’s late-commit characterization or a potential extension. Artifact status is recorded so that claims of exact reproduction are not made without an available original artifact.
