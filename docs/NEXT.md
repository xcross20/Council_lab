# CL-001 — Mission and State Foundation

**Implemented:** Python packaging, basic mission/work-order contracts, CLI, SQLite mission/task/event tables, dependency checks, transition rules, reason and evidence-reference requirements, original 27 prompts in separate immutable directory.

**Must verify before acceptance:** local unit tests; CLI smoke test; prompt byte comparison and SHA-256 manifest; Git branch/PR review.

**Not yet demonstrated:** Grok calls, real reviewer verification, transactional worktree leases, crash-safe executor resume, independent acceptance from evidence contents, adaptive council runtime, reproducible research experiment.

**Next proposed order CL-002:** registry that loads and verifies 27 unchanged originals; a typed mission compiler that produces one bounded work order; test invalid prompt hash, invalid input, non-empty success criterion. No model calls initially.

**CL-003 (later):** one bounded Grok Builder/reviewer flow, worktree isolation, crash recovery, independent evidence verification.

**CL-004 (later):** council conditions and budget-matched evaluation against baselines.

Every later order requires separately reviewed evidence; do not silently implement future phases.
