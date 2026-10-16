import json
import unittest
from pathlib import Path

from council_lab.recovery import DeterministicPolicy, Scenario, Simulator, run_trial
from council_lab.scenarios import load_scenarios

FIXTURES = Path(__file__).resolve().parents[1] / "experiments/cl-rel-001/scenarios.dev.json"


class RecoveryTest(unittest.TestCase):
    def test_baseline_all_fixture_dispositions(self):
        results = [run_trial(s, DeterministicPolicy()) for s in load_scenarios(FIXTURES)]
        self.assertEqual(len(results), 6)
        self.assertTrue(all(result["correct_safe_disposition"] for result in results), results)

    def test_hidden_truth_is_not_policy_visible(self):
        s = load_scenarios(FIXTURES)[0]
        sim = Simulator(s)
        observation = sim.observation()
        self.assertNotIn("committed", observation.visible)
        self.assertNotIn("truth", observation.visible)
        sim.act("inspect_commit")
        self.assertTrue(sim.observation().visible["committed"])

    def test_blind_retry_after_lost_ack_is_not_success(self):
        s = load_scenarios(FIXTURES)[0]
        sim = Simulator(s)
        sim.act("retry")
        sim.act("accept")
        result = sim.evaluate()
        self.assertFalse(result["correct_safe_disposition"])
        self.assertGreater(result["duplicate_effects"], 0)

    def test_lucky_guess_without_observation_not_accepted(self):\n        s = load_scenarios(FIXTURES)[0]\n        sim = Simulator(s)\n        sim.act("accept")\n        self.assertFalse(sim.evaluate()["correct_safe_disposition"])\n\n    def test_agent_self_report_never_certifies(self):
        s = load_scenarios(FIXTURES)[4]
        sim = Simulator(s)
        sim.act("accept")
        self.assertFalse(sim.evaluate()["correct_safe_disposition"])

    def test_safe_stop_on_revoked_access(self):
        s = load_scenarios(FIXTURES)[3]
        result = run_trial(s, DeterministicPolicy())
        self.assertTrue(result["correct_safe_disposition"])
        self.assertEqual(result["terminal"], "stop_escalate")

    def test_scenario_replay_fingerprint(self):
        scenarios = load_scenarios(FIXTURES)
        self.assertEqual(scenarios[0].fingerprint(), load_scenarios(FIXTURES)[0].fingerprint())

    def test_unknown_action_fails_closed(self):
        sim = Simulator(load_scenarios(FIXTURES)[0])
        with self.assertRaises(ValueError):
            sim.act("read_hidden_truth")

    def test_duplicate_ids_rejected(self):
        s = json.loads(FIXTURES.read_text())
        s["scenarios"].append(s["scenarios"][0])
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"scenarios.json"
            p.write_text(json.dumps(s))
            with self.assertRaises(ValueError):
                load_scenarios(p)


if __name__ == "__main__":
    unittest.main()
