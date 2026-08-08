from src.resource_aware_execution_snapshot_comparator import (
    ResourceAwareExecutionSnapshotComparator,
)


def test_success_rate_change():

    comparator = (
        ResourceAwareExecutionSnapshotComparator()
    )

    assert comparator.success_rate_change(
        current={
            "success_rate": 0.8,
        },
        previous={
            "success_rate": 0.5,
        },
    ) == 0.3


def test_success_rate_decline():

    comparator = (
        ResourceAwareExecutionSnapshotComparator()
    )

    assert comparator.success_rate_change(
        current={
            "success_rate": 0.4,
        },
        previous={
            "success_rate": 0.7,
        },
    ) == -0.3


def test_success_rate_unchanged():

    comparator = (
        ResourceAwareExecutionSnapshotComparator()
    )

    assert comparator.success_rate_change(
        current={
            "success_rate": 0.5,
        },
        previous={
            "success_rate": 0.5,
        },
    ) == 0.0


def test_task_count_change():

    comparator = (
        ResourceAwareExecutionSnapshotComparator()
    )

    assert comparator.task_count_change(
        current={
            "total_tasks": 15,
        },
        previous={
            "total_tasks": 10,
        },
    ) == 5


def test_result_count_change():

    comparator = (
        ResourceAwareExecutionSnapshotComparator()
    )

    assert comparator.result_count_change(
        current={
            "total_results": 20,
        },
        previous={
            "total_results": 12,
        },
    ) == 8


def test_resource_change():

    comparator = (
        ResourceAwareExecutionSnapshotComparator()
    )

    assert comparator.resource_change(
        current={
            "resource_consumption": {
                "water": 8,
                "wheat": 3,
            },
        },
        previous={
            "resource_consumption": {
                "water": 5,
                "wheat": 4,
            },
        },
    ) == {
        "water": 3,
        "wheat": -1,
    }


def test_resource_change_new_resource():

    comparator = (
        ResourceAwareExecutionSnapshotComparator()
    )

    assert comparator.resource_change(
        current={
            "resource_consumption": {
                "water": 5,
            },
        },
        previous={
            "resource_consumption": {},
        },
    ) == {
        "water": 5,
    }


def test_performance_improved():

    comparator = (
        ResourceAwareExecutionSnapshotComparator()
    )

    assert comparator.performance(
        current={
            "success_rate": 0.8,
        },
        previous={
            "success_rate": 0.5,
        },
    ) == "improved"


def test_performance_declined():

    comparator = (
        ResourceAwareExecutionSnapshotComparator()
    )

    assert comparator.performance(
        current={
            "success_rate": 0.4,
        },
        previous={
            "success_rate": 0.7,
        },
    ) == "declined"


def test_performance_unchanged():

    comparator = (
        ResourceAwareExecutionSnapshotComparator()
    )

    assert comparator.performance(
        current={
            "success_rate": 0.5,
        },
        previous={
            "success_rate": 0.5,
        },
    ) == "unchanged"


def test_build():

    comparator = (
        ResourceAwareExecutionSnapshotComparator()
    )

    current = {
        "success_rate": 0.8,
        "total_tasks": 15,
        "total_results": 20,
        "resource_consumption": {
            "water": 8,
        },
    }

    previous = {
        "success_rate": 0.5,
        "total_tasks": 10,
        "total_results": 12,
        "resource_consumption": {
            "water": 5,
        },
    }

    assert comparator.build(
        current=current,
        previous=previous,
    ) == {
        "success_rate_change": 0.3,
        "task_count_change": 5,
        "result_count_change": 8,
        "resource_change": {
            "water": 3,
        },
        "performance": "improved",
    }


def test_missing_values():

    comparator = (
        ResourceAwareExecutionSnapshotComparator()
    )

    assert comparator.build(
        current={},
        previous={},
    ) == {
        "success_rate_change": 0.0,
        "task_count_change": 0,
        "result_count_change": 0,
        "resource_change": {},
        "performance": "unchanged",
    }