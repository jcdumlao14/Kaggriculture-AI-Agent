from src.resource_aware_execution_metrics import (
    ResourceAwareExecutionMetrics,
)


def test_task_count():

    metrics = ResourceAwareExecutionMetrics()

    assert metrics.task_count(
        result={
            "plan": [
                {"name": "WATER"},
                {"name": "FEED"},
            ]
        }
    ) == 2


def test_task_count_invalid_plan():

    metrics = ResourceAwareExecutionMetrics()

    assert metrics.task_count(
        result={
            "plan": None,
        }
    ) == 0


def test_executed_count_success():

    metrics = ResourceAwareExecutionMetrics()

    assert metrics.executed_count(
        result={
            "executed": True,
            "plan": [
                {"name": "WATER"},
            ],
        }
    ) == 1


def test_executed_count_failure():

    metrics = ResourceAwareExecutionMetrics()

    assert metrics.executed_count(
        result={
            "executed": False,
            "plan": [
                {"name": "WATER"},
            ],
        }
    ) == 0


def test_success_rate():

    metrics = ResourceAwareExecutionMetrics()

    results = [
        {"success": True},
        {"success": True},
        {"success": False},
    ]

    assert metrics.success_rate(
        results=results,
    ) == 2 / 3


def test_empty_success_rate():

    metrics = ResourceAwareExecutionMetrics()

    assert metrics.success_rate(
        results=[],
    ) == 0.0


def test_failure_count():

    metrics = ResourceAwareExecutionMetrics()

    results = [
        {"success": True},
        {"success": False},
        {"success": False},
    ]

    assert metrics.failure_count(
        results=results,
    ) == 2


def test_resource_consumption():

    metrics = ResourceAwareExecutionMetrics()

    result = {
        "resources": {
            "water": 5,
            "wheat": 3,
        },
        "remaining": {
            "water": 3,
            "wheat": 2,
        },
    }

    assert metrics.resource_consumption(
        result=result,
    ) == {
        "water": 2,
        "wheat": 1,
    }


def test_total_resource_consumption():

    metrics = ResourceAwareExecutionMetrics()

    results = [
        {
            "resources": {
                "water": 5,
            },
            "remaining": {
                "water": 3,
            },
        },
        {
            "resources": {
                "water": 3,
            },
            "remaining": {
                "water": 2,
            },
        },
    ]

    assert metrics.total_resource_consumption(
        results=results,
    ) == {
        "water": 3,
    }


def test_build():

    metrics = ResourceAwareExecutionMetrics()

    result = {
        "success": True,
        "executed": True,
        "plan": [
            {"name": "WATER"},
        ],
        "resources": {
            "water": 5,
        },
        "remaining": {
            "water": 4,
        },
    }

    output = metrics.build(
        result=result,
    )

    assert output == {
        "success": True,
        "task_count": 1,
        "executed_count": 1,
        "resource_consumption": {
            "water": 1,
        },
    }