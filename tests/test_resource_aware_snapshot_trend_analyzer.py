from src.resource_aware_snapshot_trend_analyzer import (
    ResourceAwareSnapshotTrendAnalyzer,
)


def test_success_rate_improving():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.success_rate_trend(
        change=0.2,
    ) == "improving"


def test_success_rate_declining():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.success_rate_trend(
        change=-0.2,
    ) == "declining"


def test_success_rate_stable():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.success_rate_trend(
        change=0.0,
    ) == "stable"


def test_task_increasing():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.task_trend(
        change=5,
    ) == "increasing"


def test_task_decreasing():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.task_trend(
        change=-5,
    ) == "decreasing"


def test_task_stable():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.task_trend(
        change=0,
    ) == "stable"


def test_result_increasing():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.result_trend(
        change=4,
    ) == "increasing"


def test_result_decreasing():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.result_trend(
        change=-4,
    ) == "decreasing"


def test_result_stable():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.result_trend(
        change=0,
    ) == "stable"


def test_performance_positive():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.performance_trend(
        performance="improved",
    ) == "positive"


def test_performance_negative():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.performance_trend(
        performance="declined",
    ) == "negative"


def test_performance_neutral():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.performance_trend(
        performance="unchanged",
    ) == "neutral"


def test_performance_unknown():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.performance_trend(
        performance="unknown",
    ) == "unknown"


def test_build():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    comparison = {
        "success_rate_change": 0.2,
        "task_count_change": 5,
        "result_count_change": -2,
        "performance": "improved",
    }

    assert analyzer.build(
        comparison=comparison,
    ) == {
        "success_rate_trend": "improving",
        "task_trend": "increasing",
        "result_trend": "decreasing",
        "performance_trend": "positive",
    }


def test_build_missing_values():

    analyzer = (
        ResourceAwareSnapshotTrendAnalyzer()
    )

    assert analyzer.build(
        comparison={},
    ) == {
        "success_rate_trend": "stable",
        "task_trend": "stable",
        "result_trend": "stable",
        "performance_trend": "unknown",
    }