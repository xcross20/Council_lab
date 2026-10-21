# RE-2 — Expected Traces and Scored Effect Ledgers

**ID:** RE-2  
**Milestone:** M0 — Research Product Definition  
**Status:** Draft for independent review  
**Date:** 2026-10-21  
**Depends on:** PR-1, PR-2, RE-1

## Scope and notation

All records are **illustrative reference fixtures, not experimental data**. They are deliberately small examples against which the eventual architecture and evaluator should be checked.

- **A** = reference service; **B** = independently implemented service. Both must first pass the *same frozen external contract* conformance suite to be eligible for implementation-transfer assessment.
- **C0** = non-idempotent write with no replay protection; **C1** = stable-key replay protection enforced by the provider.
- **O** = controller-visible observation, **D** = controller decision/dispatch, **E** = evaluator-only authoritative committed effect, **P** = evaluator-only in-flight state, **S** = settlement record.
- Times are illustrative seconds after episode start (t=0). All retries/unresolved decisions follow a timeout observed at t=5 and must occur by t=20 (within the 15-second decision window). The success deadline is t=60. Settlement normally targets t=180 and may extend to t=300 when pending operations remain.
- Different A/B schedules are permitted; only **within each implementation** are absent and late-world observations required to remain indistinguishable through the decision point.
- Scoring uses committed *effect identity*, not response text; later compensation does not erase an effect.

## Trace 1 — C0 verification-only retry: known failure control

**Scenario:** C0 late world, non-idempotent deployment-job creation. Expected *duplicate*; this validates a negative control, **not** recovery success.

| Time | Visibility | Event |
|---|---|---|
| 0 | D | Run A-C0-VR-L: send request q1 without key |
| 5 | O | q1 timed out; execution unknown |
| 7 | O | Status query empty (consistent with absent or late world) |
| 8 | D | Retry q2 without protection |
| 12 | E | q2 commits effect e2, deployment job J2 |
| 25 | E | q1 commits effect e1, deployment job J1 |
| 180 | S | Settled; no pending requests; authoritative effects=[e2,e1] |

**Matched absent twin:** Controller sees the same timeout and empty status up to t=8; q1 is terminally absent, q2 commits e2, ledger has one effect. The controller cannot use the later difference when deciding at t=8.

**Expected A/B:** Both services reproduce the duplicate late-world control when conformant and scheduled as specified. Duplicate count = 1 excess effect; safe completed recovery = **NO**. Negative-control apparatus result = **PASS**. Novelty = **NONE**.

## Trace 2 — C0 conservative no-key controller: safety without completion

| Time | Visibility | Event |
|---|---|---|
| 0 | D | Run A-C0-CN-L: q1 submitted without key |
| 5 | O | Timeout; execution unknown |
| 7 | O | Empty status |
| 8 | D | Report UNRESOLVED; no second write |
| 25 | E | Original q1 commits e1 in late world |
| 180 | S | Settled; one authoritative effect, no pending |

**Expected A/B:** No duplicate in the late world; controller did not falsely claim success. Controller's terminal disposition is **UNRESOLVED**, even though effect later committed. **Safety no-duplicate PASS; successful reported completion NO.** The late commit is disclosed rather than backfilled into a successful controller decision.

**Absent twin:** Same controller-visible history through t=8; original q1 never commits, resulting in zero effects and UNRESOLVED. Neither twin is a completed recovery.

## Trace 3 — C1 stable-key controller: protected retry

**Preconditions:** q1 carries key K from the original submission; q2 retains K and identical parameters; key protection covers concurrency, delay, and full evaluation horizon; eligible processing is feasible by t=60.

| Time | Visibility | Event |
|---|---|---|
| 0 | D | Run A-C1-SK-L: send q1(key=K, params=P) |
| 5 | O | Timeout; execution unknown |
| 7 | O | Empty/lagging status (no proof of absence) |
| 8 | D | Retry q2(key=K, params=P) |
| 12 | E | Provider commits single effect e1 for K |
| 26 | O | Completion confirmed by authoritative permitted interface |
| 180 | S | Settled; effects=[e1], duplicate=0, no pending |

**Expected A/B:** Zero duplicates **PASS**; deadline completion **PASS** (effect and authorized confirmation both by t=60). This is **contract intervention C1**, not evidence that C0 transferred better. The actual service must prove replay protection and matching parameter handling; a self-reported key is insufficient.

**Absent twin:** Same observations through t=8; original q1 is absent but retry q2 with K commits one effect before t=60. Provider-enforced identity yields the same single-effect result.

## Trace 4 — B conformance failure (ineligible for transfer assessment)

**Declared contract:** B advertises C1 provider-enforced replay protection under overlapping delayed requests. Controlled conformance test issues two concurrent submissions with the same K and identical P.

| Time | Visibility | Event |
|---|---|---|
| 0 | D | Conformance test B-C1-CONF: submit q1(K,P) |
| 1 | D | Submit q2(K,P), concurrently |
| 12 | E | B commits e1 |
| 14 | E | B commits e2 (second effect, same K and P) |
| 180 | S | Settled; effects=[e1,e2] |

**Expected classification:** **CONFORMANCE FAIL** (enforced stable-key guarantee violated). Preserve both effects and violation evidence. **B is excluded** from a valid C1 controller-transfer assessment. This is not an automatic controller defect or evidence of a previously unknown transfer failure. It remains a service-contract defect. An A/B transfer comparison must not count this run as a scientific transfer result.

## Trace 5 — Indeterminate settlement (not silently safe)

**Scenario:** C0 conservative controller; original request remains in-flight beyond the maximum settlement cap with no authoritative terminal signal.

| Time | Visibility | Event |
|---|---|---|
| 0 | D | Run A-C0-CN-P: q1 submitted |
| 5 | O | Timeout; execution unknown |
| 7 | O | Empty status |
| 8 | D | UNRESOLVED, no retry |
| 180 | P | q1 still pending; evaluator extends settlement |
| 300 | S | q1 still pending; authoritative final effect unknown |

**Expected classification:** Controller decision=UNRESOLVED; final safety=**INDETERMINATE**; completed recovery=**NO**; duplicate count=**UNKNOWN**, not zero. Pending q1 and cap exhaustion must be recorded. This case must not be classified as a confirmed no-duplicate success or as a completed recovery; it requires an explicit count of indeterminate runs.

## Reconciliation / classification example

| Fixture | Contract | Controller decision | Settled effect count | Safety outcome | Completion by 60s | Scientific role |
|---|---|---|---:|---|---|---|
| 1 C0 VR late | C0 | RETRY | 2 | Duplicate / FAIL recovery | Not safe completed | Expected negative control |
| 2 C0 conservative late | C0 | UNRESOLVED | 1 | No duplicate / PASS for settled trace | NO resolved completion | Safety versus progress |
| 3 C1 stable-key late | C1 | RETRY same K | 1 | No duplicate / PASS | YES | Replay-protection control |
| 4 B C1 conformance | C1 | N/A test | 2 | Conformance FAIL | N/A | Excluded from transfer |
| 5 pending settlement | C0 | UNRESOLVED | UNKNOWN | INDETERMINATE | NO | Censored/pending safety |

Counts above are **within-fixture** outcomes, not study-level frequencies. All authoritative effects are evaluator-only until execution is over; illustrative reports may disclose them to authorized researchers afterward.

## A/B transfer comparison report contract

For each eligible stratum and policy, show A and B **side by side**, including: contract hash, policy hash, implementation ID, conformance status, fault schedule ID, matched-world visibility check, decision latency, outcome deadline, settlement status, committed effects, duplicates, false completion, unresolved operations, score, and evidence pointers. Separate the three gates:

1. **Apparatus validity** — expected controls and oracle/evaluator integrity.
2. **Transfer finding** — unchanged controller meets or violates prespecified requirements within A and B, after conformance eligibility.
3. **Research continuation** — independent prior-art/audit review identifies a consequential unanswered interaction; expected replication does **not** count.

## RE-2 independent review checklist

- [ ] Every example follows PR-1's 15-second *post-timeout* decision bound, 60-second deadline, and 180–300-second settlement rules.
- [ ] C0 and C1 are not treated as the same transfer stratum.
- [ ] Late and absent twins have indistinguishable controller-visible histories through the decision.
- [ ] Event counts reconcile to the final ledger or are explicitly UNKNOWN if unsettled.
- [ ] Conformance failure is excluded from transfer; indeterminate settlement is never labeled safe completed.
- [ ] Expected C0 duplicate is an apparatus-control PASS but a recovery failure.
- [ ] An independently authored implementation is not assumed conformant without its own conformance evidence.
- [ ] A reviewer can reproduce every classification using only the visible examples and PR-1/PR-2.

**Acceptance status:** DRAFT. No runs were executed; an independent reviewer must sign off before architecture is approved.
