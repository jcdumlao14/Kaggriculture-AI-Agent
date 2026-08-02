from src.market import Market
from src.market_memory import MarketMemory


class FakeParser:
    def __init__(self):
        self.prices = {
            "WHEAT": 120,
            "CARROT": 180,
            "FERTILIZER": 50,
        }

        self.inventory = {}

        self.shed = {
            "WHEAT": 5,
        }


def test_good_sell_price():

    parser = FakeParser()

    market = Market(parser)

    memory = MarketMemory()

    memory.update({"WHEAT": 80})
    memory.update({"WHEAT": 100})
    memory.update({"WHEAT": 120})

    assert market.is_good_sell_price(
        "WHEAT",
        memory,
    )


def test_good_buy_price():

    parser = FakeParser()

    market = Market(parser)

    memory = MarketMemory()

    memory.update({"WHEAT": 150})
    memory.update({"WHEAT": 140})
    memory.update({"WHEAT": 120})

    assert market.is_good_buy_price(
        "WHEAT",
        memory,
    )