from src.market_memory import MarketMemory


def test_update():

    memory = MarketMemory()

    memory.update({"WHEAT": 100})

    assert memory.latest("WHEAT") == 100


def test_average():

    memory = MarketMemory()

    memory.update({"WHEAT": 100})
    memory.update({"WHEAT": 200})

    assert memory.average("WHEAT") == 150


def test_trend_up():

    memory = MarketMemory()

    memory.update({"WHEAT": 100})
    memory.update({"WHEAT": 120})

    assert memory.trend("WHEAT") == "UP"


def test_trend_down():

    memory = MarketMemory()

    memory.update({"WHEAT": 120})
    memory.update({"WHEAT": 100})

    assert memory.trend("WHEAT") == "DOWN"


def test_trend_flat():

    memory = MarketMemory()

    memory.update({"WHEAT": 100})
    memory.update({"WHEAT": 100})

    assert memory.trend("WHEAT") == "FLAT"