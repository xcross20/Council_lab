# Research Proposal and Rethink Contract

This document **operationalizes** RETHINK.md for new research hypotheses. It is a planning policy, NOT a claim that a proposal generator is already wired to the Python Controller.

## Event inputs
Use accepted prior results, immutable method/metric versions, recent failures, explicit missing baselines, review findings, compute and spend accounting. Builder claims alone are not evidence. Never permit planner access to hidden oracle or held-out targets.

## Candidate proposal schema
Each machine-readable proposal should contain: id, parent_evidence_ids, falsifiable_hypothesis, predicted_discriminating_observation, failure_mode, treatment, best_existing_baseline, negative_control, allowed_public_inputs, private_data_custodian, action_budget, time_budget, max_spend, primary_endpoint, secondary_endpoints, preregistration_required, likely_confounds, risk, dependencies, acceptance_evidence, independent_review, status=PROPOSED.

## Decision rules
- Same causal question, cheaper execution? Prefer lowest-cost test.
- Unsuccessful prior result? Propose a diagnosis/control, not optimistic rerun.
- Incomplete Grok traces? Distinguish terminal-action training from bigger budget; predeclare cap comparisons.
- Council advantage appears due to extra calls? Require matched-compute comparator.
- No meaningful uncertainty reduction expected? Mark low priority.
- Planner cannot approve its own candidate, change evaluator, re-run confirmatory holdout, or create privileged tool grants.
- Existing Controller must enforce immutable schema + authorization before promoting any proposal to APPROVED_READY.
- If no safe authorized next step, report BLOCKED with precise budget/scientific decision needed, not MISSION_ACCEPTED.

## Harness improvement
Keep research hypotheses separate from engineering-harness optimization. Track unattended cycle completion, defect escape, independent reviewer disagreement, wall time and spend. Any proposed controller/reviewer/security modification must be independently tested against current harness and must not weaken accepted gates.

## Immediate implementation guard
No new autonomous proposal selector has been implemented by adding these docs. A later **small** approved work order may connect one existing Grok session to the Controller's existing work-order intake, provided it preserves deterministic approval checks. Do not build a separate service, graph, web UI or multi-agent organization.
