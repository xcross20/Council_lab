# Council Lab Agent Contract

Read README.md, docs/ARCHITECTURE.md, docs/NEXT.md before changes.

- Product truth = Git. Execution truth = transactional SQLite. Review/evidence truth = retained artifacts.
- Original V3 prompts are immutable research artifacts; never rewrite them to suit a new runtime.
- The CLI, not an LLM, controls task transitions. Builder may not self-certify acceptance.
- No push to main, live provider, paid data, deployment, trading, secrets, or third-party side effects without scoped approval.
- Work in separate branches/worktrees for parallel changes, and integrate only reviewed artifacts.
- Preserve failures, dissent, unknowns, and BLOCK/STOP decisions.
- Limit modifications to CL-001 scope. Implement no generalized agent platform.
- Test state validity, dependencies, restart behavior and evidence-reference requirements.
