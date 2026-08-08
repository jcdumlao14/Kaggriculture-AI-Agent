from src.resource_aware_execution_coordinator import (
    ResourceAwareExecutionCoordinator,
)


def test_can_execute():

    coordinator = ResourceAwareExecutionCoordinator()

    assert coordinator.can_execute(
        resources={"water": 3},
        plan=[
            {
                "name": "WATER",
                "requirements": {
                    "water": 1,
                },
            }
        ],
    )


def test_cannot_execute_without_resources():

    coordinator = ResourceAwareExecutionCoordinator()

    assert not coordinator.can_execute(
        resources={"water": 0},
        plan=[
            {
                "name": "WATER",
                "requirements": {
                    "water": 1,
                },
            }
        ],
    )


def test_execute_success():

    coordinator = ResourceAwareExecutionCoordinator()

    result = coordinator.execute(
        resources={"water": 3},
        plan=[
            {
                "name": "WATER",
                "requirements": {
                    "water": 1,
                },
            }
        ],
    )

    assert result["success"]
    assert result["executed"]


def test_execute_updates_resources():

    coordinator = ResourceAwareExecutionCoordinator()

    result = coordinator.execute(
        resources={
            "water": 5,
            "wheat": 2,
        },
        plan=[
            {
                "name": "WATER",
                "requirements": {
                    "water": 2,
                },
            }
        ],
    )

    assert result["remaining"] == {
        "water": 3,
        "wheat": 2,
    }


def test_execute_failure():

    coordinator = ResourceAwareExecutionCoordinator()

    result = coordinator.execute(
        resources={"water": 0},
        plan=[
            {
                "name": "WATER",
                "requirements": {
                    "water": 1,
                },
            }
        ],
    )

    assert not result["success"]
    assert not result["executed"]


def test_execute_failure_reason():

    coordinator = ResourceAwareExecutionCoordinator()

    result = coordinator.execute(
        resources={"water": 0},
        plan=[
            {
                "name": "WATER",
                "requirements": {
                    "water": 1,
                },
            }
        ],
    )

    assert result["reason"] == (
        "insufficient_resources"
    )


def test_invalid_plan_failure():

    coordinator = ResourceAwareExecutionCoordinator()

    result = coordinator.execute(
        resources={"water": 5},
        plan=[
            {
                "requirements": {
                    "water": -1,
                }
            }
        ],
    )

    assert not result["success"]
    assert result["reason"] == "invalid_plan"


def test_remaining_resources():

    coordinator = ResourceAwareExecutionCoordinator()

    result = coordinator.remaining_resources(
        resources={"water": 5},
        plan=[
            {
                "requirements": {
                    "water": 2,
                }
            }
        ],
    )

    assert result == {
        "water": 3,
    }


def test_rejected_resources_are_preserved():

    coordinator = ResourceAwareExecutionCoordinator()

    resources = {
        "water": 1,
    }

    result = coordinator.remaining_resources(
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


def test_rejection_reason():

    coordinator = ResourceAwareExecutionCoordinator()

    result = coordinator.rejection_reason(
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


def test_no_rejection_reason():

    coordinator = ResourceAwareExecutionCoordinator()

    result = coordinator.rejection_reason(
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