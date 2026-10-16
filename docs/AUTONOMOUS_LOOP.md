# Autonomous Engineering Operating Contract

## Roles
- **Controller:** deterministic Python, authoritative SQLite state and bounded permission checks; selects READY approved tasks and decides ACCEPT / REPAIR / BLOCK / SAFETY_STOP.
- **Grok Planner (optional):** reads MISSION / STRATEGY / current evidence and recommends bounded NEXT work orders. All proposed orders remain unapproved until they fit previously approved scope and authority, or the human approves a material extension.
- **Grok Builder:** separate CLI session implements a single task or repair in an isolated, sandboxed checkout.
- **Grok Reviewer:** independent fresh CLI session evaluates exact diff and frozen contract, runs/recommends targeted checks and returns structured findings. Cannot access/update controller state, reviewer-policy code, or private research oracle.
- **Verifier:** trusted deterministic tests, scenario replay, diff/scope checks, evidence/hash provenance. Not builder-controlled.

## Loop (target; components may remain unimplemented)
1. Load human-approved MISSION, STRATEGY, budget/authority and immutable work-order contract.
2. Reconcile SQLite, Git, active lease and previous artifacts before selecting a READY task.
3. Record attempt and base SHA. Invoke Builder in isolated environment with secrets minimized.
4. Persist sanitized builder logs, candidate commit and provenance.
5. Run trusted deterministic verifier against candidate with environment isolation; evaluate evidence and policy gates.
6. Invoke separate Grok Reviewer; obtain typed findings with evidence and severity.
7. Controller validates evidence content/hash bound to run/task/attempt/commit, review outcome, safety invariants and budgets.
8. If repairable within scope and limits: create bounded repair instruction and automatically reinvoke Builder; repeat independent tests/review.
9. If accepted: record local acceptance, project STATE.md, advance to next already approved READY order automatically.
10. If material ambiguity, compromised evidence, exceeded budget or new authority required: BLOCK or SAFETY_STOP with complete logs.
11. Trigger RETHINK only on its explicitly listed evidence-based conditions, and treat its recommendation as advisory.

## Authoritative artifacts
- MISSION.md / STRATEGY.md: human-approved goals and governing constraints
- RETHINK.md: triggered advisory protocol
- work_orders/*.md: approved contracts, dependencies and acceptance criteria
- .council/state.sqlite3: controller-owned runtime truth
- .council/STATE.md: generated human-readable projection, never a competing writable truth
- .council/runs/<run_id>/: sanitized logs, EVIDENCE.json (real content-addressed artifacts), DECISION.json (controller-written), RUN_REPORT.json
- Git: content and exact commit hashes, no magic symbolic evidence.

## Fail-closed constraints
No builder output alone can accept an order. A passing test alone cannot override critical reviewer evidence. A reviewer PASS alone cannot override failing deterministic checks. A sandbox violation, state forgery, evidence swap or scientific oracle manipulation is a SAFETY_STOP, not a repair prompt to the same compromised runner. Readonly/worktree naming is not filesystem sandboxing. Do not claim live isolation without a tested OS/container boundary.

## Demonstration
Run with trusted test doubles first: known defect -> Builder -> failing review/test -> bounded repair -> new independent review -> verified local acceptance -> automatically next approved order. Negative tests: retry exhaustion BLOCKED and trust violation SAFETY_STOP. Only then conduct separately authorized sandboxed live Grok pilot.

## Current state
Work orders CL-AUT-001–005 were reported implemented locally; independent acceptance and GitHub CI/live sandbox validation remain unresolved. This contract does not claim these behaviors currently operate on GitHub main.
