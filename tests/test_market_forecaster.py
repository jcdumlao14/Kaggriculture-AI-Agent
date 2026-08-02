from src.market_memory import MarketMemory
from src.market_forecaster import MarketForecaster


def test_upward_trend():

    memory = MarketMemory()

    memory.update({"WHEAT": 100})
    memory.update({"WHEAT": 120})

    forecast = MarketForecaster(memory)

    assert forecast.will_rise("WHEAT")


def test_downward_trend():

    memory = MarketMemory()

    memory.update({"WHEAT": 150})
    memory.update({"WHEAT": 120})

    forecast = MarketForecaster(memory)

    assert forecast.will_fall("WHEAT")


def test_prediction():

    memory = MarketMemory()

    memory.update({"WHEAT": 100})
    memory.update({"WHEAT": 120})

    forecast = MarketForecaster(memory)

    assert forecast.predicted_price("WHEAT") == 140