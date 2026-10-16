# CL-AUT-003 — Controlled Multi-Cycle Execution

Status: BLOCKED — requires CL-AUT-002 acceptance.

## Objective
Run sequential approved work orders without manually copying prompts between Grok sessions.

## Tasks
- Add `council run --max-cycles N`, dependency-based ready task selection and limited budgets.
- Continue only after evidence-backed acceptance. Respect max cycles/attempts/wall time; log unavailable token costs as unknown.
- Record run report, per-attempt artifacts and next work order.
- Never edit scientific oracle or held-out protocol to achieve better score.

## Acceptance
Two approved fixture orders execute in sequence, a blocked third correctly stops the run, budget-exhaustion stops safely, restart doesn't reexecute accepted work. No automatic push/merge/deploy.
