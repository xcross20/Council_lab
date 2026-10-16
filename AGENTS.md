# Council Lab Agent Operating Contract

Read MISSION.md, STRATEGY.md, RETHINK.md, docs/AUTONOMOUS_LOOP.md, docs/RESEARCH_PROTOCOL.md and docs/NEXT.md before implementation.

1. The application is the product; autonomous engineering is the operating model. Human approves mission, budget, risk and releases, not ordinary handoffs.
2. Controller = deterministic Python authority; Grok CLI Planner, Builder and independent Reviewer are advisory execution roles. Builder never self-accepts.
3. After failed independent review, Controller performs bounded repair automatically when authorized; after local acceptance, advances to next approved READY order without asking the operator.
4. Only RETHINK when evidence triggers apply, not every cycle; it never changes scientific scoring, permissions or accepted history.
5. Git owns code truth; SQLite owns runtime truth; real content-addressed evidence owns verification; STATE.md is generated, not independently editable.
6. Separate builder and reviewer sessions; trusted verifier and private scientific oracle must remain inaccessible to untrusted Builder.
7. A worktree is not a security sandbox. No unrestricted live Grok execution until real OS/container isolation is independently validated.
8. Preserve original 27 prompts, research oracle, holdouts and immutable acceptance contracts. Do not weaken tests to gain acceptance.
9. Fail closed on missing/forged/stale evidence, controller tampering, unsafe filesystem access, exhausted budgets and material uncertainty.
10. No unauthorized push, merge, deployment, trading, payment, secrets access or production mutation.
11. Favor smallest useful tested implementation: one Builder, one independent Reviewer, one deterministic Controller. Keep cycle/run/review logs, costs, time and traceability.
