# Council Lab — Mission

## Product
Build a rigorous, reproducible **autonomous-agent reliability research laboratory**. Study whether selective epistemically diverse deliberation improves evidence-grounded diagnosis, investigation and recovery decisions under ambiguous failures, compared with deterministic, strong single-agent and budget-matched structured-reasoning baselines.

The initial research environment is a controlled software-engineering workflow with fault injection, a private independent oracle, versioned scenarios and replayable evidence. The research product is not an untested claim that councils outperform individual agents.

## Operating model
**The application is the product. The autonomous engineering system is the operating model.**

Build the research lab using an unattended, minimum-viable engineering cycle:
approved mission -> bounded work order -> Grok CLI Builder -> deterministic checks + separate independent Grok CLI Reviewer -> Controller ACCEPT/REPAIR/BLOCK/SAFETY_STOP -> automatic bounded repair or advancement to the next approved order.

A human approves the mission, risk limits, scientific protocol changes, budgets, and releases—not routine engineering handoffs. A failed review triggers bounded autonomous repair, not manual prompt routing.

## Success
1. Demonstrate an end-to-end unattended engineering cycle with a repairable defect, independent re-verification, evidence-backed local acceptance, and automatic next-order advancement.
2. Fail closed on missing/cross-run evidence, controller tampering, uncontrolled filesystem access, exhausted budgets or material uncertainty.
3. Quantify research recovery quality, wrong/duplicate actions, safe abstention, cost and calibration on development and later held-out scenarios.
4. Publish reproducible methods, limitations and negative outcomes. Do not claim production-readiness or scientific efficacy from synthetic development fixtures alone.

## Authority
Python Controller owns state transitions; SQLite owns runtime truth; Git owns implementation truth; independent verified artifacts own acceptance evidence. Grok Planner/Builder/Reviewer may recommend but cannot grant permission or self-accept.

Allowed autonomy within approved boundaries: create isolated branches/worktrees, implement, run tests, review, repair, locally accept and advance. Forbidden without separate authority: push/merge protected branches, deploy, external financial transactions, unrelated secrets, editing hidden holdouts, or weakening acceptance gates.

## Non-goals
A replacement foundation model, universal organization compiler, complex distributed agent management platform, or production trading/health service.

See STRATEGY.md, RETHINK.md, docs/AUTONOMOUS_LOOP.md and docs/RESEARCH_PROTOCOL.md.
