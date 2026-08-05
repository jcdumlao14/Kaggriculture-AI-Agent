from src.market_opportunity_evaluator import (
    MarketOpportunityEvaluator,
)


def test_good_price():

    evaluator = MarketOpportunityEvaluator()

    assert evaluator.is_good_price(
        current_price=120,
        average_price=100,
    )


def test_bad_price():

    evaluator = MarketOpportunityEvaluator()

    assert not evaluator.is_good_price(
        current_price=80,
        average_price=100,
    )


def test_price_ratio():

    evaluator = MarketOpportunityEvaluator()

    assert evaluator.price_ratio(
        current_price=150,
        average_price=100,
    ) == 1.5


def test_zero_average():

    evaluator = MarketOpportunityEvaluator()

    assert evaluator.price_ratio(
        current_price=100,
        average_price=0,
    ) == 0.0


def test_score():

    evaluator = MarketOpportunityEvaluator()

    assert evaluator.score(
        current_price=125,
        average_price=100,
    ) == 1.25