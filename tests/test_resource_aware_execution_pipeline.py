from src.resource_aware_execution_pipeline import (
    ResourceAwareExecutionPipeline,
)


def test_select():

    pipeline = ResourceAwareExecutionPipeline()

    low = [
        {
            "priority": 20,
            "requirements": {},
        }
    ]

    high = [
        {
            "priority": 100,
            "requirements": {},
        }
    ]

    assert pipeline.select(
        plans=[low, high],
    ) == high


def test_can_execute():

    pipeline = ResourceAwareExecutionPipeline()

    assert pipeline.can_execute(
        resources={"water": 3},
        plan=[
            {
                "requirements": {
                    "water": 1,
                }
            }
        ],
    )


def test_cannot_execute():

    pipeline = ResourceAwareExecutionPipeline()

    assert not pipeline.can_execute(
        resources={"water": 0},
        plan=[
            {
                "requirements": {
                    "water": 1,
                }
            }
        ],
    )


def test_run_success():

    pipeline = ResourceAwareExecutionPipeline()

    plan = [
        {
            "priority": 100,
            "requirements": {
                "water": 2,
            },
        }
    ]

    result = pipeline.run(
        resources={"water": 5},
        plans=[plan],
    )

    assert result["success"]
    assert result["executed"]
    assert result["plan"] == plan


def test_run_updates_resources():

    pipeline = ResourceAwareExecutionPipeline()

    plan = [
        {
            "priority": 100,
            "requirements": {
                "water": 2,
            },
        }
    ]

    result = pipeline.run(
        resources={"water": 5},
        plans=[plan],
    )

    assert result["remaining"] == {
        "water": 3,
    }


def test_run_no_acceptable_plan():

    pipeline = ResourceAwareExecutionPipeline(
        minimum_score=200,
    )

    plan = [
        {
            "priority": 100,
            "requirements": {},
        }
    ]

    result = pipeline.run(
        resources={"water": 5},
        plans=[plan],
    )

    assert not result["success"]
    assert not result["executed"]
    assert result["reason"] == "no_acceptable_plan"


def test_run_unaffordable_plan():

    pipeline = ResourceAwareExecutionPipeline()

    plan = [
        {
            "priority": 100,
            "requirements": {
                "water": 10,
            },
        }
    ]

    result = pipeline.run(
        resources={"water": 2},
        plans=[plan],
    )

    assert not result["success"]
    assert result["reason"] == (
        "insufficient_resources"
    )


def test_remaining_resources():

    pipeline = ResourceAwareExecutionPipeline()

    plan = [
        {
            "priority": 100,
            "requirements": {
                "water": 2,
            },
        }
    ]

    result = pipeline.remaining_resources(
        resources={"water": 5},
        plans=[plan],
    )

    assert result == {
        "water": 3,
    }


def test_remaining_resources_no_plan():

    pipeline = ResourceAwareExecutionPipeline(
        minimum_score=200,
    )

    plan = [
        {
            "priority": 100,
            "requirements": {},
        }
    ]

    result = pipeline.remaining_resources(
        resources={"water": 5},
        plans=[plan],
    )

    assert result == {
        "water": 5,
    }


def test_selected_score():

    pipeline = ResourceAwareExecutionPipeline()

    plan = [
        {
            "priority": 100,
            "requirements": {},
        }
    ]

    assert pipeline.selected_score(
        plans=[plan],
    ) == 100.0


def test_selected_score_empty():

    pipeline = ResourceAwareExecutionPipeline(
        minimum_score=200,
    )

    plan = [
        {
            "priority": 100,
            "requirements": {},
        }
    ]

    assert pipeline.selected_score(
        plans=[plan],
    ) == 0.0