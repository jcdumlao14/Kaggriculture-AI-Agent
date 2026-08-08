from src.resource_aware_execution_insights import (
    ResourceAwareExecutionInsights,
)


def test_initial_state():

    insights = (
        ResourceAwareExecutionInsights()
    )

    assert insights.current() is None
    assert insights.previous() is None
    assert insights.comparison() is None
    assert insights.trend() is None
    assert insights.performance() == "unknown"
    assert insights.success_rate_change() == 0.0
    assert not insights.ready_for_comparison()


def test_record_first_snapshot():

    insights = (
        ResourceAwareExecutionInsights()
    )

    snapshot = insights.record(
        analytics={
            "success_rate": 0.5,
            "total_tasks": 10,
        }
    )

    assert snapshot[
        "success_rate"
    ] == 0.5

    assert insights.current()[
        "success_rate"
    ] == 0.5

    assert insights.previous() is None


def test_record_second_snapshot():

    insights = (
        ResourceAwareExecutionInsights()
    )

    insights.record(
        analytics={
            "success_rate": 0.5,
            "total_tasks": 10,
        }
    )

    insights.record(
        analytics={
            "success_rate": 0.8,
            "total_tasks": 15,
        }
    )

    assert insights.ready_for_comparison()

    assert insights.current()[
        "success_rate"
    ] == 0.8

    assert insights.previous()[
        "success_rate"
    ] == 0.5


def test_comparison():

    insights = (
        ResourceAwareExecutionInsights()
    )

    insights.record(
        analytics={
            "success_rate": 0.5,
            "total_tasks": 10,
            "total_results": 10,
        }
    )

    insights.record(
        analytics={
            "success_rate": 0.8,
            "total_tasks": 15,
            "total_results": 14,
        }
    )

    comparison = insights.comparison()

    assert comparison[
        "success_rate_change"
    ] == 0.3

    assert comparison[
        "task_count_change"
    ] == 5

    assert comparison[
        "result_count_change"
    ] == 4

    assert comparison[
        "performance"
    ] == "improved"


def test_trend():

    insights = (
        ResourceAwareExecutionInsights()
    )

    insights.record(
        analytics={
            "success_rate": 0.5,
            "total_tasks": 10,
            "total_results": 10,
        }
    )

    insights.record(
        analytics={
            "success_rate": 0.8,
            "total_tasks": 15,
            "total_results": 14,
        }
    )

    assert insights.trend() == {
        "success_rate_trend": "improving",
        "task_trend": "increasing",
        "result_trend": "increasing",
        "performance_trend": "positive",
    }


def test_declining_execution():

    insights = (
        ResourceAwareExecutionInsights()
    )

    insights.record(
        analytics={
            "success_rate": 0.9,
            "total_tasks": 20,
        }
    )

    insights.record(
        analytics={
            "success_rate": 0.4,
            "total_tasks": 15,
        }
    )

    assert insights.performance() == "declined"

    assert insights.success_rate_change() == -0.5

    assert insights.trend() == {
        "success_rate_trend": "declining",
        "task_trend": "decreasing",
        "result_trend": "stable",
        "performance_trend": "negative",
    }


def test_stable_execution():

    insights = (
        ResourceAwareExecutionInsights()
    )

    insights.record(
        analytics={
            "success_rate": 0.7,
            "total_tasks": 10,
        }
    )

    insights.record(
        analytics={
            "success_rate": 0.7,
            "total_tasks": 10,
        }
    )

    assert insights.performance() == "unchanged"

    assert insights.success_rate_change() == 0.0

    assert insights.trend() == {
        "success_rate_trend": "stable",
        "task_trend": "stable",
        "result_trend": "stable",
        "performance_trend": "neutral",
    }


def test_clear():

    insights = (
        ResourceAwareExecutionInsights()
    )

    insights.record(
        analytics={
            "success_rate": 0.5,
        }
    )

    insights.record(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert insights.ready_for_comparison()

    insights.clear()

    assert insights.current() is None
    assert insights.previous() is None
    assert insights.comparison() is None
    assert insights.trend() is None
    assert not insights.ready_for_comparison()