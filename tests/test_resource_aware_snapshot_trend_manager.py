from src.resource_aware_snapshot_trend_manager import (
    ResourceAwareSnapshotTrendManager,
)


def test_initial_manager():

    manager = (
        ResourceAwareSnapshotTrendManager()
    )

    assert manager.current() is None
    assert manager.previous() is None
    assert not manager.can_analyze()
    assert manager.comparison() is None
    assert manager.trend() is None


def test_first_snapshot():

    manager = (
        ResourceAwareSnapshotTrendManager()
    )

    snapshot = manager.create_snapshot(
        analytics={
            "success_rate": 0.5,
        }
    )

    assert snapshot[
        "success_rate"
    ] == 0.5

    assert manager.current() is not None
    assert manager.previous() is None
    assert not manager.can_analyze()


def test_second_snapshot():

    manager = (
        ResourceAwareSnapshotTrendManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.5,
        }
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert manager.current()[
        "success_rate"
    ] == 0.8

    assert manager.previous()[
        "success_rate"
    ] == 0.5

    assert manager.can_analyze()


def test_comparison():

    manager = (
        ResourceAwareSnapshotTrendManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.5,
            "total_tasks": 10,
        }
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.8,
            "total_tasks": 15,
        }
    )

    comparison = manager.comparison()

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

    manager = (
        ResourceAwareSnapshotTrendManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.5,
            "total_tasks": 10,
            "total_results": 10,
        }
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.8,
            "total_tasks": 15,
            "total_results": 12,
        }
    )

    trend = manager.trend()

    assert trend == {
        "success_rate_trend": "improving",
        "task_trend": "increasing",
        "result_trend": "increasing",
        "performance_trend": "positive",
    }


def test_declining_trend():

    manager = (
        ResourceAwareSnapshotTrendManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.8,
            "total_tasks": 15,
            "total_results": 15,
        }
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.4,
            "total_tasks": 10,
            "total_results": 12,
        }
    )

    assert manager.performance() == "declined"

    assert manager.trend() == {
        "success_rate_trend": "declining",
        "task_trend": "decreasing",
        "result_trend": "decreasing",
        "performance_trend": "negative",
    }


def test_stable_trend():

    manager = (
        ResourceAwareSnapshotTrendManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.7,
            "total_tasks": 10,
            "total_results": 10,
        }
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.7,
            "total_tasks": 10,
            "total_results": 10,
        }
    )

    assert manager.performance() == "unchanged"

    assert manager.trend() == {
        "success_rate_trend": "stable",
        "task_trend": "stable",
        "result_trend": "stable",
        "performance_trend": "neutral",
    }


def test_trend_without_previous():

    manager = (
        ResourceAwareSnapshotTrendManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert manager.trend() is None
    assert manager.performance() == "unknown"
    assert manager.success_rate_change() == 0.0


def test_success_rate_change():

    manager = (
        ResourceAwareSnapshotTrendManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.5,
        }
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert manager.success_rate_change() == 0.3


def test_clear():

    manager = (
        ResourceAwareSnapshotTrendManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.5,
        }
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.8,
        }
    )

    manager.clear()

    assert manager.current() is None
    assert manager.previous() is None
    assert not manager.can_analyze()
    assert manager.comparison() is None
    assert manager.trend() is None