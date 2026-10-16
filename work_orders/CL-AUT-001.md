# CL-AUT-001 — One Bounded Grok Engineering Cycle

Status: PROPOSED — first implementation order. Depends on accepted CL-REL-001 baseline and tests.

## Objective
Implement a single `council cycle` that invokes Grok CLI in an isolated worktree, collects objective verification and records a controller-owned decision.

## Tasks
- Define explicit work-order parser and validation.
- Add `GrokCLIBuilder` subprocess adapter (no shell=True), configured CLI executable, bounded timeout, cwd and stdout/stderr capture. Include dry-run adapter to test without model credentials.
- Establish clean base Git commit and branch/worktree isolation; do not automatically merge or push.
- Run independent unittest and scenario replay commands.
- Write EVIDENCE.json and DECISION.json, record state transactionally in SQLite. Project .council/STATE.md from SQLite only.
- Expose `council cycle --dry-run`, and `council cycle`. Fail closed if CLI unavailable or authorization not given.

## Acceptance
- Dry-run fixture completes full pipeline with deterministic evidence and machine-readable decision.
- Real Grok builder can be configured without hard-coded secrets; execution cannot escape worktree by default.
- Failed tests / missing evidence cannot result in COMPLETE.
- Worktree/source refs, commands, exit codes, time limits, and artifact hashes are recorded.
- Tests pass in CI; no automatic merge, deploy, push, or research-oracle changes.

## Limits
One builder; one independent verifier; maximum 3 attempts; no auto-generated work orders. Do not implement CL-AUT-002/003 early.
