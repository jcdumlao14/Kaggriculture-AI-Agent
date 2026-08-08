from src.resource_aware_execution_analytics_manager import (
    ResourceAwareExecutionAnalyticsManager,
)


def test_initial_manager():

    manager = (
        ResourceAwareExecutionAnalyticsManager()
    )

    assert manager.results() == []
    assert manager.success_count() == 0
    assert manager.failure_count() == 0
    assert manager.success_rate() == 0.0


def test_record():

    manager = (
        ResourceAwareExecutionAnalyticsManager()
    )

    result = {
        "success": True,
        "plan": [
            {"name": "WATER"},
        ],
    }

    assert manager.record(
        result=result,
    ) == result

    assert manager.results() == [result]


def test_success_count():

    manager = (
        ResourceAwareExecutionAnalyticsManager()
    )

    manager.record(
        result={"success": True}
    )

    manager.record(
        result={"success": False}
    )

    manager.record(
        result={"success": True}
    )

    assert manager.success_count() == 2


def test_failure_count():

    manager = (
        ResourceAwareExecutionAnalyticsManager()
    )

    manager.record(
        result={"success": True}
    )

    manager.record(
        result={"success": False}
    )

    manager.record(
        result={"success": False}
    )

    assert manager.failure_count() == 2


def test_success_rate():

    manager = (
        ResourceAwareExecutionAnalyticsManager()
    )

    manager.record(
        result={"success": True}
    )

    manager.record(
        result={"success": False}
    )

    assert manager.success_rate() == 0.5


def test_total_tasks():

    manager = (
        ResourceAwareExecutionAnalyticsManager()
    )

    manager.record(
        result={
            "success": True,
            "plan": [
                {"name": "A"},
                {"name": "B"},
            ],
        }
    )

    manager.record(
        result={
            "success": True,
            "plan": [
                {"name": "C"},
            ],
        }
    )

    assert manager.total_tasks() == 3


def test_average_task_count():

    manager = (
        ResourceAwareExecutionAnalyticsManager()
    )

    manager.record(
        result={
            "plan": [
                {"name": "A"},
                {"name": "B"},
            ],
        }
    )

    manager.record(
        result={
            "plan": [
                {"name": "C"},
                {"name": "D"},
                {"name": "E"},
                {"name": "F"},
            ],
        }
    )

    assert manager.average_task_count() == 3.0


def test_resource_consumption():

    manager = (
        ResourceAwareExecutionAnalyticsManager()
    )

    manager.record(
        result={
            "resources": {
                "water": 5,
            },
            "remaining": {
                "water": 3,
            },
        }
    )

    manager.record(
        result={
            "resources": {
                "water": 3,
            },
            "remaining": {
                "water": 2,
            },
        }
    )

    assert manager.resource_consumption() == {
        "water": 3,
    }


def test_rejection_reasons():

    manager = (
        ResourceAwareExecutionAnalyticsManager()
    )

    manager.record(
        result={
            "success": False,
            "reason": "invalid_plan",
        }
    )

    manager.record(
        result={
            "success": False,
            "reason": "invalid_plan",
        }
    )

    manager.record(
        result={
            "success": False,
            "reason": "insufficient_resources",
        }
    )

    assert manager.rejection_reasons() == {
        "invalid_plan": 2,
        "insufficient_resources": 1,
    }


def test_summary():

    manager = (
        ResourceAwareExecutionAnalyticsManager()
    )

    manager.record(
        result={
            "success": True,
            "plan": [
                {"name": "WATER"},
            ],
            "resources": {
                "water": 5,
            },
            "remaining": {
                "water": 4,
            },
            "reason": None,
        }
    )

    manager.record(
        result={
            "success": False,
            "plan": [],
            "resources": {
                "water": 0,
            },
            "remaining": {
                "water": 0,
            },
            "reason": "insufficient_resources",
        }
    )

    summary = manager.summary()

    assert summary["total_results"] == 2
    assert summary["success_count"] == 1
    assert summary["failure_count"] == 1
    assert summary["success_rate"] == 0.5
    assert summary["total_tasks"] == 1
    assert summary["average_task_count"] == 0.5
    assert summary["resource_consumption"] == {
        "water": 1,
    }
    assert summary["rejection_reasons"] == {
        "insufficient_resources": 1,
    }


def test_clear():

    manager = (
        ResourceAwareExecutionAnalyticsManager()
    )

    manager.record(
        result={"success": True}
    )

    manager.clear()

    assert manager.results() == []
    assert manager.success_count() == 0
    assert manager.failure_count() == 0