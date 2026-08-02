from src.money_manager import MoneyManager
from src.parser import ObservationParser


def make_observation(money=3000):

    return {
        "player": 0,
        "day": 1,
        "hour": 0,
        "farms": [{
            "money": money,
            "farmer": [0, 0],
            "tiles": [[None] * 10 for _ in range(10)],
        }],
        "private": {
            "shed": {},
            "seeds": {},
            "inventories": {},
        },
        "market": {
            "prices": {},
            "inventory": {},
        },
        "town": {
            "unlocked_shops": [],
        },
    }


def test_available_cash():

    parser = ObservationParser(make_observation(3000))

    manager = MoneyManager(parser)

    assert manager.available_cash() == 2500


def test_can_afford():

    parser = ObservationParser(make_observation(3000))

    manager = MoneyManager(parser)

    assert manager.can_afford(1000)


def test_should_save():

    parser = ObservationParser(make_observation(300))

    manager = MoneyManager(parser)

    assert manager.should_save()


def test_spending_ratio():

    parser = ObservationParser(make_observation(3000))

    manager = MoneyManager(parser)

    ratio = manager.spending_ratio()

    assert 0 <= ratio <= 1