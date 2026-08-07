from src.market_trend_engine import (
    MarketTrendEngine,
)


def test_record():

    engine = MarketTrendEngine()

    engine.record(
        "WHEAT",
        100,
    )

    assert (
        engine.observations(
            "WHEAT",
        )
        == 1
    )


def test_latest_price():

    engine = MarketTrendEngine()

    engine.record(
        "WHEAT",
        120,
    )

    engine.record(
        "WHEAT",
        140,
    )

    assert (
        engine.latest_price(
            "WHEAT",
        )
        == 140.0
    )


def test_average_price():

    engine = MarketTrendEngine()

    engine.record(
        "WHEAT",
        100,
    )

    engine.record(
        "WHEAT",
        200,
    )

    assert (
        engine.average_price(
            "WHEAT",
        )
        == 150.0
    )


def test_trend():

    engine = MarketTrendEngine()

    engine.record(
        "WHEAT",
        100,
    )

    engine.record(
        "WHEAT",
        130,
    )

    assert (
        engine.trend(
            "WHEAT",
        )
        == "RISING"
    )


def test_unknown():

    engine = MarketTrendEngine()

    assert (
        engine.trend(
            "CARROT",
        )
        == "UNKNOWN"
    )