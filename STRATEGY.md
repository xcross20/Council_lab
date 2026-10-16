# STRATEGY — Council Lab product and autonomous engineering

## First principle
**The application is the product. The autonomous engineering system is the operating model.**

The product is a reproducible research lab for evidence-grounded recovery decisions in long-running AI engineering workflows. The operating model must be a minimal, unattended engineering loop that builds and improves that product.

## Objective
One approved mission -> bounded work order -> independent Grok Builder -> independent Grok Reviewer and deterministic tests -> controller decision -> automatic bounded repair if needed -> accepted local work -> next approved order.

Humans set mission, budgets, material risk boundaries, scientific protocol and external release authority; humans do NOT coordinate routine builder/reviewer/QA handoffs.

## Implementation principles
1. Reuse tested Rally / existing Council Lab code before introducing another orchestration subsystem.
2. One Python deterministic Controller, one Grok CLI Builder, one independent Grok CLI Reviewer. Optional Grok Planner prepares proposals; it cannot grant authority.
3. Scope all tasks with frozen testable acceptance criteria, exact base SHA, allowed paths, attempt/time/cost budget, and dependencies.
4. Builder and Reviewer get separate fresh contexts. Reviewer receives exact diff, tests, original requirements, and evidence; never rely on Builder self-report.
5. Keep controller/evaluator outside Builder authority. Treat all Builder output as untrusted. A Git worktree is NOT a sandbox: live execution requires independently validated filesystem/process restrictions.
6. Acceptance is a deterministic policy over validated, content-addressed evidence bound to task, run, attempt, verifier result and exact commit. No symbolic evidence-only promotions, status text self-certification or copied evidence.
7. Automatic repair is allowed only within approved scope/limits; rerun independent verification after each repair.
8. Auto-advance only after evidence-backed local acceptance. Do not auto-merge protected branches, deploy, trade or access unrelated secrets.
9. Keep SQLite authoritative for execution state; Git for source; evidence artifacts for verification; generated STATE.md for readability.
10. Never modify scientific ground truth, hidden holdouts or scoring criteria in response to treatment performance. Require explicit scientific protocol review.
11. Prefer small modules, clear interfaces, realistic negative tests, CI, and reproducible builds. Prevent unsupported complexity and architectural drift.
12. Measure verified acceptance rate, cycles, repair attempts, reviewer false positives, elapsed time, cost, unsafe interventions and escape/rollback incidents.

## Thin vertical slice
With one initially approved task containing an intentionally repairable defect, prove uninterrupted **Builder -> independent Reviewer -> deterministic verifier -> automatic bounded repair -> re-review -> local acceptance -> next READY approved task**. Record complete trace and confirm zero human handoffs. Separately demonstrate BLOCKED on exhausted retries and SAFETY_STOP on trust-boundary violation.

Do not delay the basic loop to construct a multi-agent organization, user interface, distributed scheduler, or generalized council compiler.

## Critical security prerequisite
CL-AUT-004/005 remediation reports are local and not accepted. Evidence integrity, controller authority, trusted verifier, CI provenance and actual live Grok sandbox enforcement are mandatory before unrestricted live autonomy. In the meantime use trusted test doubles to prove the orchestration.

## Progression
1. Validate trust boundary and evidence integrity.
2. Complete CL-AUT-006 review-repair-accept and next-order orchestration using test doubles.
3. Test real Grok sandbox restrictions and execute one authorized end-to-end pilot.
4. Enable unattended continuation over approved bounded roadmap, with budgets and stop rules.
5. Add adaptive council research treatments only after independent evaluation harness is credible.
