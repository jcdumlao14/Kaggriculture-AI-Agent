"""
test_crop_strategy.py

Unit tests for CropStrategy.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from src.parser import ObservationParser
from src.crop_strategy import CropStrategy


# ==========================================================
# Helper
# ==========================================================

def make_observation(day=1):
    """
    Create a standard observation used by the tests.
    """

    return {
        "player": 0,
        "day": day,
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


# ==========================================================
# Best Crop
# ==========================================================

def test_best_crop():

    parser = ObservationParser(make_observation())

    strategy = CropStrategy(parser)

    assert strategy.best_crop() in {
        "WHEAT",
        "CARROT",
        "TOMATO",
        "STRAWBERRY",
        "MELON",
    }


# ==========================================================
# Crop Score
# ==========================================================

def test_crop_score():

    parser = ObservationParser(make_observation())

    strategy = CropStrategy(parser)

    score = strategy.crop_score("WHEAT")

    assert isinstance(score, (int, float))


# ==========================================================
# Early Game Score
# ==========================================================

def test_adjusted_score_returns_number():

    parser = ObservationParser(make_observation(day=2))

    strategy = CropStrategy(parser)

    score = strategy.adjusted_crop_score("WHEAT")

    assert isinstance(score, (int, float))


# ==========================================================
# Late Game Penalty
# ==========================================================

def test_late_game_penalty():

    parser = ObservationParser(make_observation(day=29))

    strategy = CropStrategy(parser)

    assert (
        strategy.adjusted_crop_score("MELON")
        < strategy.crop_score("MELON")
    )


# ==========================================================
# Best Crop Near End of Season
# ==========================================================

def test_best_crop_late_season():

    parser = ObservationParser(make_observation(day=29))

    strategy = CropStrategy(parser)

    crop = strategy.best_crop(remaining_days=2)

    assert crop in {
        "WHEAT",
        "CARROT",
    }