from src.resource_consumption_planner import (
    ResourceConsumptionPlanner,
)


def test_consumption():

    planner = ResourceConsumptionPlanner()

    result = planner.consumption(
        task={
            "name": "FERTILIZE",
            "requirements": {
                "fertilizer": 2,
            },
        }
    )

    assert result == {
        "fertilizer": 2,
    }


def test_remaining():

    planner = ResourceConsumptionPlanner()

    result = planner.remaining(
        resources={
            "fertilizer": 5,
            "water": 3,
        },
        task={
            "name": "FERTILIZE",
            "requirements": {
                "fertilizer": 2,
            },
        },
    )

    assert result == {
        "fertilizer": 3,
        "water": 3,
    }


def test_affordable():

    planner = ResourceConsumptionPlanner()

    assert planner.affordable(
        resources={
            "wheat": 5,
        },
        task={
            "name": "FEED",
            "requirements": {
                "wheat": 1,
            },
        },
    )


def test_not_affordable():

    planner = ResourceConsumptionPlanner()

    assert not planner.affordable(
        resources={
            "wheat": 0,
        },
        task={
            "name": "FEED",
            "requirements": {
                "wheat": 1,
            },
        },
    )


def test_apply_multiple_tasks():

    planner = ResourceConsumptionPlanner()

    result = planner.apply(
        resources={
            "water": 5,
            "fertilizer": 3,
        },
        tasks=[
            {
                "name": "WATER",
                "requirements": {
                    "water": 1,
                },
            },
            {
                "name": "FERTILIZE",
                "requirements": {
                    "fertilizer": 2,
                },
            },
        ],
    )

    assert result == {
        "water": 4,
        "fertilizer": 1,
    }


def test_apply_stops_when_unaffordable():

    planner = ResourceConsumptionPlanner()

    result = planner.apply(
        resources={
            "wheat": 1,
        },
        tasks=[
            {
                "name": "FEED",
                "requirements": {
                    "wheat": 1,
                },
            },
            {
                "name": "FEED",
                "requirements": {
                    "wheat": 1,
                },
            },
        ],
    )

    assert result == {
        "wheat": 0,
    }