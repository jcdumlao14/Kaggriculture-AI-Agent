"""
test_parser.py

Unit tests for ObservationParser.
"""

from src.parser import ObservationParser


def make_observation():
    return {
        "player": 0,
        "day": 5,
        "hour": 12,
        "farms": [
            {
                "money": 4500,
                "farmer": [3, 4],
                "tiles": [[None] * 10 for _ in range(10)],
            }
        ],
        "private": {
            "shed": {
                "WHEAT": 8,
            },
            "seeds": {
                "WHEAT": 5,
            },
            "inventories": {},
        },
        "market": {
            "prices": {
                "WHEAT": 120,
            },
            "inventory": {},
        },
        "town": {
            "unlocked_shops": [],
        },
    }


def test_day():
    parser = ObservationParser(make_observation())
    assert parser.day == 5


def test_hour():
    parser = ObservationParser(make_observation())
    assert parser.hour == 12


def test_money():
    parser = ObservationParser(make_observation())
    assert parser.money == 4500


def test_farmer_position():
    parser = ObservationParser(make_observation())
    assert parser.farmer_position == (3, 4)


def test_shed():
    parser = ObservationParser(make_observation())
    assert parser.shed["WHEAT"] == 8


def test_prices():
    parser = ObservationParser(make_observation())
    assert parser.prices["WHEAT"] == 120