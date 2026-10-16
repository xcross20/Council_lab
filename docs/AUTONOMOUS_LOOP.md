# Minimal Autonomous Engineering Loop

## Responsibilities
- Deterministic Python controller: task selection, authorization, durable state, attempt budget, worktree leases, decision gates and stopping.
- Grok CLI: implementation builder, optional planning/review intelligence; never the authority for state transitions.
- Independent verifier: deterministic tests, fixture replay, diff/scope checks; independent LLM reviewer may be added, but cannot replace objective tests.

## Cycle
1. Read approved MISSION.md and work_orders/*.md.
2. Read SQLite runtime state and reconcile Git worktree/commit state.
3. Select one approved READY order with satisfied dependencies.
4. Create/reuse isolated worktree, record attempt before invocation.
5. Invoke Grok CLI subprocess with bounded time and explicit working directory.
6. Capture command status and logs, with secrets redacted.
7. Run independently configured tests, fault-scenario evaluations and scope checks.
8. Persist EVIDENCE.json, controller writes DECISION.json.
9. Project .council/STATE.md from authoritative SQLite.
10. STOP on COMPLETE/BLOCKED/SAFETY_STOP, otherwise execute next approved order if within budget.

## Authoritative records
Git commits: code. SQLite: runtime and transition state. EVIDENCE.json: evidence artifacts. MISSION.md/work_orders: human-reviewed task specification. STATE.md: *generated projection*, not competing state truth.

## Decisions
CONTINUE means further approved work remains and gates pass. COMPLETE requires independently checked evidence. BLOCKED means intervention/reconciliation needed. SAFETY_STOP means a violated invariant or unauthorized action. Builder text never grants COMPLETE.

## Proposed paths (not yet implemented)
`.council/state.sqlite3`; `.council/STATE.md`; `.council/runs/<run_id>/EVIDENCE.json`; `.council/runs/<run_id>/DECISION.json`; `.council/runs/<run_id>/builder.log`.

## Research integrity
Loop A builds/reviews research software. Loop B runs the frozen research trials. Loop A must not rewrite Loop B hidden truth, acceptance criteria or holdout scores after seeing treatment results. Version/scientifically review scoring changes.

## Local commands targeted by work orders (not currently available)
`council cycle --dry-run`; `council cycle`; `council run --max-cycles 5`; `council status`; `council results`.
