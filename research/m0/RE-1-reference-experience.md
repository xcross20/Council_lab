# RE-1 — Reference Experience

**ID**: RE-1  
**Milestone**: M0 — Research Product Definition  
**Status**: Draft for independent review  
**Date**: 2026-10-21  
**Depends on**: PR-1, PR-2

## Purpose

Provide a complete, inspectable example of the researcher journey for Stage A (implementation transfer) so that a third party can walk through a realistic experiment without implementation and determine what evidence must be produced.

The reference experience is not a dashboard or multi-screen application. It is the sequence of reviews, executions, inspections, and classifications a researcher performs.

## Researcher Journey

1. **Review the research contract**  
   Researcher confirms the frozen hypothesis, C0/C1 strata, the specific policy under test, numerical times (decision 15 s, task deadline 60 s, settlement horizon 180–300 s), per-policy requirements, and evaluation rules from PR-1.

2. **Examine two service implementations**  
   Reference implementation A and independently authored implementation B expose the same declared external contract. Their internal execution mechanisms differ. Conformance is checked separately from controller behavior.

3. **Execute matched fault scenarios**  
   The researcher runs the same unchanged recovery policy in both environments under prespecified fault conditions (absent world and late-commit world). Within each implementation, controller-visible histories are matched through the decision point.

4. **Inspect the evidence**  
   View controller-visible observations alongside the evaluator’s separately protected effect history. Every decision and side effect has an auditable provenance record. Settlement occurs (or is labeled indeterminate) before final grading.

5. **Compare and classify**  
   Determine whether each implementation met the prespecified safety and deadline-completion requirements.  
   - Conformance failure (service violates frozen contract) is distinguished from controller requirement violation.  
   - Expected known failures (e.g., verification-only retry producing a duplicate on C0 late world) are recorded as successful negative-control demonstrations.  
   - Unexpected discrepancies enter the bounded audit. Classification does not convert a failed transfer hypothesis into a pass.

6. **Produce a defensible conclusion**  
   Export the run records, contract version, implementation identity, scoring evidence, audit findings (if any), and continuation recommendation. Pure replication of the known late-commit limitation does not establish novelty.

## Design Corrections Incorporated

**A. Contract conformance is visibly separate from controller performance.**  
If implementation B fails the external-contract conformance suite, the researcher sees a conformance failure. This does not automatically mean the controller failed to transfer. Results from a non-conforming implementation are not used for the transfer assessment.

**B. Expected known failures are distinguished from unexpected transfer failures.**  
A verification-only controller producing a duplicate under the C0 late-commit condition is apparatus-validity evidence (negative control), not a transfer failure and not evidence of novelty. An unexpected requirement violation in the independent implementation fails the transfer hypothesis for that stratum and enters the bounded audit.

## Illustrative Expected Outcomes (Demonstration Only)

These are expected demonstration outcomes consistent with PR-1, not experimental findings.

| Case | Reference A | Independent B |
|------|-------------|---------------|
| C0 verification-only retry, late commit | Duplicate side effect (known control) | Duplicate side effect (known control) |
| C0 conservative no-key controller, late commit | No duplicate; unresolved | No duplicate; unresolved |
| C1 stable-key controller, late commit | No duplicate; completion by 60 s if liveness holds | No duplicate; completion by 60 s if liveness holds |

Cross-implementation timing differences permitted by the contract are recorded rather than automatically classified as defects.

## Illustrative Trace: C0 Verification-Only Policy, Late-Commit World

1. Initial request submitted (Operation O-101, non-idempotent write). Acknowledgment unavailable.
2. Controller observes timeout. Execution outcome unknown; original request may still be pending.
3. Status read returns empty. Observation is compatible with both absent and late-commit worlds.
4. Controller retries without replay protection (Operation O-102) within the 15 s decision window.
5. Evaluator settles outstanding operations through the settlement horizon. Both operations commit.
6. Final classification: known duplicate-effect failure reproduced (negative control passes). Safety outcome is not scored as safe completed recovery.

The researcher can reconstruct that the policy’s retry decision was unsupported by its available observations.

## Evidence of Satisfaction

An independent reviewer can follow the complete researcher journey from this document and the related PR-1 / PR-2 artifacts, and can determine whether a future experimental result meets the criteria without relying on implementation details.
