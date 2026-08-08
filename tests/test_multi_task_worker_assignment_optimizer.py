from src.multi_task_worker_assignment_optimizer import (
    MultiTaskWorkerAssignmentOptimizer,
)


def test_assign_multiple_tasks():

    optimizer = (
        MultiTaskWorkerAssignmentOptimizer()
    )

    assignments = optimizer.assign(
        workers={
            "farmer": (0, 0),
            "worker1": (10, 10),
        },
        tasks=[
            {
                "name": "Harvest",
                "priority": 100,
                "position": (1, 1),
            },
            {
                "name": "Water",
                "priority": 50,
                "position": (9, 9),
            },
        ],
    )

    assert len(assignments) == 2
    assert assignments["farmer"]["name"] == "Harvest"
    assert assignments["worker1"]["name"] == "Water"


def test_worker_used_once():

    optimizer = (
        MultiTaskWorkerAssignmentOptimizer()
    )

    assignments = optimizer.assign(
        workers={
            "farmer": (0, 0),
        },
        tasks=[
            {
                "name": "Harvest",
                "priority": 100,
                "position": (1, 1),
            },
            {
                "name": "Water",
                "priority": 50,
                "position": (2, 2),
            },
        ],
    )

    assert len(assignments) == 1
    assert assignments["farmer"]["name"] == "Harvest"


def test_unassigned_tasks():

    optimizer = (
        MultiTaskWorkerAssignmentOptimizer()
    )

    remaining = optimizer.unassigned_tasks(
        workers={
            "farmer": (0, 0),
        },
        tasks=[
            {
                "name": "Harvest",
                "priority": 100,
                "position": (1, 1),
            },
            {
                "name": "Water",
                "priority": 50,
                "position": (2, 2),
            },
        ],
    )

    assert len(remaining) == 1
    assert remaining[0]["name"] == "Water"


def test_idle_workers():

    optimizer = (
        MultiTaskWorkerAssignmentOptimizer()
    )

    idle = optimizer.idle_workers(
        workers={
            "farmer": (0, 0),
            "worker1": (5, 5),
        },
        tasks=[
            {
                "name": "Harvest",
                "priority": 100,
                "position": (1, 1),
            }
        ],
    )

    assert idle == ["worker1"]


def test_empty_workers():

    optimizer = (
        MultiTaskWorkerAssignmentOptimizer()
    )

    assert optimizer.assign(
        workers={},
        tasks=[
            {
                "name": "Harvest",
                "priority": 100,
                "position": (1, 1),
            }
        ],
    ) == {}


def test_empty_tasks():

    optimizer = (
        MultiTaskWorkerAssignmentOptimizer()
    )

    assert optimizer.assign(
        workers={
            "farmer": (0, 0),
        },
        tasks=[],
    ) == {}