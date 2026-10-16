# CL-AUT-006 — Autonomous Review, Repair, Acceptance and Advancement

Status: PROPOSED. Implementation must not bypass unresolved CL-AUT-004/005 verification and sandbox gates.

## Mission
Demonstrate one instruction -> Grok Builder -> separate independent Grok Reviewer + deterministic verifier -> bounded autonomous repair when necessary -> controller-owned local acceptance -> next approved work order, **without manual human handoffs**.

## Work
1. Build a Reviewer adapter that launches a fresh Grok CLI session with exact work order, diff, independent test evidence and scoped repository access. Normalize output as structured findings; no self-certification.
2. Extend the deterministic Controller with ACCEPT / REPAIR / BLOCKED / SAFETY_STOP over frozen criteria, artifact checks and independent reviewer findings.
3. On REPAIR, synthesize minimal repair instructions from verified findings; retain original task scope, exact branch/commit lineage and finite attempt budget; automatically rerun Builder.
4. After each repair, rerun objective checks and a *fresh* independent review. Persist all attempts and decision provenance.
5. On ACCEPT, persist verified local acceptance and advance to the next already-approved READY order with satisfied dependencies. Never auto-push, auto-merge, deploy, or alter research scoring.
6. Run the first end-to-end demonstration with trusted Builder/Reviewer test doubles. Only run a real Grok subprocess after separately verified OS sandbox restrictions and authorized live testing.

## Acceptance tests
- A deliberate repairable defect causes initial nonacceptance, unattended repair, fresh review, and local ACCEPT with evidence hashes bound to current task/run/attempt/commit.
- The next eligible approved order begins without manual prompts or handoffs.
- Reviewer and Builder disagreement cannot bypass deterministic validation.
- Over-budget repair chain returns BLOCKED; protected-file/state/evidence corruption returns SAFETY_STOP and never retries compromised runner.
- Crash/restart does not duplicate accepted work or reuse successful evidence across runs.
- No changes to original 27 council prompts, scientific oracle, hidden scoring, or protected branches.
- Complete sanitized run report with attempts, outcomes, reviewer findings, hashes, time and known/unknown cost.
- All historical adversarial regression tests continue passing.

## Explicit exclusions
No generalized agent organization, UI, dynamic council compiler, production deployment or silent weakening of test/verification gates.

## Dependencies
CL-AUT-001 through CL-AUT-005 must have independently validated acceptance, and actual live Grok sandbox checks precede any unattended external-model execution.
