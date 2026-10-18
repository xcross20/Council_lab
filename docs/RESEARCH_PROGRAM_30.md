# Council Lab — 30-Order Autonomous Research Program

**Mission state:** MISSION_IN_PROGRESS. Not research-accepted. Existing CL-REL-003A and CL-REL-003B historical QA passed on development scenarios; CL-REL-003B scored 2/6 correct for interactive Grok vs 1/6 deterministic, but no held-out data, no compute matching and no generalized claim.

## Purpose and success
Evaluate whether selective, epistemically diverse expert deliberation improves evidence-grounded diagnosis and safe action over strong interactive single-agent and deterministic baselines **after controlling for information access, cost, abstention and leakage**. A defensible null result counts as mission progress. Do not search indefinitely for positive findings.

## 30 staged orders
All individual specs live in work_orders/CL-REL-004.md through CL-REL-033.md; they are PROPOSED, not READY, because no new paid experiment budget or modified scientific protocol has been authorized.

| Stage | Orders | Focus | Gate |
|---|---|---|---|
| I: Historical integrity / protocol | 004–007 | QA/replay; freeze sequential parity; budget sensitivity; negative-control escalation | Frozen, QA-reviewed development protocol |
| II: Strong baselines | 008–010 | Plain Grok, structured Grok, deterministic evidence-seeking | Comparable observation/action contracts |
| III: Scenario causality | 011–015 | Contradiction, lost ack, revoked authority, partial execution, ambiguous integration | Independently audited causal scenario variants |
| IV: Comparative analysis | 016–018 | Observation parity, efficiency frontier, adversarial self-check | Quantified quality, unsafe events and cost |
| V: Deliberation | 019–023 | Two-expert pilot, expert selection, trigger threshold, matched-compute control, evidence acquisition ablation | Improvement measured against strongest fair single agent |
| VI: Blinded confirmation | 024–031 | Taxonomy, preregistration, private data, leakage probes, held-out comparative runs, replication, threats-to-validity audit | Scientific independent acceptance |
| VII: Knowledge + discovery | 032–033 | Reproducible synthesis; next hypothesis proposals | Negative and positive findings reported faithfully |

## Execution authorization
The queue is **planned capacity, not blanket permission**. Controller can auto-execute only when status=APPROVED_READY, all dependencies have independent acceptance, relevant protocol is frozen, test data access policy is satisfied, and a specific cumulative budget cap has been provided. No permission to run paid Grok experiments, alter oracle/scorer, create or inspect private held-out truth, change scientific acceptance criteria, push/merge protected branches or publish. Human authorizes each material protocol/release decision, not routine Builder-Reviewer-repair handoffs.

Default exploration policy: prepare specs and no-cost tests; **new paid experiment spend = $0 until explicitly authorized**. Per-run action cap and model budget are inherited from the frozen protocol, never inferred or quietly increased. Hard-stop on exceeded cost/attempt/time limits. Controller still obeys SAFETY_STOP for compromised evaluator or sandbox.

## Autonomous hypothesis generation and replanning
Trigger when: (a) authorized queue drained, (b) 2 independent repetitions of a material failure mode, (c) unresolved incomplete/invalid runs dominate, (d) strong negative/null result, (e) concrete protocol gap or missing control discovered, (f) efficiency significantly regresses.

Within the existing Controller architecture (no new agent platform), a **research planner/advisory Grok pass** may inspect only approved public evidence, failure taxonomy and resource limits, then write 1–3 **candidate** work orders:
- falsifiable hypothesis and disconfirming observation
- public inputs, hidden ground truth separation and data custody
- strongest existing comparator and negative/compute-matched control
- fixed primary + secondary metrics and action budgets
- smallest discriminating test, cost upper bound, dependencies, safety risks
- value of information, expected branch of outcomes
- status PROPOSED, never automatically APPROVED_READY

Independent methodology review checks causal discriminability, power, multiple testing, leakage, design validity and whether this proposal duplicates earlier work. A deterministic controller can auto-queue and auto-execute no-cost diagnostics inside an already approved protocol and budget, but changing outcome definitions, testing on held-out data, or funding a new intervention requires approval.

**No breakthrough hunting / optional stopping:** Never repeatedly evaluate on the same held-out set or pick only positive outcomes. Maintain hypothesis registry; log unsuccessful candidates and selection rationale. Record negative results. Preregister private confirmatory experiments, control false discovery, and reserve fresh data for each new confirmatory hypothesis.

## Definition of done
(1) defensible experimental protocol and independent custody; (2) meaningful controlled comparison with information parity and explicit resource accounting; (3) model/council effects distinguished from extra calls and abstention; (4) at least one independently reviewed confirmatory evaluation, whether positive or negative; (5) reproducible methods, evidence, limitations and safe governance. Not: simply finishing 30 work orders.

## Minimal operating process
1. Reconcile Git/SQLite/evidence state before selecting order.
2. Controller chooses highest-priority eligible APPROVED_READY work order; branches and runs Grok Builder only when source permissions allow.
3. Independent verifier/reviewer evaluates; controller ACCEPT/REPAIR/BLOCK/SAFETY_STOP; retries finite.
4. Following acceptance, choose next eligible authorized order automatically, including multiple queued orders.
5. On triggers, call governed RETHINK/research planner to produce PROPOSED next experiments and tests, then independently review proposals.
6. Only stop for safety, material ambiguity, missing external authority, budget exhaustion, or completed independently verified mission. An empty READY queue means reassess, not claim victory; if remaining work is unauthorized return BLOCKED with requested decision.

## Current known limitations
Original science runs are exploratory development on only six scenarios. CL-REL-003B interactive Grok: 2/6 correct, 0 unsafe accept, 3 incomplete, 1 invalid; deterministic 1/6 correct and 5 unsafe accept. No blinded data, no compute parity, no CI provenance for local work, and unpushed feature branch. This backlog does **not** contain or modify the local CL-REL-003B product implementation and does not assert acceptance of any new experiment.
