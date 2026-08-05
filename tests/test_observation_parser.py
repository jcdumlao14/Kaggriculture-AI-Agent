from src.observation_parser import ObservationParser


def sample_observation():

    return {
        "player": 0,
        "day": 2,
        "hour": 10,
        "farms": [
            {
                "money": 750,
                "tiles": [],
                "farmer": [3, 4],
                "hands": [],
                "unlocked_quadrants": ["NW"],
                "hires_today": 1,
            }
        ],
        "market": {
            "prices": {
                "MELON": 250,
            }
        },
        "town": {
            "unlocked_shops": [],
        },
        "private": {
            "shed": {
                "MELON": 5,
            },
            "seeds": {
                "MELON": 2,
            },
            "inventories": [],
        },
    }


def test_player():

    parser = ObservationParser()

    assert parser.player_id(sample_observation()) == 0


def test_money():

    parser = ObservationParser()

    assert parser.money(sample_observation()) == 750


def test_day():

    parser = ObservationParser()

    assert parser.current_day(sample_observation()) == 2


def test_hour():

    parser = ObservationParser()

    assert parser.current_hour(sample_observation()) == 10


def test_market_prices():

    parser = ObservationParser()

    prices = parser.market_prices(sample_observation())

    assert prices["MELON"] == 250