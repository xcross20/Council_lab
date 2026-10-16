# Council Lab — Research Mission v2 (proposed)

## Problem
Long-running autonomous software engineering agents encounter incomplete, conflicting, stale, or misleading evidence. Their recovery policy may prematurely retry, falsely accept completion, lose the correct state, or escalate unnecessarily.

## Research question
When does selectively invoked, epistemically diverse expert deliberation improve the selection of authorized evidence-gathering and recovery actions under ambiguous failures, compared with standard deterministic policies and budget-matched single-agent diagnosis?

## Falsifiable hypothesis
Adaptive deliberation may improve correct safe disposition on **ambiguous, multi-causal** incidents at an acceptable incremental cost. On ordinary faults, deterministic policies may be preferable. The experiment must permit a null or negative result.

## Scope
An open, replayable fault-injection laboratory; simulated implementation -> test -> review -> integration workflow; controlled fault scenarios; independent evaluator; original 27 VentureOS V3 prompts as immutable candidate treatment assets.

## Non-goals
A new coding model, a production runtime, universal organization spawning, live brokerage/trading, an autonomous deployment system, or publishing research claims before robust evaluation.

## Primary outcome
Correct safe disposition: valid recover/verify/stop after honoring constraints. Report hard safety violations independently, not hidden inside a single aggregate score.

## External-validity limits
Synthetic environment validity must be audited. Transfer requires real bounded Grok/other-agent workloads and held-out incident families. No conclusion on production reliability from the six dev fixtures.
