from src.search_dispatcher import (
    SearchDispatcher,
)


def test_dispatch():

    dispatcher = SearchDispatcher()

    assert (
        dispatcher.dispatch(
            "BEAM_SEARCH",
            {},
        )
        == "BEAM_SEARCH"
    )


def test_supported():

    dispatcher = SearchDispatcher()

    assert dispatcher.supports(
        "MCTS"
    )


def test_not_supported():

    dispatcher = SearchDispatcher()

    assert not dispatcher.supports(
        "UNKNOWN"
    )


def test_supported_algorithms():

    dispatcher = SearchDispatcher()

    algorithms = (
        dispatcher.supported_algorithms()
    )

    assert len(algorithms) == 4


def test_minimax_exists():

    dispatcher = SearchDispatcher()

    assert (
        "MINIMAX"
        in dispatcher.supported_algorithms()
    )