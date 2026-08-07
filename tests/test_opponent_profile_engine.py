from src.opponent_profile_engine import (
    OpponentProfileEngine,
)


def test_record():

    engine = OpponentProfileEngine()

    engine.record(
        "player1",
        "AGGRESSIVE",
    )

    assert engine.known(
        "player1",
    )


def test_dominant_strategy():

    engine = OpponentProfileEngine()

    engine.record(
        "player1",
        "ECONOMIC",
    )

    engine.record(
        "player1",
        "ECONOMIC",
    )

    engine.record(
        "player1",
        "BALANCED",
    )

    assert (
        engine.dominant_strategy(
            "player1",
        )
        == "ECONOMIC"
    )


def test_strategy_count():

    engine = OpponentProfileEngine()

    engine.record(
        "player1",
        "BALANCED",
    )

    engine.record(
        "player1",
        "BALANCED",
    )

    assert (
        engine.strategy_count(
            "player1",
            "BALANCED",
        )
        == 2
    )


def test_unknown():

    engine = OpponentProfileEngine()

    assert (
        engine.dominant_strategy(
            "unknown",
        )
        == "UNKNOWN"
    )


def test_known():

    engine = OpponentProfileEngine()

    assert not engine.known(
        "player1",
    )

    engine.record(
        "player1",
        "FARMING",
    )

    assert engine.known(
        "player1",
    )