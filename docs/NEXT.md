# NEXT — CL-REL-001 Fault-Injection Thin Slice

## Mission
Establish a repeatable small research experiment for evidence-grounded recovery decisions before building model-driven councils or Grok execution.

## This branch adds
- docs/RESEARCH_MISSION.md, docs/RESEARCH_PROTOCOL.md, docs/ROADMAP.md
- Python private-ground-truth simulator and Observation/RecoveryPolicy boundary
- Six development incident fixtures and baseline deterministic recovery policy
- Independent evaluator with correct-safe-disposition and duplicate-effects detection
- Unit tests for baseline handling, unsafe blind retry, unverified acceptance, access revocation, unknown actions, replay identity

## Verification required
Run `python -m unittest discover -s tests -v` in clean checkout; run scenario smoke evaluation. Review oracle assumptions independently before promotion. No research efficacy claims may be made from these fixtures.

## Known limitations
This is a *research kernel*, not a secure sandbox or production agent runtime. Six dev fixtures are not 30–50 varied scenarios; no blind held-out set, no model treatments, no council runtime, no Grok session, no timed execution or real external side effects. Simulator invariants/possible terminal outcomes are provisional and must be strengthened in CL-REL-002.

## Next
CL-REL-002 oracle hardening and typed scenario families; then CL-REL-003 model policy adapter; CL-REL-004 prompt registry. Stop after the verified vertical slice.
