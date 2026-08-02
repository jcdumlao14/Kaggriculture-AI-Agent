from src.goal_manager import GoalManager


def test_default_goal():

    manager = GoalManager()

    assert manager.current_goal() == "MAKE_PROFIT"


def test_save_money_goal():

    manager = GoalManager()

    manager.update(
        money=300,
        day=5,
    )

    assert manager.current_goal() == "SAVE_MONEY"


def test_expand_goal():

    manager = GoalManager()

    manager.update(
        money=9000,
        day=10,
    )

    assert manager.current_goal() == "EXPAND_FARM"


def test_final_goal():

    manager = GoalManager()

    manager.update(
        money=5000,
        day=29,
    )

    assert manager.current_goal() == "FINAL_PROFIT"


def test_reset():

    manager = GoalManager()

    manager.update(
        money=9000,
        day=10,
    )

    manager.reset()

    assert manager.current_goal() == "MAKE_PROFIT"