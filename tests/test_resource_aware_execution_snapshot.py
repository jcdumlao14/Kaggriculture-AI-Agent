from src.resource_aware_execution_snapshot import (
    ResourceAwareExecutionSnapshot,
)


def test_create_snapshot():

    snapshotter = (
        ResourceAwareExecutionSnapshot()
    )

    analytics = {
        "total_results": 5,
        "success_count": 4,
        "failure_count": 1,
    }

    snapshot = snapshotter.create(
        analytics=analytics,
    )

    assert snapshot == analytics


def test_snapshot_is_independent():

    snapshotter = (
        ResourceAwareExecutionSnapshot()
    )

    analytics = {
        "resource_consumption": {
            "water": 5,
        }
    }

    snapshot = snapshotter.create(
        analytics=analytics,
    )

    analytics[
        "resource_consumption"
    ]["water"] = 100

    assert snapshot[
        "resource_consumption"
    ]["water"] == 5


def test_total_results():

    snapshotter = (
        ResourceAwareExecutionSnapshot()
    )

    assert snapshotter.total_results(
        snapshot={
            "total_results": 7,
        }
    ) == 7


def test_success_count():

    snapshotter = (
        ResourceAwareExecutionSnapshot()
    )

    assert snapshotter.success_count(
        snapshot={
            "success_count": 6,
        }
    ) == 6


def test_failure_count():

    snapshotter = (
        ResourceAwareExecutionSnapshot()
    )

    assert snapshotter.failure_count(
        snapshot={
            "failure_count": 2,
        }
    ) == 2


def test_success_rate():

    snapshotter = (
        ResourceAwareExecutionSnapshot()
    )

    assert snapshotter.success_rate(
        snapshot={
            "success_rate": 0.75,
        }
    ) == 0.75


def test_resource_consumption():

    snapshotter = (
        ResourceAwareExecutionSnapshot()
    )

    snapshot = {
        "resource_consumption": {
            "water": 4,
            "wheat": 2,
        }
    }

    assert snapshotter.resource_consumption(
        snapshot=snapshot,
    ) == {
        "water": 4,
        "wheat": 2,
    }


def test_rejection_reasons():

    snapshotter = (
        ResourceAwareExecutionSnapshot()
    )

    snapshot = {
        "rejection_reasons": {
            "invalid_plan": 2,
        }
    }

    assert snapshotter.rejection_reasons(
        snapshot=snapshot,
    ) == {
        "invalid_plan": 2,
    }


def test_is_empty():

    snapshotter = (
        ResourceAwareExecutionSnapshot()
    )

    assert snapshotter.is_empty(
        snapshot={
            "total_results": 0,
        }
    )


def test_is_not_empty():

    snapshotter = (
        ResourceAwareExecutionSnapshot()
    )

    assert not snapshotter.is_empty(
        snapshot={
            "total_results": 1,
        }
    )


def test_build():

    snapshotter = (
        ResourceAwareExecutionSnapshot()
    )

    analytics = {
        "total_results": 10,
        "success_count": 8,
        "failure_count": 2,
        "success_rate": 0.8,
        "total_tasks": 15,
        "average_task_count": 1.5,
        "resource_consumption": {
            "water": 10,
        },
        "rejection_reasons": {
            "invalid_plan": 2,
        },
    }

    snapshot = snapshotter.build(
        analytics=analytics,
    )

    assert snapshot == analytics


def test_build_missing_values():

    snapshotter = (
        ResourceAwareExecutionSnapshot()
    )

    snapshot = snapshotter.build(
        analytics={},
    )

    assert snapshot == {
        "total_results": 0,
        "success_count": 0,
        "failure_count": 0,
        "success_rate": 0.0,
        "total_tasks": 0,
        "average_task_count": 0.0,
        "resource_consumption": {},
        "rejection_reasons": {},
    }