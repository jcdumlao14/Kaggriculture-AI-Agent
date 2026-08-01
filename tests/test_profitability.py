import sys
from pathlib import Path

# Add the project root to Python's search path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.parser import ObservationParser
from src.profitability import ProfitCalculator


def test_best_crop():
    observation = {
        "player": 0,
        "day": 1,
        "hour": 0,
        "farms": [
            {
                "money": 3000,
                "farmer": [0, 0],
                "tiles": [[None] * 10 for _ in range(10)],
            }
        ],
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

    parser = ObservationParser(observation)
    profit = ProfitCalculator(parser)

    print("Best crop:", profit.best_crop())