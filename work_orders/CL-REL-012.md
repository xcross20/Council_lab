# CL-REL-012 — Lost acknowledgment intervention

Status: PROPOSED (not automatically authorized)
Program: Council Lab 30-order research mission backlog
Dependencies: CL-REL-005
Authority gate: scientific protocol approval

## Research objective
Vary success-without-ack and false-completion reports; test duplicate-effect control.

## Work
1. Read MISSION.md, STRATEGY.md, RETHINK.md, the frozen protocol and all upstream evidence. Check exact code/fixture SHAs.
2. Design the smallest bounded implementation or experiment; preregister hypothesis, comparator, primary metric, stop rules and permitted data before any model run.
3. Use existing simulator, deterministic scorer, standard Grok CLI, strict sandbox and independent Reviewer. Do not create new orchestration.
4. Preserve read-only historical results. Collect per-run actions, permitted observations, status, latency, costs when known and reproducible evidence.
5. Test, independently review and record Controller decision. Repair only within preapproved scope; block rather than weaken oracle or reveal hidden data.

## Acceptance
Replay shows intended differences in safe action.
Also: zero hidden-oracle exposure; complete invalid/cancelled attempt accounting; exact SHA provenance; public observation parity when comparing policies; independent QA and no unsupported scientific claim.

## Boundaries
No self-approval of paid experiments, held-out disclosure, scoring/protocol modifications, protected merge, external publication or budget increase. Development results are not held-out evidence. Automatic progression allowed only when this order is independently accepted and the next order has satisfied dependencies and separately granted execution authority.
