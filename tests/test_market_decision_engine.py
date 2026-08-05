from src.market_decision_engine import (
    MarketDecisionEngine,
)


def test_should_sell():

    engine = MarketDecisionEngine()

    assert engine.should_sell(
        current_price=120,
        average_price=100,
    )


def test_should_buy():

    engine = MarketDecisionEngine()

    assert engine.should_buy(
        current_price=80,
        average_price=100,
    )


def test_price_ratio():

    engine = MarketDecisionEngine()

    assert engine.price_ratio(
        current_price=120,
        average_price=100,
    ) == 1.2


def test_hot_market():

    engine = MarketDecisionEngine()

    assert (
        engine.market_state(
            current_price=140,
            average_price=100,
        )
        == "HOT"
    )


def test_cheap_market():

    engine = MarketDecisionEngine()

    assert (
        engine.market_state(
            current_price=70,
            average_price=100,
        )
        == "CHEAP"
    )