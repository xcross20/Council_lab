# CL-REL-028 — Held-out deterministic and single-agent runs

Status: PROPOSED (not authorized for automatic execution)
Dependencies: CL-REL-025, CL-REL-026, CL-REL-027
Authority gate: paid model and held-out approval

## Hypothesis / objective
Run frozen baseline, simple and strong structured single-agent protocols.

## Minimum work
Inspect existing results, exact Git SHAs and frozen protocols. Predeclare comparison, metrics, budgets and stop criteria before any experiment. Reuse existing deterministic simulator, scorer, standard Grok CLI and independent Reviewer. Preserve all prior evidence. Implement or execute only the smallest useful slice. Validate against actual outputs and independently QA. Repair only in approved scope and report all invalid and incomplete attempts.

## Acceptance
Paired scored results including invalid/cancelled runs.
The record must include exact SHA, procedure, trace, oracle provenance, latency, model usage if available, unknown costs marked unknown, limitations and independent QA decision. Never promote favorable development results to held-out evidence.

## Boundaries
Do not change hidden truth, scoring rules or research protocol without separately approved frozen revision. No new orchestration, production deployment, automatic publication, paid run without budget, or promotion of protected Git branches. Status remains PROPOSED until explicitly authorized.
