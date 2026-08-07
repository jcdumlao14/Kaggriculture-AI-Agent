from src.action_utility_ranker import (
    ActionUtilityRanker,
)


def test_rank():

    ranker = ActionUtilityRanker()

    actions = [
        {"action": "MOVE", "utility": 10},
        {"action": "HARVEST", "utility": 100},
        {"action": "WATER", "utility": 50},
    ]

    ranked = ranker.rank(actions)

    assert ranked[0]["action"] == "HARVEST"


def test_best():

    ranker = ActionUtilityRanker()

    actions = [
        {"action": "MOVE", "utility": 5},
        {"action": "SELL", "utility": 20},
    ]

    assert (
        ranker.best(actions)["action"]
        == "SELL"
    )


def test_empty():

    ranker = ActionUtilityRanker()

    assert ranker.best([]) is None


def test_utilities():

    ranker = ActionUtilityRanker()

    actions = [
        {"utility": 3},
        {"utility": 9},
        {"utility": 1},
    ]

    assert ranker.utilities(actions) == [
        9,
        3,
        1,
    ]


def test_default():

    ranker = ActionUtilityRanker()

    actions = [
        {"action": "WAIT"},
    ]

    assert (
        ranker.best(actions)["action"]
        == "WAIT"
    )