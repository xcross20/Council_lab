"""Strict contracts for the first executable vertical slice."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Mission:
    mission_id: str
    objective: str
    repository: str
    success: str

    def __post_init__(self):
        if not all((self.mission_id.strip(), self.objective.strip(), self.repository.strip(), self.success.strip())):
            raise ValueError("mission fields may not be empty")


@dataclass(frozen=True)
class WorkOrder:
    task_id: str
    mission_id: str
    objective: str
    acceptance: tuple[str, ...]
    dependencies: tuple[str, ...] = ()
    authority: str = "LOCAL_ONLY"

    def __post_init__(self):
        if not self.task_id or not self.mission_id or not self.objective or not self.acceptance:
            raise ValueError("work order requires task id, mission id, objective and acceptance")
        if self.authority != "LOCAL_ONLY":
            raise ValueError("v0.1 supports only LOCAL_ONLY authority")
