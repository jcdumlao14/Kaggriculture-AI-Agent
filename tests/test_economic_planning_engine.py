from src.economic_planning_engine import (
    EconomicPlanningEngine,
)


def test_sell():

    engine = EconomicPlanningEngine()

    assert engine.recommend(
        "DOWN",
    ) == "SELL"


def test_hold():

    engine = EconomicPlanningEngine()

    assert engine.recommend(
        "UP",
    ) == "HOLD"


def test_wait():

    engine = EconomicPlanningEngine()

    assert engine.recommend(
        "STABLE",
    ) == "WAIT"


def test_unknown():

    engine = EconomicPlanningEngine()

    assert engine.recommend(
        "anything",
    ) == "WAIT"


def test_boolean_helpers():

    engine = EconomicPlanningEngine()

    assert engine.should_sell("DOWN")
    assert engine.should_hold("UP")
    assert engine.should_wait("UNKNOWN")