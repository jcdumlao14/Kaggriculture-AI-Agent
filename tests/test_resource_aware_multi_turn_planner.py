from src.resource_aware_multi_turn_planner import (
    ResourceAwareMultiTurnPlanner,
)


def test_can_schedule():

    planner = ResourceAwareMultiTurnPlanner()

    assert planner.can_schedule(
        resources={"water": 2},
        task={
            "name": "WATER",
            "requirements": {
                "water": 1,
            },
        },
    )


def test_build_plan():

    planner = ResourceAwareMultiTurnPlanner()

    plan = planner.build_plan(
        resources={"water": 2},
        tasks=[
            {
                "name": "Water A",
                "priority": 100,
                "requirements": {
                    "water": 1,
                },
            },
            {
                "name": "Water B",
                "priority": 80,
                "requirements": {
                    "water": 1,
                },
            },
        ],
    )

    assert len(plan) == 2


def test_resource_limit():

    planner = ResourceAwareMultiTurnPlanner()

    plan = planner.build_plan(
        resources={"water": 1},
        tasks=[
            {
                "name": "Water A",
                "priority": 100,
                "requirements": {
                    "water": 1,
                },
            },
            {
                "name": "Water B",
                "priority": 80,
                "requirements": {
                    "water": 1,
                },
            },
        ],
    )

    assert len(plan) == 1
    assert plan[0]["name"] == "Water A"


def test_priority_order():

    planner = ResourceAwareMultiTurnPlanner()

    plan = planner.build_plan(
        resources={"water": 2},
        tasks=[
            {
                "name": "Low",
                "priority": 10,
                "requirements": {
                    "water": 1,
                },
            },
            {
                "name": "High",
                "priority": 100,
                "requirements": {
                    "water": 1,
                },
            },
        ],
    )

    assert plan[0]["name"] == "High"


def test_max_turns():

    planner = ResourceAwareMultiTurnPlanner()

    plan = planner.build_plan(
        resources={"water": 5},
        tasks=[
            {
                "name": "A",
                "priority": 100,
                "requirements": {
                    "water": 1,
                },
            },
            {
                "name": "B",
                "priority": 90,
                "requirements": {
                    "water": 1,
                },
            },
            {
                "name": "C",
                "priority": 80,
                "requirements": {
                    "water": 1,
                },
            },
        ],
        max_turns=2,
    )

    assert len(plan) == 2


def test_zero_max_turns():

    planner = ResourceAwareMultiTurnPlanner()

    assert planner.build_plan(
        resources={"water": 5},
        tasks=[
            {
                "name": "Water",
                "priority": 100,
                "requirements": {
                    "water": 1,
                },
            }
        ],
        max_turns=0,
    ) == []


def test_remaining_resources():

    planner = ResourceAwareMultiTurnPlanner()

    plan = [
        {
            "name": "Water",
            "requirements": {
                "water": 2,
            },
        }
    ]

    result = planner.remaining_resources(
        resources={"water": 5},
        plan=plan,
    )

    assert result == {
        "water": 3,
    }


def test_plan_cost():

    planner = ResourceAwareMultiTurnPlanner()

    plan = [
        {
            "name": "A",
            "requirements": {
                "water": 2,
                "wheat": 1,
            },
        },
        {
            "name": "B",
            "requirements": {
                "water": 1,
            },
        },
    ]

    result = planner.plan_cost(
        plan=plan,
    )

    assert result == {
        "water": 3,
        "wheat": 1,
    }


def test_skips_unaffordable_task():

    planner = ResourceAwareMultiTurnPlanner()

    plan = planner.build_plan(
        resources={"water": 0},
        tasks=[
            {
                "name": "Water",
                "priority": 100,
                "requirements": {
                    "water": 1,
                },
            },
            {
                "name": "Harvest",
                "priority": 50,
                "requirements": {},
            },
        ],
    )

    assert len(plan) == 1
    assert plan[0]["name"] == "Harvest"