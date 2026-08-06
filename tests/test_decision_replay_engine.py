from src.decision_replay_engine import (
    DecisionReplayEngine,
)


def test_record():

    replay = DecisionReplayEngine()

    replay.record(
        1,
        "HARVEST",
        95,
    )

    assert replay.total() == 1


def test_latest():

    replay = DecisionReplayEngine()

    replay.record(
        5,
        "SELL",
        100,
    )

    assert (
        replay.latest()["action"]
        == "SELL"
    )


def test_history():

    replay = DecisionReplayEngine()

    replay.record(
        1,
        "PLANT",
        40,
    )

    replay.record(
        2,
        "WATER",
        50,
    )

    assert len(
        replay.history()
    ) == 2


def test_clear():

    replay = DecisionReplayEngine()

    replay.record(
        3,
        "HARVEST",
        90,
    )

    replay.clear()

    assert replay.total() == 0


def test_empty():

    replay = DecisionReplayEngine()

    assert replay.latest() is None