from src.farm_state_evaluator import (
    FarmStateEvaluator,
)


def test_money_score():

    evaluator = FarmStateEvaluator()

    observation = {
        "farm": {
            "money": 3000,
            "unlocked_quadrants": ["NW"],
            "tiles": [],
        }
    }

    assert evaluator.evaluate(observation) == 3500


def test_land_bonus():

    evaluator = FarmStateEvaluator()

    observation = {
        "farm": {
            "money": 0,
            "unlocked_quadrants": [
                "NW",
                "NE",
            ],
            "tiles": [],
        }
    }

    assert evaluator.evaluate(observation) == 1000


def test_crop_bonus():

    evaluator = FarmStateEvaluator()

    observation = {
        "farm": {
            "money": 0,
            "unlocked_quadrants": [],
            "tiles": [
                [
                    {
                        "kind": "PLANT",
                    }
                ]
            ],
        }
    }

    assert evaluator.evaluate(observation) == 50


def test_animal_bonus():

    evaluator = FarmStateEvaluator()

    observation = {
        "farm": {
            "money": 0,
            "unlocked_quadrants": [],
            "tiles": [
                [
                    {
                        "kind": "COOP",
                        "animal": "GOOSE",
                    }
                ]
            ],
        }
    }

    assert evaluator.evaluate(observation) == 200


def test_combined_score():

    evaluator = FarmStateEvaluator()

    observation = {
        "farm": {
            "money": 1000,
            "unlocked_quadrants": [
                "NW",
                "NE",
            ],
            "tiles": [
                [
                    {"kind": "PLANT"},
                    {
                        "kind": "PASTURE",
                        "animal": "COW",
                    },
                ]
            ],
        }
    }

    assert evaluator.evaluate(observation) == 2250