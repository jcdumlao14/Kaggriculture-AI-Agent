from src.resource_aware_execution_guard import (
    ResourceAwareExecutionGuard,
)


def test_affordable_plan():

    guard = ResourceAwareExecutionGuard()

    assert guard.is_affordable(
        resources={"water": 3},
        plan=[
            {
                "requirements": {
                    "water": 2,
                }
            }
        ],
    )


def test_unaffordable_plan():

    guard = ResourceAwareExecutionGuard()

    assert not guard.is_affordable(
        resources={"water": 1},
        plan=[
            {
                "requirements": {
                    "water": 2,
                }
            }
        ],
    )


def test_multiple_tasks_consume_resources():

    guard = ResourceAwareExecutionGuard()

    assert guard.is_affordable(
        resources={"water": 3},
        plan=[
            {
                "requirements": {
                    "water": 1,
                }
            },
            {
                "requirements": {
                    "water": 2,
                }
            },
        ],
    )


def test_multiple_tasks_exceed_resources():

    guard = ResourceAwareExecutionGuard()

    assert not guard.is_affordable(
        resources={"water": 2},
        plan=[
            {
                "requirements": {
                    "water": 1,
                }
            },
            {
                "requirements": {
                    "water": 2,
                }
            },
        ],
    )


def test_can_execute():

    guard = ResourceAwareExecutionGuard()

    assert guard.can_execute(
        resources={"water": 2},
        plan=[
            {
                "name": "WATER",
                "requirements": {
                    "water": 1,
                },
            }
        ],
    )


def test_invalid_plan_cannot_execute():

    guard = ResourceAwareExecutionGuard()

    assert not guard.can_execute(
        resources={"water": 2},
        plan=[
            {
                "requirements": {
                    "water": -1,
                }
            }
        ],
    )


def test_remaining_resources():

    guard = ResourceAwareExecutionGuard()

    result = guard.remaining_resources(
        resources={
            "water": 5,
            "wheat": 3,
        },
        plan=[
            {
                "requirements": {
                    "water": 2,
                }
            },
            {
                "requirements": {
                    "wheat": 1,
                }
            },
        ],
    )

    assert result == {
        "water": 3,
        "wheat": 2,
    }


def test_remaining_resources_rejected_plan():

    guard = ResourceAwareExecutionGuard()

    resources = {
        "water": 1,
    }

    result = guard.remaining_resources(
        resources=resources,
        plan=[
            {
                "requirements": {
                    "water": 2,
                }
            }
        ],
    )

    assert result == resources


def test_reject_reason_invalid_plan():

    guard = ResourceAwareExecutionGuard()

    result = guard.reject_reason(
        resources={"water": 5},
        plan=[
            {
                "requirements": {
                    "water": -1,
                }
            }
        ],
    )

    assert result == "invalid_plan"


def test_reject_reason_insufficient_resources():

    guard = ResourceAwareExecutionGuard()

    result = guard.reject_reason(
        resources={"water": 1},
        plan=[
            {
                "requirements": {
                    "water": 2,
                }
            }
        ],
    )

    assert result == "insufficient_resources"


def test_no_rejection():

    guard = ResourceAwareExecutionGuard()

    result = guard.reject_reason(
        resources={"water": 5},
        plan=[
            {
                "requirements": {
                    "water": 2,
                }
            }
        ],
    )

    assert result is None