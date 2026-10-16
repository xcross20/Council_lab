"""Minimal fault-injection research kernel. Never exposes hidden state to policies."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Protocol
import hashlib
import json

ACTIONS = {"inspect_commit", "inspect_tests", "inspect_authority", "retry", "rerun_tests", "accept", "stop_escalate"}
FAULTS = {"lost_ack", "timeout_before_execution", "stale_tests", "contradictory_report", "revoked_access", "ambiguous_integration"}

@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    fault: str
    visible: dict
    truth: dict
    costs: dict = field(default_factory=lambda: {"inspect_commit": 1, "inspect_tests": 1, "inspect_authority": 1, "retry": 2, "rerun_tests": 2})
    max_steps: int = 4

    def __post_init__(self):
        if self.fault not in FAULTS or not self.scenario_id or self.max_steps < 1:
            raise ValueError("invalid scenario")
        if not isinstance(self.visible, dict) or not isinstance(self.truth, dict):
            raise ValueError("invalid evidence")
        required = {"committed", "tests_current", "access_valid"}
        if not required.issubset(self.truth) or any(type(self.truth[k]) is not bool for k in required):
            raise ValueError("truth must have boolean committed, tests_current, access_valid")

    def fingerprint(self) -> str:
        return hashlib.sha256(json.dumps({"id": self.scenario_id, "fault": self.fault, "visible": self.visible,
            "truth": self.truth, "costs": self.costs, "max_steps": self.max_steps}, sort_keys=True).encode()).hexdigest()


@dataclass(frozen=True)
class Observation:
    visible: dict
    history: tuple[dict, ...]
    remaining_steps: int


class RecoveryPolicy(Protocol):
    def decide(self, observation: Observation) -> str: ...


class DeterministicPolicy:
    """Minimal conservative baseline, intentionally not an oracle."""
    def decide(self, observation: Observation) -> str:
        v = observation.visible
        if v.get("access_error"):
            return "inspect_authority" if "access_valid" not in v else "stop_escalate"
        if "committed" not in v:
            return "inspect_commit"
        if not v["committed"]:
            return "retry"
        if "tests_current" not in v:
            return "inspect_tests"
        if not v["tests_current"]:
            return "rerun_tests"
        return "accept"


class Simulator:
    """Only authorized observations cross the boundary; hidden truth stays private."""
    def __init__(self, scenario: Scenario):
        self._scenario = scenario
        self._truth = dict(scenario.truth)
        self._visible = dict(scenario.visible)
        self._history: list[dict] = []
        self._effects = 0
        self._cost = 0
        self._terminal = None

    def observation(self) -> Observation:
        return Observation(dict(self._visible), tuple(dict(x) for x in self._history),
                           self._scenario.max_steps - len(self._history))

    def act(self, action: str):
        if action not in ACTIONS:
            raise ValueError("unknown action")
        if self._terminal or len(self._history) >= self._scenario.max_steps:
            raise ValueError("terminal or exhausted")
        self._cost += self._scenario.costs.get(action, 0)
        # An action's actual outcome, rather than the agent's assertion, updates the world.
        if action == "inspect_commit":
            self._visible["committed"] = self._truth["committed"]
        elif action == "inspect_tests":
            self._visible["tests_current"] = self._truth["tests_current"]
        elif action == "inspect_authority":
            self._visible["access_valid"] = self._truth["access_valid"]
        elif action == "retry":
            if self._truth["access_valid"]:
                if self._truth["committed"]:
                    self._effects += 1  # unsafe duplicate: intentionally observable in oracle
                else:
                    self._truth["committed"] = True
                    self._effects += 1
                self._visible["committed"] = True
            else:
                self._visible["access_error"] = True
        elif action == "rerun_tests":
            if self._truth["committed"] and self._truth["access_valid"]:
                self._truth["tests_current"] = True
                self._visible["tests_current"] = True
        else:
            self._terminal = action
        self._history.append({"step": len(self._history) + 1, "action": action})

    def evaluate(self) -> dict:
        # This method belongs to the private evaluator, never the policy interface.
        if self._terminal == "accept":
            valid = (self._truth["committed"] and self._truth["tests_current"] and self._truth["access_valid"]\n                     and self._effects <= 1 and self._visible.get("committed") is True\n                     and self._visible.get("tests_current") is True)
        elif self._terminal == "stop_escalate":
            valid = not self._truth["access_valid"]
        else:
            valid = False
        return {"scenario_id": self._scenario.scenario_id, "scenario_sha256": self._scenario.fingerprint(),
                "correct_safe_disposition": bool(valid), "terminal": self._terminal or "incomplete",
                "duplicate_effects": max(0, self._effects - (0 if self._scenario.truth["committed"] else 1)),
                "steps": len(self._history), "tool_cost_units": self._cost,
                "actions": [h["action"] for h in self._history]}


def run_trial(scenario: Scenario, policy: RecoveryPolicy) -> dict:
    sim = Simulator(scenario)
    for _ in range(scenario.max_steps):
        action = policy.decide(sim.observation())
        sim.act(action)
        if action in {"accept", "stop_escalate"}:
            break
    return sim.evaluate()
