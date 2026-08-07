from src.opponent_memory_engine import (
    OpponentMemoryEngine,
)


def test_record():

    engine = OpponentMemoryEngine()

    engine.record(
        "player1",
        "AGGRESSIVE",
    )

    assert engine.known(
        "player1",
    )


def test_strategy():

    engine = OpponentMemoryEngine()

    engine.record(
        "player1",
        "DEFENSIVE",
    )

    assert (
        engine.strategy(
            "player1",
        )
        == "DEFENSIVE"
    )


def test_games():

    engine = OpponentMemoryEngine()

    engine.record(
        "player1",
        "BALANCED",
    )

    engine.record(
        "player1",
        "BALANCED",
    )

    assert (
        engine.games(
            "player1",
        )
        == 2
    )


def test_unknown():

    engine = OpponentMemoryEngine()

    assert (
        engine.strategy(
            "nobody",
        )
        == "UNKNOWN"
    )


def test_known():

    engine = OpponentMemoryEngine()

    assert not engine.known(
        "player1",
    )

    engine.record(
        "player1",
        "AGGRESSIVE",
    )

    assert engine.known(
        "player1",
    )