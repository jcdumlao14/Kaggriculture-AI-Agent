from src.multi_turn_planner import MultiTurnPlanner


class FakePlanner:

    def plan(self):

        return [
            {"priority": 1, "task": "HARVEST"},
            {"priority": 2, "task": "SELL"},
            {"priority": 3, "task": "PLANT"},
            {"priority": 4, "task": "WATER"},
        ]


def test_plan_horizon():

    planner = MultiTurnPlanner(FakePlanner())

    tasks = planner.plan(2)

    assert len(tasks) == 2


def test_next_task():

    planner = MultiTurnPlanner(FakePlanner())

    task = planner.next_task()

    assert task["task"] == "HARVEST"

def test_plan_length():

    planner = MultiTurnPlanner(
        FakePlanner()
    )

    assert planner.plan_length(3) == 3


def test_has_plan():

    planner = MultiTurnPlanner(
        FakePlanner()
    )

    assert planner.has_plan()


def test_all_tasks():

    planner = MultiTurnPlanner(
        FakePlanner()
    )

    tasks = planner.all_tasks()

    assert len(tasks) == 4