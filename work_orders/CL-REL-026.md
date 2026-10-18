# CL-REL-026 — Private evaluation set design

Status: PROPOSED (not authorized for automatic execution)
Dependencies: CL-REL-025
Authority gate: human scientific approval

## Hypothesis / objective
Prepare causally varied external-to-repo scenarios isolated from Builder/treatment workspaces.

## Minimum work
Inspect existing results, exact Git SHAs and frozen protocols. Predeclare comparison, metrics, budgets and stop criteria before any experiment. Reuse existing deterministic simulator, scorer, standard Grok CLI and independent Reviewer. Preserve all prior evidence. Implement or execute only the smallest useful slice. Validate against actual outputs and independently QA. Repair only in approved scope and report all invalid and incomplete attempts.

## Acceptance
Independent custody, leakage audit and frozen design.
The record must include exact SHA, procedure, trace, oracle provenance, latency, model usage if available, unknown costs marked unknown, limitations and independent QA decision. Never promote favorable development results to held-out evidence.

## Boundaries
Do not change hidden truth, scoring rules or research protocol without separately approved frozen revision. No new orchestration, production deployment, automatic publication, paid run without budget, or promotion of protected Git branches. Status remains PROPOSED until explicitly authorized.
