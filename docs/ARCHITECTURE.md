# Council Lab Architecture

## Mission

Build a reproducible autonomous engineering research harness that evaluates whether adaptive epistemically diverse councils improve independently verified software outcomes.

## Modules and their authority

1. Mission interface: user objective + repository + measurable success criteria.
2. Research intelligence: source-backed discipline packets (future, invoked when justified).
3. Council Foundry: immutable original prompts + versioned experimental variants (future).
4. Work planning: typed tasks, dependencies, scope, acceptance criteria.
5. Controller: deterministic transitions, authorization, leases/recovery (only transition rules exist in CL-001).
6. Execution adapters: Grok CLI first (future).
7. Independent review/integration: tests, reviewer, Git/worktrees (future).
8. Evaluation: isolated treatment assignment, same builder, independent scoring (future).

## Current implementation

Single Python package, SQLite local state, CLI. The controller uses SQLite transactions for task state changes and append-only events. Task status is not derived from a model claim. `ACCEPTED_LOCAL`, `INTEGRATED`, and `VERIFIED` require an evidence reference but **v0.1 has not yet verified evidence contents**, so its transitions are not a release security boundary.

## State

PROPOSED -> READY -> RUNNING -> REVIEW -> ACCEPTED_LOCAL -> INTEGRATED -> VERIFIED. BLOCKED is recoverable to READY; SAFETY_STOP is terminal. Invalid moves fail closed. Work may RUN only when dependencies have reached INTEGRATED/VERIFIED.

## Design restrictions

No web UI, distributed queue, microservices, external model execution, or multi-provider framework in CL-001. No claimed scientific improvement without blinded independent evaluation. Original prompts never grant execution permissions.
