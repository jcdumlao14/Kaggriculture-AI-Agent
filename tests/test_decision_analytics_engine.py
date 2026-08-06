from src.decision_analytics_engine import (
    DecisionAnalyticsEngine,
)


def test_record():

    engine = DecisionAnalyticsEngine()

    engine.record(
        "HARVEST",
        80,
    )

    assert engine.count() == 1


def test_average():

    engine = DecisionAnalyticsEngine()

    engine.record(
        "SELL",
        50,
    )

    engine.record(
        "HARVEST",
        70,
    )

    assert engine.average_score() == 60.0


def test_best():

    engine = DecisionAnalyticsEngine()

    engine.record(
        "SELL",
        30,
    )

    engine.record(
        "HARVEST",
        90,
    )

    assert (
        engine.best()["action"]
        == "HARVEST"
    )


def test_clear():

    engine = DecisionAnalyticsEngine()

    engine.record(
        "BUY",
        10,
    )

    engine.clear()

    assert engine.count() == 0


def test_empty_average():

    engine = DecisionAnalyticsEngine()

    assert engine.average_score() == 0.0