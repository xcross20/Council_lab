"""Transactional local execution state. No LLM has write authority."""
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from .contracts import Mission, WorkOrder

TRANSITIONS = {
    "PROPOSED": {"READY", "BLOCKED"},
    "READY": {"RUNNING", "BLOCKED"},
    "RUNNING": {"REVIEW", "BLOCKED", "SAFETY_STOP"},
    "REVIEW": {"ACCEPTED_LOCAL", "READY", "BLOCKED"},
    "ACCEPTED_LOCAL": {"INTEGRATED", "BLOCKED"},
    "INTEGRATED": {"VERIFIED", "BLOCKED"},
    "VERIFIED": set(),
    "BLOCKED": {"READY"},
    "SAFETY_STOP": set(),
}


class StateStore:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.execute("PRAGMA foreign_keys=ON")
        self.conn.execute("PRAGMA busy_timeout=5000")
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS missions(
                mission_id TEXT PRIMARY KEY, objective TEXT NOT NULL,
                repository TEXT NOT NULL, success TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS tasks(
                task_id TEXT PRIMARY KEY, mission_id TEXT NOT NULL REFERENCES missions(mission_id),
                objective TEXT NOT NULL, acceptance TEXT NOT NULL,
                dependencies TEXT NOT NULL, authority TEXT NOT NULL, status TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS events(
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id TEXT NOT NULL REFERENCES tasks(task_id),
                old_status TEXT, new_status TEXT NOT NULL,
                reason TEXT NOT NULL, evidence_ref TEXT,
                timestamp TEXT NOT NULL);
        """)

    def close(self):
        self.conn.close()

    def add_mission(self, mission: Mission):
        with self.conn:
            self.conn.execute("INSERT INTO missions VALUES(?,?,?,?)", (mission.mission_id, mission.objective, mission.repository, mission.success))

    def add_task(self, task: WorkOrder):
        if task.task_id in task.dependencies:
            raise ValueError("task cannot depend on itself")
        with self.conn:
            if not self.conn.execute("SELECT 1 FROM missions WHERE mission_id=?", (task.mission_id,)).fetchone():
                raise ValueError("mission not found")
            for dep in task.dependencies:
                row = self.conn.execute("SELECT mission_id FROM tasks WHERE task_id=?", (dep,)).fetchone()
                if not row or row[0] != task.mission_id:
                    raise ValueError(f"dependency unavailable in mission: {dep}")
            self.conn.execute("INSERT INTO tasks VALUES(?,?,?,?,?,?,?)", (task.task_id, task.mission_id, task.objective,
                json.dumps(task.acceptance), json.dumps(task.dependencies), task.authority, "PROPOSED"))
            self._event(task.task_id, None, "PROPOSED", "Work order registered", None)

    def _event(self, task_id, old, new, reason, evidence):
        self.conn.execute("INSERT INTO events(task_id,old_status,new_status,reason,evidence_ref,timestamp) VALUES(?,?,?,?,?,?)",
            (task_id, old, new, reason, evidence, datetime.now(timezone.utc).isoformat()))

    def transition(self, task_id: str, new: str, reason: str, evidence_ref: str | None = None):
        if not reason.strip():
            raise ValueError("transition requires a reason")
        with self.conn:
            row = self.conn.execute("SELECT status,dependencies FROM tasks WHERE task_id=?", (task_id,)).fetchone()
            if row is None:
                raise KeyError(task_id)
            old, dependencies_json = row
            if new not in TRANSITIONS[old]:
                raise ValueError(f"invalid transition: {old} -> {new}")
            if new == "RUNNING":
                for dep in json.loads(dependencies_json):
                    status = self.conn.execute("SELECT status FROM tasks WHERE task_id=?", (dep,)).fetchone()
                    if not status or status[0] not in {"INTEGRATED", "VERIFIED"}:
                        raise ValueError(f"dependency not integrated: {dep}")
            if new in {"ACCEPTED_LOCAL", "INTEGRATED", "VERIFIED"} and not evidence_ref:
                raise ValueError(f"{new} requires an evidence reference")
            self.conn.execute("UPDATE tasks SET status=? WHERE task_id=?", (new, task_id))
            self._event(task_id, old, new, reason, evidence_ref)

    def status(self):
        missions = [dict(zip(("mission_id", "objective", "repository", "success"), r)) for r in self.conn.execute("SELECT * FROM missions ORDER BY mission_id")]
        tasks = [dict(zip(("task_id", "mission_id", "objective", "acceptance", "dependencies", "authority", "status"), r)) for r in self.conn.execute("SELECT * FROM tasks ORDER BY task_id")]
        for t in tasks:
            t["acceptance"] = json.loads(t["acceptance"])
            t["dependencies"] = json.loads(t["dependencies"])
        return {"missions": missions, "tasks": tasks}

    def history(self, task_id):
        return [dict(zip(("event_id", "old", "new", "reason", "evidence_ref", "timestamp"), r)) for r in self.conn.execute("SELECT * FROM events WHERE task_id=? ORDER BY event_id", (task_id,))]
