from src.multi_turn_execution_planner import (
    MultiTurnExecutionPlanner,
)


def test_build():

    planner = MultiTurnExecutionPlanner()

    plan = planner.build(
        turns=[
            [
                {"task": "Harvest"},
                {"task": "Water"},
            ],
            [
                {"task": "Plant"},
            ],
        ]
    )

    assert len(plan) == 3
    assert plan[0]["turn"] == 0
    assert plan[2]["turn"] == 1


def test_turn_plan():

    planner = MultiTurnExecutionPlanner()

    turns = [
        [{"task": "Harvest"}],
        [{"task": "Plant"}],
    ]

    result = planner.turn_plan(
        turns=turns,
        turn=1,
    )

    assert result[0]["task"] == "Plant"


def test_invalid_turn():

    planner = MultiTurnExecutionPlanner()

    assert planner.turn_plan(
        turns=[],
        turn=5,
    ) == []


def test_total_actions():

    planner = MultiTurnExecutionPlanner()

    total = planner.total_actions(
        turns=[
            [{"task": "A"}],
            [{"task": "B"}, {"task": "C"}],
        ]
    )

    assert total == 3


def test_empty():

    planner = MultiTurnExecutionPlanner()

    assert planner.total_actions(
        turns=[],
    ) == 0