from src.turn_execution_planner import (
    TurnExecutionPlanner,
)


def test_build_plan():

    planner = TurnExecutionPlanner()

    assignments = {
        "farmer": {
            "name": "Harvest",
            "priority": 100,
        },
        "worker1": {
            "name": "Water",
            "priority": 60,
        },
    }

    plan = planner.build_plan(
        assignments=assignments,
    )

    assert len(plan) == 2
    assert plan[0]["task"] == "Harvest"
    assert plan[1]["task"] == "Water"


def test_next_step():

    planner = TurnExecutionPlanner()

    plan = [
        {
            "worker": "farmer",
            "task": "Harvest",
            "priority": 100,
        },
        {
            "worker": "worker1",
            "task": "Water",
            "priority": 50,
        },
    ]

    assert (
        planner.next_step(plan)["task"]
        == "Harvest"
    )


def test_empty_plan():

    planner = TurnExecutionPlanner()

    assert planner.next_step([]) is None


def test_total_steps():

    planner = TurnExecutionPlanner()

    plan = [
        {"task": "Harvest"},
        {"task": "Water"},
        {"task": "Feed"},
    ]

    assert planner.total_steps(plan) == 3


def test_build_empty_plan():

    planner = TurnExecutionPlanner()

    plan = planner.build_plan(
        assignments={},
    )

    assert plan == []