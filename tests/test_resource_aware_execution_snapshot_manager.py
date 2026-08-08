from src.resource_aware_execution_snapshot_manager import (
    ResourceAwareExecutionSnapshotManager,
)


def test_initial_manager():

    manager = (
        ResourceAwareExecutionSnapshotManager()
    )

    assert manager.current() is None
    assert manager.previous() is None
    assert not manager.has_current()
    assert not manager.has_previous()


def test_create_current_snapshot():

    manager = (
        ResourceAwareExecutionSnapshotManager()
    )

    analytics = {
        "total_results": 5,
        "success_count": 4,
        "failure_count": 1,
        "success_rate": 0.8,
    }

    snapshot = manager.create(
        analytics=analytics,
    )

    assert snapshot["total_results"] == 5
    assert manager.current() == snapshot
    assert manager.has_current()


def test_first_snapshot_has_no_previous():

    manager = (
        ResourceAwareExecutionSnapshotManager()
    )

    manager.create(
        analytics={
            "success_rate": 0.5,
        }
    )

    assert manager.previous() is None
    assert not manager.has_previous()


def test_second_snapshot_moves_current_to_previous():

    manager = (
        ResourceAwareExecutionSnapshotManager()
    )

    first = {
        "total_results": 5,
        "success_rate": 0.5,
    }

    second = {
        "total_results": 10,
        "success_rate": 0.8,
    }

    manager.create(analytics=first)
    manager.create(analytics=second)

    assert manager.previous() == {
        "total_results": 5,
        "success_rate": 0.5,
        "success_count": 0,
        "failure_count": 0,
        "total_tasks": 0,
        "average_task_count": 0.0,
        "resource_consumption": {},
        "rejection_reasons": {},
    }

    assert manager.current() == {
        "total_results": 10,
        "success_rate": 0.8,
        "success_count": 0,
        "failure_count": 0,
        "total_tasks": 0,
        "average_task_count": 0.0,
        "resource_consumption": {},
        "rejection_reasons": {},
    }


def test_current_is_independent():

    manager = (
        ResourceAwareExecutionSnapshotManager()
    )

    analytics = {
        "success_rate": 0.75,
        "resource_consumption": {
            "water": 5,
        },
    }

    manager.create(
        analytics=analytics,
    )

    current = manager.current()

    current["resource_consumption"]["water"] = 100

    assert manager.current()[
        "resource_consumption"
    ]["water"] == 5


def test_previous_is_independent():

    manager = (
        ResourceAwareExecutionSnapshotManager()
    )

    manager.create(
        analytics={
            "success_rate": 0.5,
            "resource_consumption": {
                "water": 3,
            },
        }
    )

    manager.create(
        analytics={
            "success_rate": 0.8,
        }
    )

    previous = manager.previous()

    previous[
        "resource_consumption"
    ]["water"] = 100

    assert manager.previous()[
        "resource_consumption"
    ]["water"] == 3


def test_current_success_rate():

    manager = (
        ResourceAwareExecutionSnapshotManager()
    )

    manager.create(
        analytics={
            "success_rate": 0.75,
        }
    )

    assert manager.current_success_rate() == 0.75


def test_previous_success_rate():

    manager = (
        ResourceAwareExecutionSnapshotManager()
    )

    manager.create(
        analytics={
            "success_rate": 0.5,
        }
    )

    manager.create(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert manager.previous_success_rate() == 0.5


def test_success_rate_change():

    manager = (
        ResourceAwareExecutionSnapshotManager()
    )

    manager.create(
        analytics={
            "success_rate": 0.5,
        }
    )

    manager.create(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert manager.success_rate_change() == 0.3


def test_success_rate_change_without_previous():

    manager = (
        ResourceAwareExecutionSnapshotManager()
    )

    manager.create(
        analytics={
            "success_rate": 0.8,
        }
    )

    assert manager.success_rate_change() == 0.8


def test_clear():

    manager = (
        ResourceAwareExecutionSnapshotManager()
    )

    manager.create(
        analytics={
            "success_rate": 0.5,
        }
    )

    manager.create(
        analytics={
            "success_rate": 0.8,
        }
    )

    manager.clear()

    assert manager.current() is None
    assert manager.previous() is None
    assert not manager.has_current()
    assert not manager.has_previous()