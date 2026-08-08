from src.worker_assignment_cost_optimizer import (
    WorkerAssignmentCostOptimizer,
)


def test_assignment_score():

    optimizer = WorkerAssignmentCostOptimizer()

    score = optimizer.assignment_score(
        task_priority=100,
        worker_position=(0, 0),
        task_position=(3, 4),
    )

    assert score == 93.0


def test_zero_travel_cost():

    optimizer = WorkerAssignmentCostOptimizer()

    score = optimizer.assignment_score(
        task_priority=100,
        worker_position=(2, 2),
        task_position=(2, 2),
    )

    assert score == 100.0


def test_best_worker():

    optimizer = WorkerAssignmentCostOptimizer()

    worker = optimizer.best_worker(
        workers={
            "farmer": (0, 0),
            "worker1": (9, 9),
        },
        task_priority=100,
        task_position=(2, 2),
    )

    assert worker == "farmer"


def test_rank_workers():

    optimizer = WorkerAssignmentCostOptimizer()

    ranked = optimizer.rank_workers(
        workers={
            "farmer": (0, 0),
            "worker1": (5, 5),
            "worker2": (10, 10),
        },
        task_priority=100,
        task_position=(2, 2),
    )

    assert ranked[0]["worker"] == "farmer"
    assert ranked[-1]["worker"] == "worker2"


def test_empty_workers():

    optimizer = WorkerAssignmentCostOptimizer()

    assert optimizer.best_worker(
        workers={},
        task_priority=100,
        task_position=(0, 0),
    ) is None


def test_empty_rank():

    optimizer = WorkerAssignmentCostOptimizer()

    assert optimizer.rank_workers(
        workers={},
        task_priority=100,
        task_position=(0, 0),
    ) == []


def test_travel_weight():

    optimizer = WorkerAssignmentCostOptimizer(
        travel_weight=2.0,
    )

    score = optimizer.assignment_score(
        task_priority=100,
        worker_position=(0, 0),
        task_position=(3, 4),
    )

    assert score == 86.0


def test_negative_travel_weight():

    try:
        WorkerAssignmentCostOptimizer(
            travel_weight=-1.0,
        )

        assert False

    except ValueError:
        assert True