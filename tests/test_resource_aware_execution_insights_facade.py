from src.resource_aware_execution_insights_facade import (
    ResourceAwareExecutionInsightsFacade,
)


def test_initial_state():

    facade = (
        ResourceAwareExecutionInsightsFacade()
    )

    assert facade.current() is None
    assert facade.previous() is None
    assert facade.comparison() is None
    assert facade.trend() is None
    assert facade.performance() == "unknown"
    assert facade.success_rate_change() == 0.0
    assert not facade.ready()


def test_record():

    facade = (
        ResourceAwareExecutionInsightsFacade()
    )

    snapshot = facade.record(
        analytics={
            "success_rate": 0.6,
            "total_tasks": 10,
        }
    )

    assert snapshot[
        "success_rate"
    ] == 0.6

    assert facade.current()[
        "total_tasks"
    ] == 10


def test_previous_snapshot():

    facade = (
        ResourceAwareExecutionInsightsFacade()
    )

    facade.record(
        analytics={
            "success_rate": 0.5,
        }
    )

    facade.record(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert facade.previous()[
        "success_rate"
    ] == 0.5

    assert facade.current()[
        "success_rate"
    ] == 0.8


def test_ready():

    facade = (
        ResourceAwareExecutionInsightsFacade()
    )

    facade.record(
        analytics={
            "success_rate": 0.5,
        }
    )

    assert not facade.ready()

    facade.record(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert facade.ready()


def test_comparison():

    facade = (
        ResourceAwareExecutionInsightsFacade()
    )

    facade.record(
        analytics={
            "success_rate": 0.5,
            "total_tasks": 10,
        }
    )

    facade.record(
        analytics={
            "success_rate": 0.8,
            "total_tasks": 15,
        }
    )

    comparison = facade.comparison()

    assert comparison[
        "success_rate_change"
    ] == 0.3

    assert comparison[
        "task_count_change"
    ] == 5

    assert comparison[
        "performance"
    ] == "improved"


def test_trend():

    facade = (
        ResourceAwareExecutionInsightsFacade()
    )

    facade.record(
        analytics={
            "success_rate": 0.5,
            "total_tasks": 10,
        }
    )

    facade.record(
        analytics={
            "success_rate": 0.8,
            "total_tasks": 15,
        }
    )

    assert facade.trend() == {
        "success_rate_trend": "improving",
        "task_trend": "increasing",
        "result_trend": "stable",
        "performance_trend": "positive",
    }


def test_declining():

    facade = (
        ResourceAwareExecutionInsightsFacade()
    )

    facade.record(
        analytics={
            "success_rate": 0.9,
            "total_tasks": 20,
        }
    )

    facade.record(
        analytics={
            "success_rate": 0.4,
            "total_tasks": 15,
        }
    )

    assert facade.performance() == "declined"
    assert facade.success_rate_change() == -0.5


def test_stable():

    facade = (
        ResourceAwareExecutionInsightsFacade()
    )

    facade.record(
        analytics={
            "success_rate": 0.7,
            "total_tasks": 10,
        }
    )

    facade.record(
        analytics={
            "success_rate": 0.7,
            "total_tasks": 10,
        }
    )

    assert facade.performance() == "unchanged"
    assert facade.success_rate_change() == 0.0


def test_clear():

    facade = (
        ResourceAwareExecutionInsightsFacade()
    )

    facade.record(
        analytics={
            "success_rate": 0.5,
        }
    )

    facade.record(
        analytics={
            "success_rate": 0.8,
        }
    )

    facade.clear()

    assert facade.current() is None
    assert facade.previous() is None
    assert facade.comparison() is None
    assert facade.trend() is None
    assert not facade.ready()