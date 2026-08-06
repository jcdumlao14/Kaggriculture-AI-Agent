from src.decision_learning_engine import (
    DecisionLearningEngine,
)


def test_record():

    engine = DecisionLearningEngine()

    engine.record(
        "HARVEST",
        50,
    )

    assert engine.total_records() == 1


def test_average():

    engine = DecisionLearningEngine()

    engine.record(
        "SELL",
        20,
    )

    engine.record(
        "SELL",
        40,
    )

    assert engine.average_reward(
        "SELL",
    ) == 30.0


def test_adjustment():

    engine = DecisionLearningEngine()

    engine.record(
        "PLANT",
        100,
    )

    assert engine.adjustment(
        "PLANT",
    ) == 10.0


def test_unknown():

    engine = DecisionLearningEngine()

    assert (
        engine.average_reward(
            "UNKNOWN",
        )
        == 0.0
    )


def test_clear():

    engine = DecisionLearningEngine()

    engine.record(
        "HARVEST",
        50,
    )

    engine.clear()

    assert engine.total_records() == 0