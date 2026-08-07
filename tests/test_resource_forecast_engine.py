from src.resource_forecast_engine import (
    ResourceForecastEngine,
)


def test_forecast():

    engine = ResourceForecastEngine()

    result = engine.forecast(
        current=100,
        production=20,
        consumption=10,
        turns=5,
    )

    assert result == 150


def test_shortage():

    engine = ResourceForecastEngine()

    assert engine.shortage(
        current=10,
        production=0,
        consumption=5,
        turns=3,
    )


def test_not_shortage():

    engine = ResourceForecastEngine()

    assert not engine.shortage(
        current=100,
        production=20,
        consumption=5,
        turns=5,
    )


def test_surplus():

    engine = ResourceForecastEngine()

    assert engine.surplus(
        current=50,
        production=10,
        consumption=5,
        turns=5,
    )


def test_not_surplus():

    engine = ResourceForecastEngine()

    assert not engine.surplus(
        current=100,
        production=5,
        consumption=10,
        turns=5,
    )