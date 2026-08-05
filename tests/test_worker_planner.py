from src.worker_planner import WorkerPlanner


def make_state():

    return {
        "farmer": [5, 5],
        "hands": [
            [1, 1],
            [2, 2],
        ],
    }


def test_available_workers():

    planner = WorkerPlanner()

    workers = planner.available_workers(
        make_state(),
    )

    assert len(workers) == 3


def test_worker_count():

    planner = WorkerPlanner()

    assert (
        planner.worker_count(
            make_state(),
        )
        == 3
    )


def test_has_workers():

    planner = WorkerPlanner()

    assert planner.has_workers(
        make_state(),
    )


def test_assign():

    planner = WorkerPlanner()

    assignment = planner.assign(
        [5, 5],
        {
            "action": "HARVEST",
        },
    )

    assert assignment["action"]["action"] == "HARVEST"


def test_empty():

    planner = WorkerPlanner()

    state = {}

    assert (
        planner.worker_count(
            state,
        )
        == 0
    )