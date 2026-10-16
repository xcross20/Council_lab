"""Versioned fixture loader with strict separation between policy observations and oracle truth."""
import json
from pathlib import Path
from .recovery import Scenario


def load_scenarios(path: str | Path) -> list[Scenario]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    scenarios = [Scenario(**row) for row in payload["scenarios"]]
    ids = [s.scenario_id for s in scenarios]
    if len(ids) != len(set(ids)):
        raise ValueError("scenario IDs must be unique")
    return scenarios
