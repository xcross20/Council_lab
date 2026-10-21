# Council Lab Research

This directory contains the formal Research Product Definition and acceptance artifacts for the Contract Transfer Lab direction.

## Status

**M0 — Research Product Definition:** In progress. PR-1, PR-2, RE-1, and RE-2 are drafts for independent review. Documentation is not implementation acceptance.

No new Stage A implementation is authorized until M0 has been independently reviewed and approved.

## M0 artifacts

| ID | File | Purpose | Status |
|---|---|---|---|
| PR-1 | [PR-1-research-question.md](m0/PR-1-research-question.md) | Falsifiable transfer hypothesis, C0/C1 strata, fixed policies, deadlines, stop gates | Revised draft |
| PR-2 | [PR-2-related-work-boundary.md](m0/PR-2-related-work-boundary.md) | Limbo prior-art boundary and replication versus novelty | Revised draft |
| RE-1 | [RE-1-reference-experience.md](m0/RE-1-reference-experience.md) | End-to-end researcher journey **and integrated functional, presentation, data-integrity, and scientific acceptance** | Draft |
| RE-2 | [RE-2-expected-traces.md](m0/RE-2-expected-traces.md) | Five illustrative scored traces including known recovery cases, conformance failure and indeterminate settlement | Draft |

## Remaining proposed M0 contracts (not yet committed)

- `AC-1-external-spec-and-authorship.md` — Frozen external specification and independently authored implementation plan
- `AC-2-evaluator-contract.md` — Independent effect-history scoring and settlement
- `AC-3-classification-table.md` — Contract/implementation/controller/evaluator fault classification
- `AC-4-continuation-gate.md` — Controlled audit and continuation decision
- `AC-5-claim-boundary.md` — Deterministic-first research and novelty limits

## Operating sequence

User outcome → reference experience → architecture and data contracts → vertical slices → implementation → independent functional, visual/presentation, and data-integrity acceptance → release evidence → measured user outcome.

**Governing rule:** No code without an approved user journey. No architecture without explicit contracts. No accepted feature without independent evidence. No released result without reproducibility. No claim of success without a measured user outcome.

Reference examples are illustrative only. They are not experimental results. A successful replication is not automatically a novel research finding.
