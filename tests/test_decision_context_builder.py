from src.decision_context_builder import (
    DecisionContextBuilder,
)


def make_state():

    return {
        "day": 5,
        "hour": 10,
        "money": 2000,
        "tiles": [1, 2],
        "workers": [1],
        "inventory": {"WHEAT": 3},
        "market": {},
    }


def test_build():

    builder = DecisionContextBuilder()

    context = builder.build(
        game_state=make_state(),
        search_algorithm="MCTS",
    )

    assert context["algorithm"] == "MCTS"


def test_tile_count():

    builder = DecisionContextBuilder()

    context = builder.build(
        game_state=make_state(),
        search_algorithm="MCTS",
    )

    assert builder.tile_count(context) == 2


def test_worker_count():

    builder = DecisionContextBuilder()

    context = builder.build(
        game_state=make_state(),
        search_algorithm="MCTS",
    )

    assert builder.worker_count(context) == 1


def test_inventory():

    builder = DecisionContextBuilder()

    context = builder.build(
        game_state=make_state(),
        search_algorithm="MCTS",
    )

    assert builder.has_inventory(context)


def test_algorithm():

    builder = DecisionContextBuilder()

    context = builder.build(
        game_state=make_state(),
        search_algorithm="Beam Search",
    )

    assert builder.algorithm(context) == "Beam Search"