from src.inventory_strategy import InventoryStrategy
from src.market import Market
from src.parser import ObservationParser


def make_observation():
    return {
        "player": 0,
        "day": 1,
        "hour": 0,
        "farms": [{
            "money": 3000,
            "farmer": [0, 0],
            "tiles": [[None] * 10 for _ in range(10)],
        }],
        "private": {
            "shed": {
                "WHEAT": 10,
                "CARROT": 5,
            },
            "seeds": {
                "WHEAT": 2,
            },
            "inventories": {},
        },
        "market": {
            "prices": {
                "WHEAT": 120,
                "CARROT": 180,
            },
            "inventory": {},
        },
        "town": {
            "unlocked_shops": [],
        },
    }


def test_inventory_value():

    parser = ObservationParser(make_observation())

    market = Market(parser)

    inventory = InventoryStrategy(parser, market)

    assert inventory.inventory_value() == (10 * 120 + 5 * 180)


def test_keep_seed():

    parser = ObservationParser(make_observation())

    market = Market(parser)

    inventory = InventoryStrategy(parser, market)

    assert inventory.should_keep_seed("WHEAT")


def test_store_or_sell():

    parser = ObservationParser(make_observation())

    market = Market(parser)

    inventory = InventoryStrategy(parser, market)

    assert isinstance(inventory.should_sell("WHEAT"), bool)
    assert isinstance(inventory.should_store("WHEAT"), bool)


def test_liquidation():

    parser = ObservationParser(make_observation())

    market = Market(parser)

    inventory = InventoryStrategy(parser, market)

    products = inventory.liquidate_inventory()

    assert "WHEAT" in products
    assert "CARROT" in products