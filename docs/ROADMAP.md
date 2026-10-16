# Council Lab Roadmap

## Product
Research selective, epistemically diverse deliberation for evidence-grounded agent failure investigation and safe recovery. Initial simulator: CL-REL-001. Subsequent research: CL-REL-002 oracle hardening; CL-REL-003 model treatments; CL-REL-004 adaptive council; CL-REL-005 controlled pilot; CL-REL-006 held-out replication; CL-REL-007 real-world transfer.

## Operating-model critical path
- CL-AUT-001–003: one bounded cycle, recovery/resume, multi-cycle execution (locally reported implemented; not automatically accepted).
- CL-AUT-004–005: security, controller authority, evidence binding and redaction (locally reported remediation; independent QA/CI/sandbox gate unresolved).
- **CL-AUT-006:** independent Grok Reviewer -> deterministic gate -> unattended bounded Builder repair -> fresh verification -> local acceptance -> next approved work order.
- CL-AUT-007 (only if needed): evidence-triggered RETHINK invocation and low-cost engineering telemetry; do not implement before observing need.

## Required demo
One approved instruction -> Builder -> independent Reviewer and trusted tests -> repair -> independent acceptance -> next approved order, with zero intermediate operator handoffs. Also verify exhaustion BLOCKED and trust-boundary SAFETY_STOP.

## Standards
Reviewable modular code; durable SQLite state; fresh independent sessions; protected verifier; artifact provenance; isolated worktrees AND validated sandbox; bounded retries; reproducible tests; exact SHA and CI evidence. No automatic protected merges or deployment.

## Research separation
Engineering improvement loop must not manipulate benchmark truth, holdout fixtures or scoring to optimize performance. Scientific protocol changes are reviewed and versioned outside active treatment runs.
