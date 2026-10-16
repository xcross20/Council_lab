"""Explicit CLI and controlled transitions; no model execution in v0.1."""
import argparse
import json
from pathlib import Path
from uuid import uuid4

from .contracts import Mission, WorkOrder
from .state import StateStore


def main(argv=None):
    p = argparse.ArgumentParser(prog="council", description="Council Lab — mission and execution state foundation")
    p.add_argument("--workspace", default=".", help="Directory containing .council state")
    sub = p.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init", help="Initialize local state")
    init.add_argument("--repo", default=".")
    mission = sub.add_parser("mission", help="Create a mission")
    mission.add_argument("objective")
    mission.add_argument("--success", required=True)
    mission.add_argument("--repo", default=".")
    task = sub.add_parser("task", help="Register a work order")
    task.add_argument("mission_id")
    task.add_argument("objective")
    task.add_argument("--acceptance", required=True)
    task.add_argument("--depends-on", action="append", default=[])
    task.add_argument("--id")
    move = sub.add_parser("transition", help="Change a task state under deterministic rules")
    move.add_argument("task_id")
    move.add_argument("state")
    move.add_argument("--reason", required=True)
    move.add_argument("--evidence")
    sub.add_parser("status", help="Read current mission and task state")
    hist = sub.add_parser("history", help="Read immutable task events")
    hist.add_argument("task_id")
    args = p.parse_args(argv)
    root = Path(args.workspace).resolve()
    if args.command == "init":
        (root / ".council").mkdir(parents=True, exist_ok=True)
        (root / ".council" / "repository.txt").write_text(str(Path(args.repo).resolve())+"\n")
    db = root / ".council" / "state.sqlite3"
    if args.command != "init" and not db.exists():
        p.error("workspace not initialized; run council init first")
    store = StateStore(db)
    try:
        if args.command == "init":
            print(f"Initialized {db}")
        elif args.command == "mission":
            mid = "M-" + uuid4().hex[:8]
            store.add_mission(Mission(mid, args.objective, str(Path(args.repo).resolve()), args.success))
            print(mid)
        elif args.command == "task":
            tid = args.id or "T-" + uuid4().hex[:8]
            store.add_task(WorkOrder(tid, args.mission_id, args.objective, (args.acceptance,), tuple(args.depends_on)))
            print(tid)
        elif args.command == "transition":
            store.transition(args.task_id, args.state, args.reason, args.evidence)
            print(f"{args.task_id}: {args.state}")
        elif args.command == "status":
            print(json.dumps(store.status(), indent=2))
        elif args.command == "history":
            print(json.dumps(store.history(args.task_id), indent=2))
    except (ValueError, KeyError) as ex:
        p.error(str(ex))
    finally:
        store.close()


if __name__ == "__main__":
    main()
