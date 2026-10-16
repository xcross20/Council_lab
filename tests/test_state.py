import tempfile
import unittest
from pathlib import Path
from council_lab.contracts import Mission, WorkOrder
from council_lab.state import StateStore


class StateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "state.sqlite3"
        self.store = StateStore(self.db)
        self.store.add_mission(Mission("M-1", "Improve app", self.tmp.name, "Tests pass"))

    def tearDown(self):
        self.store.close()
        self.tmp.cleanup()

    def test_invalid_transition(self):
        self.store.add_task(WorkOrder("T-1", "M-1", "Fix UI", ("test",)))
        with self.assertRaises(ValueError):
            self.store.transition("T-1", "VERIFIED", "skip gates")

    def test_review_requires_evidence_reference(self):
        self.store.add_task(WorkOrder("T-1", "M-1", "Fix UI", ("test",)))
        for stage in ("READY", "RUNNING", "REVIEW"):
            self.store.transition("T-1", stage, "workflow")
        with self.assertRaises(ValueError):
            self.store.transition("T-1", "ACCEPTED_LOCAL", "looks fine")
        self.store.transition("T-1", "ACCEPTED_LOCAL", "independent review", "artifact:review-1")

    def test_unintegrated_dependency_blocks_execution(self):
        self.store.add_task(WorkOrder("T-1", "M-1", "Base", ("test",)))
        self.store.add_task(WorkOrder("T-2", "M-1", "Dependent", ("test",), ("T-1",)))
        self.store.transition("T-2", "READY", "ready")
        with self.assertRaises(ValueError):
            self.store.transition("T-2", "RUNNING", "go")

    def test_persists_history_on_restart(self):
        self.store.add_task(WorkOrder("T-1", "M-1", "Fix", ("test",)))
        self.store.transition("T-1", "READY", "prepared")
        self.store.close()
        self.store = StateStore(self.db)
        self.assertEqual(self.store.status()["tasks"][0]["status"], "READY")
        self.assertEqual(len(self.store.history("T-1")), 2)

    def test_rejects_bad_authority(self):
        with self.assertRaises(ValueError):
            WorkOrder("T-1", "M-1", "Deploy", ("test",), authority="PRODUCTION")


if __name__ == "__main__":
    unittest.main()
