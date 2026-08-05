from src.animal_profit_evaluator import (
    AnimalProfitEvaluator,
)


def test_goose_profit():

    evaluator = AnimalProfitEvaluator()

    market = {
        "GOOSE": {
            "purchase_cost": 100,
            "product_value": 160,
            "feed_cost": 20,
        }
    }

    animal = {
        "type": "GOOSE",
    }

    assert evaluator.evaluate(
        animal,
        market,
    ) == 40


def test_cow_profit():

    evaluator = AnimalProfitEvaluator()

    market = {
        "COW": {
            "purchase_cost": 500,
            "product_value": 700,
            "feed_cost": 100,
        }
    }

    assert evaluator.evaluate(
        {"type": "COW"},
        market,
    ) == 100


def test_sheep_profit():

    evaluator = AnimalProfitEvaluator()

    market = {
        "SHEEP": {
            "purchase_cost": 300,
            "product_value": 450,
            "feed_cost": 50,
        }
    }

    assert evaluator.evaluate(
        {"type": "SHEEP"},
        market,
    ) == 100


def test_negative_profit():

    evaluator = AnimalProfitEvaluator()

    market = {
        "GOOSE": {
            "purchase_cost": 200,
            "product_value": 150,
            "feed_cost": 25,
        }
    }

    assert evaluator.evaluate(
        {"type": "GOOSE"},
        market,
    ) == -75


def test_zero_profit():

    evaluator = AnimalProfitEvaluator()

    market = {
        "GOOSE": {
            "purchase_cost": 100,
            "product_value": 120,
            "feed_cost": 20,
        }
    }

    assert evaluator.evaluate(
        {"type": "GOOSE"},
        market,
    ) == 0