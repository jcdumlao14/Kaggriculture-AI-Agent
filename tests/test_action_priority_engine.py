from src.action_priority_engine import (
    ActionPriorityEngine,
)


def test_rank():

    engine = ActionPriorityEngine()

    actions = [
        {"action": "MOVE", "priority": 10},
        {"action": "HARVEST", "priority": 100},
        {"action": "WATER", "priority": 50},
    ]

    ranked = engine.rank(actions)

    assert ranked[0]["action"] == "HARVEST"


def test_best_action():

    engine = ActionPriorityEngine()

    actions = [
        {"action": "MOVE", "priority": 5},
        {"action": "SELL", "priority": 20},
    ]

    assert (
        engine.best_action(actions)["action"]
        == "SELL"
    )


def test_empty():

    engine = ActionPriorityEngine()

    assert engine.best_action([]) is None


def test_priorities():

    engine = ActionPriorityEngine()

    actions = [
        {"priority": 3},
        {"priority": 9},
        {"priority": 1},
    ]

    assert engine.priorities(actions) == [9, 3, 1]


def test_default_priority():

    engine = ActionPriorityEngine()

    actions = [
        {"action": "PASS"},
    ]

    assert (
        engine.best_action(actions)["action"]
        == "PASS"
    )