# Council Lab Roadmap — Fault-Aware Recovery Research

Status: research pivot proposed on feat/cl-rel-001-fault-simulator. Base: CL-001 mission/state foundation, 27 original prompts; no changes to immutable originals.

| Order | Deliverable | Acceptance / STOP gate |
| --- | --- | --- |
| CL-REL-001 | Research mission, replayable scenarios, deterministic simulator/evaluator and baseline | Unit tests pass; hidden truth not in policy observation; unsafe outcomes caught; repeatable traces |
| CL-REL-002 | Oracle hardening and fault-model breadth | Independent oracle audit; six fault classes vary in causal structure; no test/validation leakage; strict action authorization |
| CL-REL-003 | Interchangeable model-policy adapter and structured reasoning | Matched budgets, normalized decisions, provider identity and costs; no privileged truth |
| CL-REL-004 | Original council prompt registry and selective composition | Hash/version provenance; Composition Critic PASS/REVISE/BLOCK enforced; independent Round 1 and dissent retained |
| CL-REL-005 | Pilot comparison and ablations | At least 30–50 generated/reviewed scenarios; repeated trials; transparent failures and null results |
| CL-REL-006 | Held-out benchmark and external replication | Prespecified metrics and analysis; held-out incident families; clean-room reproducibility |
| CL-REL-007 | Real engineering workflow transfer | Bounded Grok integration, verified task state and evidence; compare simulation versus real outcomes |

No scope expansion without accepted evidence. No production calls or commits to main by agents. Retain CL-001 as separately reviewed foundation.
