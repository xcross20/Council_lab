# Council Lab

Research-grade expert deliberation with a minimal, evidence-governed engineering harness.

**Current capability:** a runnable Python CLI for missions, work orders, dependency-aware state transitions, and an append-only local audit log. **Not yet implemented:** Grok execution, autonomous councils, browser verification, agent selection, independent evidence validation, and publication-grade benchmarks.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
council init --repo .
council mission "Improve onboarding" --success "Browser journey passes"
council status
python -m unittest discover -s tests -v
```

To register a task: `council task M-<id> "Implement a narrow fix" --acceptance "Test passes"`. Use `council transition T-<id> READY --reason "Scoped"` for explicit controlled transitions.

The 27 authentic VentureOS V3 council prompts are preserved unchanged under [prompts/original-v3](prompts/original-v3/README.md). They are **not** enabled by the CLI.

See [architecture](docs/ARCHITECTURE.md), [CL-001 acceptance and scope](docs/NEXT.md), and [contributor/agent contracts](AGENTS.md). Source-level code is authoritative in Git; local execution state is SQLite in `.council/`; evidence must be checked before later promotion stages.

## Scope and research

Primary research: under what conditions does epistemically diverse expert deliberation improve downstream independently verified software changes relative to budget-matched single-agent and fixed-council baselines? Keep experimental treatments separate from the execution harness and record negative results.

## Safety

No live model/provider calls, releases, paid requests, production mutations, or autonomous merges in this foundation. Local-only authority.
