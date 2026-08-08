from src.resource_aware_snapshot_comparison_manager import (
    ResourceAwareSnapshotComparisonManager,
)


def test_initial_manager():

    manager = (
        ResourceAwareSnapshotComparisonManager()
    )

    assert manager.current() is None
    assert manager.previous() is None
    assert not manager.can_compare()
    assert manager.compare() is None


def test_create_first_snapshot():

    manager = (
        ResourceAwareSnapshotComparisonManager()
    )

    snapshot = manager.create_snapshot(
        analytics={
            "success_rate": 0.5,
        }
    )

    assert snapshot["success_rate"] == 0.5
    assert manager.current() is not None
    assert manager.previous() is None


def test_create_second_snapshot():

    manager = (
        ResourceAwareSnapshotComparisonManager()
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


def test_can_compare():

    manager = (
        ResourceAwareSnapshotComparisonManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.5,
        }
    )

    assert not manager.can_compare()

    manager.create_snapshot(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert manager.can_compare()


def test_compare_without_previous():

    manager = (
        ResourceAwareSnapshotComparisonManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert manager.compare() is None


def test_compare():

    manager = (
        ResourceAwareSnapshotComparisonManager()
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

    comparison = manager.compare()

    assert comparison[
        "success_rate_change"
    ] == 0.3

    assert comparison[
        "task_count_change"
    ] == 5

    assert comparison[
        "performance"
    ] == "improved"


def test_performance_without_previous():

    manager = (
        ResourceAwareSnapshotComparisonManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert manager.performance() == "unknown"


def test_performance_improved():

    manager = (
        ResourceAwareSnapshotComparisonManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.4,
        }
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.9,
        }
    )

    assert manager.performance() == "improved"


def test_performance_declined():

    manager = (
        ResourceAwareSnapshotComparisonManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.9,
        }
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.4,
        }
    )

    assert manager.performance() == "declined"


def test_performance_unchanged():

    manager = (
        ResourceAwareSnapshotComparisonManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.7,
        }
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.7,
        }
    )

    assert manager.performance() == "unchanged"


def test_success_rate_change_without_previous():

    manager = (
        ResourceAwareSnapshotComparisonManager()
    )

    manager.create_snapshot(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert manager.success_rate_change() == 0.0


def test_success_rate_change():

    manager = (
        ResourceAwareSnapshotComparisonManager()
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
        ResourceAwareSnapshotComparisonManager()
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
    assert not manager.can_compare()