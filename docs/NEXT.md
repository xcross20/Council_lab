# NEXT — Autonomous Engineering Work-Loop Preparation

**Current stage:** prepare only, do not claim autonomous work loop is implemented.

**Scientific baseline:** CL-REL-001 fault simulator and six development fixtures on `feat/cl-rel-001-fault-simulator`. The scientific simulator, oracle, and original council assets remain separately versioned.

**Engineering implementation queue**
1. [CL-AUT-001](../work_orders/CL-AUT-001.md): one bounded Grok build → tests → controller decision cycle.
2. [CL-AUT-002](../work_orders/CL-AUT-002.md): durable restart, reconciliation, leases and projected STATE.md.
3. [CL-AUT-003](../work_orders/CL-AUT-003.md): max-cycles loop over approved task dependency chain.

**Proposed operator UX:** `council cycle --dry-run`, then `council cycle`, then `council run --max-cycles 5`. These commands do NOT exist until the relevant work orders are accepted.

**Next action:** verify CL-REL-001 tests/CI and inspect its evaluator; then authorize CL-AUT-001 with a bounded Grok CLI configuration. Do not start autonomous execution without approval.
