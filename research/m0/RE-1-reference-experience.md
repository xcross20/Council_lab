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

## Screen/Artifact-Level Interaction Contract

Stage A requires no browser UI. The researcher's reference experience may be presented as CLI output plus readable Markdown/JSON artifacts. Each journey stage must expose the following inspectable information.

| Journey stage | Required input/view | Researcher action | Observable output and failure state |
|---|---|---|---|
| Review contract | Frozen PR-1/PR-2, contract hash, C0/C1, policy ID, deadlines | Confirm selected fixed stratum and policy | Study manifest; reject mixed contract strata or changed policy |
| Examine services | A/B implementation IDs, conformance evidence, declared guarantees | Inspect conformance independently | PASS/FAIL/NOT_VERIFIED; FAIL excludes that implementation from transfer assessment |
| Run matched worlds | Fault schedule identifier (protected), controller-visible requests/reads | Execute fixed policy for absent/late worlds in A and B | Immutable run IDs and traces; visibility-equivalence check within each implementation |
| Inspect outcomes | Controller log, independent effect ledger, pending requests, settlement record | Drill down from policy result to each dispatch and effect | Counts and timestamps; unresolved pending → INDETERMINATE, never implied safety |
| Classify difference | Contract, requirements, traces, evaluator reconciliation | Apply PR-1 taxonomy and bounded audit | Conformance failure, controller defect, permitted scheduling sensitivity, specification gap, measurement defect, or unresolved |
| Report finding | All run IDs, source/contract revisions, audit decision | Export reproducible study record | Separate apparatus validity, transfer result, novelty/continuation gate; no automatic novelty claim |

### Functional acceptance checks (reference-level; not implementation tests)
- **RE1-F01:** A reader can identify the fixed policy/contract pair and compare A/B without confusing C0→C1 as implementation transfer.
- **RE1-F02:** A reader can follow absent versus late worlds and see equal controller-visible history **within each implementation** through decision, without requiring byte-identical A/B traces.
- **RE1-F03:** A reader can follow all three PR-1 expected policy outcomes and the two failure paths detailed in RE-2.
- **RE1-F04:** A conformance FAIL makes the implementation ineligible for the transfer assessment while retaining a visible audit record.
- **RE1-F05:** A pending operation at settlement cap produces INDETERMINATE, not a safety pass or a clean completion.
- **RE1-F06:** A negative-control duplicate is reported as expected apparatus behavior, not as successful recovery or novelty.

### Data-integrity acceptance checks
- **RE1-D01:** Every decision, observation, dispatch, side effect, and scoring assertion references a unique run/operation/evidence ID and ordered timestamp.
- **RE1-D02:** The evaluator's authoritative effect ledger is separate from the controller-visible event stream; hidden schedules and effects are not supplied to the controller.
- **RE1-D03:** Zero duplicates is established only from the settled ledger; a missing record or pending operation cannot be silently interpreted as zero effects.
- **RE1-D04:** All outcome counts reconcile to ledger entries, including late, duplicate, partial, prohibited, and inconclusive effects.
- **RE1-D05:** Contract version, policy version, implementation identity, deadlines, settlement state, and provenance travel with the exported report.

### Scientific-validity acceptance checks
- **RE1-S01:** Safety, deadline completion, apparatus conformance, transfer assessment, and novelty are distinct decisions.
- **RE1-S02:** Only the implementation and permitted internal scheduling differ within each stratum; documentation, task, scoring, and policy stay frozen.
- **RE1-S03:** Expected control failure is not interpreted as transfer degradation. Nonconforming services are excluded from a valid transfer comparison.
- **RE1-S04:** An unexpected difference is not causally attributed without a controlled reproduction/removal test within PR-1's four-person-hour plus one-reproduction audit budget.
- **RE1-S05:** An unresolved audit remains unresolved and is not promoted to a scientific claim; replication alone does not clear the research-continuation gate.

### Presentation and accessibility acceptance checks
- **RE1-V01:** Tables and trace descriptions have textual status labels (PASS, FAIL, UNRESOLVED, INDETERMINATE), not only color.
- **RE1-V02:** Event timelines consistently identify the clock origin and units; the 15 s decision, 60 s completion, and 180–300 s settlement limits are not conflated.
- **RE1-V03:** A reviewer can find the per-run effect history and its reconciliation from the summary without guessing internal filenames.
- **RE1-V04:** Missing information is explicitly labeled UNKNOWN/NOT_VERIFIED; no fabricated costs, traces, or precise timestamps.

## Independent M0 Reference Acceptance Procedure

A reviewer independent of drafting receives PR-1, PR-2, RE-1, and RE-2. Without seeing future implementation code, they: (1) walk through the six stages; (2) recalculate the worked ledger outcomes in RE-2; (3) apply the conformance and indeterminate paths; (4) classify the known duplicate negative control correctly; (5) confirm that no novelty claim is implied. Record each RE1-* result as PASS/FAIL/BLOCKED with evidence and reviewer identity. **This document remains DRAFT until that separate review is completed.**
