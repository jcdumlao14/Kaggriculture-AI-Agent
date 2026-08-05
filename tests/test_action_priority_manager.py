from src.action_priority_manager import (
    ActionPriorityManager,
)


def test_priority():

    manager = ActionPriorityManager()

    assert manager.priority("HARVEST") == 100


def test_unknown():

    manager = ActionPriorityManager()

    assert manager.priority("UNKNOWN") == 0


def test_higher_priority():

    manager = ActionPriorityManager()

    assert (
        manager.higher_priority(
            "HARVEST",
            "PLANT",
        )
        == "HARVEST"
    )


def test_sort_actions():

    manager = ActionPriorityManager()

    actions = [
        "PASS",
        "PLANT",
        "HARVEST",
    ]

    assert manager.sort_actions(actions) == [
        "HARVEST",
        "PLANT",
        "PASS",
    ]


def test_is_critical():

    manager = ActionPriorityManager()

    assert manager.is_critical("HARVEST")
    assert not manager.is_critical("PLANT")


def test_available_priorities():

    manager = ActionPriorityManager()

    priorities = manager.available_priorities()

    assert priorities["HARVEST"] == 100