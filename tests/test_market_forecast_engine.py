from src.market_forecast_engine import (
    MarketForecastEngine,
)


def test_record():

    engine = MarketForecastEngine()

    engine.record(
        "WHEAT",
        100,
    )

    assert engine.has_history(
        "WHEAT",
    )


def test_forecast():

    engine = MarketForecastEngine()

    engine.record(
        "WHEAT",
        100,
    )

    engine.record(
        "WHEAT",
        120,
    )

    engine.record(
        "WHEAT",
        140,
    )

    assert (
        engine.forecast(
            "WHEAT",
        )
        == 120.0
    )


def test_direction():

    engine = MarketForecastEngine()

    engine.record(
        "WHEAT",
        100,
    )

    engine.record(
        "WHEAT",
        150,
    )

    assert (
        engine.expected_direction(
            "WHEAT",
        )
        == "DOWN"
    )


def test_single_value():

    engine = MarketForecastEngine()

    engine.record(
        "CARROT",
        200,
    )

    assert (
        engine.forecast(
            "CARROT",
        )
        == 200.0
    )


def test_unknown():

    engine = MarketForecastEngine()

    assert (
        engine.expected_direction(
            "UNKNOWN",
        )
        == "UNKNOWN"
    )