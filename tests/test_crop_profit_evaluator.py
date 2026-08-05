from src.crop_profit_evaluator import (
    CropProfitEvaluator,
)


def test_positive_profit():

    evaluator = CropProfitEvaluator()

    market = {
        "WHEAT": {
            "seed_cost": 20,
            "sell_price": 50,
        }
    }

    crop = {
        "type": "WHEAT",
    }

    assert evaluator.evaluate(
        crop,
        market,
    ) == 30


def test_zero_profit():

    evaluator = CropProfitEvaluator()

    market = {
        "CARROT": {
            "seed_cost": 40,
            "sell_price": 40,
        }
    }

    crop = {
        "type": "CARROT",
    }

    assert evaluator.evaluate(
        crop,
        market,
    ) == 0


def test_negative_profit():

    evaluator = CropProfitEvaluator()

    market = {
        "TOMATO": {
            "seed_cost": 100,
            "sell_price": 80,
        }
    }

    crop = {
        "type": "TOMATO",
    }

    assert evaluator.evaluate(
        crop,
        market,
    ) == -20


def test_multiple_crop_types():

    evaluator = CropProfitEvaluator()

    market = {
        "WHEAT": {
            "seed_cost": 10,
            "sell_price": 40,
        },
        "MELON": {
            "seed_cost": 120,
            "sell_price": 220,
        },
    }

    assert evaluator.evaluate(
        {"type": "WHEAT"},
        market,
    ) == 30

    assert evaluator.evaluate(
        {"type": "MELON"},
        market,
    ) == 100


def test_large_profit():

    evaluator = CropProfitEvaluator()

    market = {
        "STRAWBERRY": {
            "seed_cost": 150,
            "sell_price": 500,
        }
    }

    assert evaluator.evaluate(
        {"type": "STRAWBERRY"},
        market,
    ) == 350