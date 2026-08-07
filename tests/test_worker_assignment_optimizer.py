from src.worker_assignment_optimizer import (
    WorkerAssignmentOptimizer,
)


def test_assign():

    optimizer = WorkerAssignmentOptimizer()

    assignments = optimizer.assign(
        workers=[
            "farmer",
            "worker1",
        ],
        tasks=[
            {
                "name": "Harvest",
                "priority": 100,
            },
            {
                "name": "Water",
                "priority": 50,
            },
        ],
    )

    assert assignments["farmer"]["name"] == "Harvest"
    assert assignments["worker1"]["name"] == "Water"


def test_unassigned_tasks():

    optimizer = WorkerAssignmentOptimizer()

    remaining = optimizer.unassigned_tasks(
        workers=["farmer"],
        tasks=[
            {"name": "Harvest", "priority": 100},
            {"name": "Water", "priority": 50},
        ],
    )

    assert len(remaining) == 1
    assert remaining[0]["name"] == "Water"


def test_idle_workers():

    optimizer = WorkerAssignmentOptimizer()

    idle = optimizer.idle_workers(
        workers=[
            "farmer",
            "worker1",
            "worker2",
        ],
        tasks=[
            {
                "name": "Harvest",
                "priority": 100,
            }
        ],
    )

    assert idle == [
        "worker1",
        "worker2",
    ]


def test_no_idle_workers():

    optimizer = WorkerAssignmentOptimizer()

    idle = optimizer.idle_workers(
        workers=["farmer"],
        tasks=[
            {
                "name": "Harvest",
                "priority": 100,
            }
        ],
    )

    assert idle == []


def test_empty_tasks():

    optimizer = WorkerAssignmentOptimizer()

    assignments = optimizer.assign(
        workers=[
            "farmer",
        ],
        tasks=[],
    )

    assert assignments == {}