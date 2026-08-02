from src.parser import ObservationParser
from src.profitability import Profitability


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
            "shed": {},
            "seeds": {},
            "inventories": {},
        },
        "market": {
            "prices": {
                "WHEAT": 120,
                "CARROT": 180,
                "TOMATO": 250,
                "STRAWBERRY": 350,
                "MELON": 500,
            },
            "inventory": {},
        },
        "town": {
            "unlocked_shops": [],
        },
    }


def test_profit_positive():
    parser = ObservationParser(make_observation())
    engine = Profitability(parser)

    assert engine.profit("WHEAT") > 0


def test_roi_positive():
    parser = ObservationParser(make_observation())
    engine = Profitability(parser)

    assert engine.roi("WHEAT") > 0


def test_summary_contains_profit():
    parser = ObservationParser(make_observation())
    engine = Profitability(parser)

    summary = engine.summary("WHEAT")

    assert "profit" in summary
