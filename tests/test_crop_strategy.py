from src.parser import ObservationParser
from src.crop_strategy import CropStrategy


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

    strategy = CropStrategy(parser)

    assert strategy.best_crop() in {
        "WHEAT",
        "CARROT",
        "TOMATO",
        "STRAWBERRY",
        "MELON",
    }

def test_crop_score():

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

    strategy = CropStrategy(parser)

    score = strategy.crop_score("WHEAT")

    assert isinstance(score, (int, float))

# Test 1 — Early Game
def test_adjusted_score_returns_number():
    observation = {
        "player": 0,
        "day": 2,
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
            "prices": {},
            "inventory": {},
        },
        "town": {
            "unlocked_shops": [],
        },
    }

    parser = ObservationParser(observation)
    strategy = CropStrategy(parser)

    score = strategy.adjusted_crop_score("WHEAT")

    assert isinstance(score, (int, float))

# Test 2 — Late Game
def test_late_game_penalty():
    observation = {
        "player": 0,
        "day": 29,
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
            "prices": {},
            "inventory": {},
        },
        "town": {
            "unlocked_shops": [],
        },
    }

    parser = ObservationParser(observation)
    strategy = CropStrategy(parser)

    assert strategy.adjusted_crop_score("MELON") < strategy.crop_score("MELON")