# CL-AUT-002 — Durable State, Recovery and Resume

Status: BLOCKED — requires CL-AUT-001 acceptance.

## Objective
Resume interrupted engineering cycles without losing truth, duplicating side effects, or falsely accepting progress.

## Tasks
- SQLite run/cycle/attempt/lease records and append-only events.
- Generate STATE.md projection; ensure generated state agrees with SQLite.
- Reconcile worktree HEAD, commits, output artifacts, and test results after crash before ever re-invoking Grok.
- Cover timeout before execution, lost builder acknowledgement after commit, interrupted tests, and lost persistence acknowledgements.
- Enforce bounded retries and redaction.

## Acceptance
Fault-inject termination at four checkpoints. All recovered cases preserve state, avoid duplicate semantic execution, and do not report false COMPLETE. Ambiguous outcomes BLOCK pending independent verification. Every transition is audited. Tests pass.
