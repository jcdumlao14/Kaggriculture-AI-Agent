from src.plan_executor import PlanExecutor


def make_plan():

    return [
        {"action": "PLANT"},
        {"action": "WATER"},
        {"action": "HARVEST"},
    ]


def test_load_plan():

    executor = PlanExecutor()

    executor.load_plan(make_plan())

    assert executor.remaining_actions() == 3


def test_next_action():

    executor = PlanExecutor()

    executor.load_plan(make_plan())

    action = executor.next_action()

    assert action["action"] == "PLANT"


def test_remaining():

    executor = PlanExecutor()

    executor.load_plan(make_plan())

    executor.next_action()

    assert executor.remaining_actions() == 2


def test_has_actions():

    executor = PlanExecutor()

    executor.load_plan(make_plan())

    assert executor.has_actions()


def test_clear():

    executor = PlanExecutor()

    executor.load_plan(make_plan())

    executor.clear()

    assert executor.remaining_actions() == 0