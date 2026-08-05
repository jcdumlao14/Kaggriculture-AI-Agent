from src.market_action_generator import (
    MarketActionGenerator,
)


def test_sell_melon():

    generator = MarketActionGenerator()

    state = {
        "money": 100,
        "shed": {
            "MELON": 5,
        },
        "seeds": {},
        "market": {
            "prices": {
                "MELON": 250,
            }
        },
    }

    actions = generator.generate(state)

    assert actions == [["SELL", "MELON", 5]]


def test_buy_seed():

    generator = MarketActionGenerator()

    state = {
        "money": 500,
        "shed": {},
        "seeds": {
            "MELON": 0,
        },
        "market": {
            "prices": {},
        },
    }

    actions = generator.generate(state)

    assert actions == [["BUY_SEED", "MELON", 1]]


def test_no_action():

    generator = MarketActionGenerator()

    state = {
        "money": 50,
        "shed": {},
        "seeds": {
            "MELON": 2,
        },
        "market": {
            "prices": {
                "MELON": 100,
            }
        },
    }

    actions = generator.generate(state)

    assert actions == []


def test_multiple_actions():

    generator = MarketActionGenerator()

    state = {
        "money": 500,
        "shed": {
            "MELON": 4,
        },
        "seeds": {
            "MELON": 0,
        },
        "market": {
            "prices": {
                "MELON": 220,
            }
        },
    }

    actions = generator.generate(state)

    assert len(actions) == 2


def test_return_type():

    generator = MarketActionGenerator()

    assert isinstance(generator.generate({}), list)