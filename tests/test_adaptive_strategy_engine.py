from src.adaptive_strategy_engine import (
    AdaptiveStrategyEngine,
)


def test_economic_sell():

    engine = AdaptiveStrategyEngine()

    assert (
        engine.adjustment(
            "SELL",
            "ECONOMIC",
        )
        == 20
    )


def test_aggressive_expand():

    engine = AdaptiveStrategyEngine()

    assert (
        engine.adjustment(
            "EXPAND",
            "AGGRESSIVE",
        )
        == 20
    )


def test_unknown():

    engine = AdaptiveStrategyEngine()

    assert (
        engine.adjustment(
            "SELL",
            "UNKNOWN",
        )
        == 0
    )


def test_apply():

    engine = AdaptiveStrategyEngine()

    score = engine.apply(
        100,
        action="SELL",
        strategy="ECONOMIC",
    )

    assert score == 120


def test_supported():

    engine = AdaptiveStrategyEngine()

    assert (
        "ECONOMIC"
        in engine.supported_strategies()
    )