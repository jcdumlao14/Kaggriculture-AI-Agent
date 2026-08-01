"""
test_scheduler.py

Unit tests for the Scheduler.
"""

from src.scheduler import Scheduler


def test_add_task():
    scheduler = Scheduler()

    scheduler.add(
        priority=2,
        action="WATER",
        target=(1, 2),
    )

    assert len(scheduler) == 1


def test_priority_order():
    scheduler = Scheduler()

    scheduler.add(priority=5, action="PLANT")
    scheduler.add(priority=1, action="HARVEST")
    scheduler.add(priority=3, action="FEED")

    task = scheduler.next()

    assert task.action == "HARVEST"


def test_clear():
    scheduler = Scheduler()

    scheduler.add(priority=1, action="PASS")

    scheduler.clear()

    assert scheduler.empty()


def test_summary():
    scheduler = Scheduler()

    scheduler.add(
        priority=1,
        action="HARVEST",
        target=(3, 4),
    )

    summary = scheduler.summary()

    assert summary[0]["action"] == "HARVEST"
    assert summary[0]["priority"] == 1


def test_iteration():
    scheduler = Scheduler()

    scheduler.add(priority=2, action="WATER")
    scheduler.add(priority=1, action="HARVEST")

    actions = [task.action for task in scheduler]

    assert actions == ["HARVEST", "WATER"]