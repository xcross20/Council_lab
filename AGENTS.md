# Council Lab Agent Operating Contract

Read MISSION.md, docs/AUTONOMOUS_LOOP.md, docs/RESEARCH_PROTOCOL.md and docs/NEXT.md before implementing any task.

- **Controller = deterministic Python authority**. Grok CLI is a builder (and optionally a reviewer/planner); its self-report is never acceptance.
- Loop A (engineering) builds the system. Loop B (research) measures recovery. Do not confound them.
- Execute only human-approved, bounded work orders with frozen acceptance criteria.
- Git owns code truth; SQLite owns runtime state; evidence artifacts own validation; STATE.md is generated from SQLite.
- Original 27 VentureOS prompts are immutable. No hidden oracle access by trial agents.
- Always test and retain failures. Unknown / contradictory evidence must BLOCK or trigger authorized investigation.
- Never push, merge, deploy, purchase services or alter production resources automatically.
- No shell=True, no unbounded retries, no logging secrets, and no tools outside assigned worktree without explicit authorization.
- Capture provenance (commit SHA, adapter/config, tool commands, scenario hashes, artifacts, decisions).
- Keep the first release tiny: one Grok worker, one independent deterministic verifier, one controller.
