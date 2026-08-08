from src.resource_aware_execution_result import (
    ResourceAwareExecutionResult,
)


def test_success_result():

    builder = ResourceAwareExecutionResult()

    result = builder.success(
        plan=[
            {"name": "WATER"},
        ],
        resources={
            "water": 2,
        },
        remaining={
            "water": 1,
        },
    )

    assert result["success"]
    assert result["executed"]


def test_success_preserves_plan():

    builder = ResourceAwareExecutionResult()

    plan = [
        {"name": "WATER"},
        {"name": "FEED"},
    ]

    result = builder.success(
        plan=plan,
        resources={},
        remaining={},
    )

    assert result["plan"] == plan


def test_success_reason_is_none():

    builder = ResourceAwareExecutionResult()

    result = builder.success(
        plan=[],
        resources={},
        remaining={},
    )

    assert result["reason"] is None


def test_failure_result():

    builder = ResourceAwareExecutionResult()

    result = builder.failure(
        plan=[
            {"name": "WATER"},
        ],
        resources={
            "water": 0,
        },
        reason="insufficient_resources",
    )

    assert not result["success"]
    assert not result["executed"]


def test_failure_preserves_resources():

    builder = ResourceAwareExecutionResult()

    resources = {
        "water": 0,
        "wheat": 2,
    }

    result = builder.failure(
        plan=[],
        resources=resources,
        reason="insufficient_resources",
    )

    assert result["remaining"] == resources


def test_failure_reason():

    builder = ResourceAwareExecutionResult()

    result = builder.failure(
        plan=[],
        resources={},
        reason="invalid_plan",
    )

    assert result["reason"] == "invalid_plan"


def test_is_success():

    builder = ResourceAwareExecutionResult()

    result = builder.success(
        plan=[],
        resources={},
        remaining={},
    )

    assert builder.is_success(
        result=result,
    )


def test_is_failure():

    builder = ResourceAwareExecutionResult()

    result = builder.failure(
        plan=[],
        resources={},
        reason="invalid_plan",
    )

    assert builder.is_failure(
        result=result,
    )


def test_executed_tasks_success():

    builder = ResourceAwareExecutionResult()

    plan = [
        {"name": "WATER"},
    ]

    result = builder.success(
        plan=plan,
        resources={},
        remaining={},
    )

    assert builder.executed_tasks(
        result=result,
    ) == plan


def test_executed_tasks_failure():

    builder = ResourceAwareExecutionResult()

    result = builder.failure(
        plan=[
            {"name": "WATER"},
        ],
        resources={},
        reason="invalid_plan",
    )

    assert builder.executed_tasks(
        result=result,
    ) == []


def test_reason():

    builder = ResourceAwareExecutionResult()

    result = builder.failure(
        plan=[],
        resources={},
        reason="insufficient_resources",
    )

    assert builder.reason(
        result=result,
    ) == "insufficient_resources"
    