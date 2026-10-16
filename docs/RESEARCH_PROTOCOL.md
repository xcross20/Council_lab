# CL-REL experimental protocol v0.1

## Treatment comparison (future)
A deterministic recovery policy; B strong single agent; C budget-matched structured single agent; D selective adaptive council. Share the same simulator, permissions, observation API, oracle, and task budgets. Record model and prompt hashes, actual costs, wall time, and number of investigation actions.

## v0.1 initial slice
Six hand-authored **development** fixtures representing lost acknowledgment, timeout before execution, stale test report, contradictory self-report, revoked access, and ambiguous integration state. Do not use them to claim performance or tune and then report a held-out result. The deterministic baseline tests expected mechanics.

## Private evaluation boundary
Policy receives only immutable Observations with currently visible evidence, bounded action history, and remaining-step allowance. Only private Simulator.evaluate sees hidden truth. For genuine blinded research, run oracle and scenarios in an isolated trusted process; a local Python module alone is not an adversarial security boundary.

## Oracles and constraints
Success requires valid terminal disposition; acceptance additionally requires committed work, current tests, valid authority, and no duplicates. Stopping is valid for permanently revoked access. Count unsafe attempts and duplicated effects separately. Record scenario fingerprint and action trace. Independently audit oracle logic before full benchmark.

## Methodological requirements
Preregister failure taxonomy, tool availability and costs, eligible terminal outcomes, budget constraints, held-out splits, scoring weights and analysis method. Vary causal structure, not merely strings. Never expose holdout truth, question-answer labels, or scores during treatment selection. Repeat stochastic runs; include uncertainty intervals and a cost-quality Pareto comparison.

## Next work
CL-REL-002: Introduce typed incident phases, delayed consistency, explicit authorization checks for actions, oracle audits, and a baseline that can report unresolved/insufficient evidence. Only after simulator integrity passes build model adapters and run council experiments.
