from src.decision_engine_v2 import DecisionEngineV2


def test_empty_history():

    engine = DecisionEngineV2()

    assert engine.decision_history() == []


def test_clear_history():

    engine = DecisionEngineV2()

    engine.replay.record(
        1,
        "HARVEST",
        100,
    )

    assert len(
        engine.decision_history()
    ) == 1

    engine.clear_history()

    assert engine.decision_history() == []


def test_latest_none():

    engine = DecisionEngineV2()

    assert engine.latest_decision() is None


def test_manual_record():

    engine = DecisionEngineV2()

    engine.replay.record(
        5,
        "SELL",
        80,
    )

    latest = engine.latest_decision()

    assert latest["action"] == "SELL"


def test_history_length():

    engine = DecisionEngineV2()

    engine.replay.record(
        1,
        "PLANT",
        20,
    )

    engine.replay.record(
        2,
        "WATER",
        30,
    )

    assert len(
        engine.decision_history()
    ) == 2