from src.resource_balance_analyzer import (
    ResourceBalanceAnalyzer,
)


def test_balance_score():

    analyzer = ResourceBalanceAnalyzer()

    score = analyzer.balance_score(
        money=5000,
        crops=5,
        animals=5,
        fertilizer=10,
    )

    assert score == 100.0


def test_low_money():

    analyzer = ResourceBalanceAnalyzer()

    score = analyzer.balance_score(
        money=500,
        crops=5,
        animals=5,
        fertilizer=10,
    )

    assert score == 80.0


def test_no_fertilizer():

    analyzer = ResourceBalanceAnalyzer()

    score = analyzer.balance_score(
        money=5000,
        crops=5,
        animals=5,
        fertilizer=0,
    )

    assert score == 85.0


def test_balanced():

    analyzer = ResourceBalanceAnalyzer()

    assert analyzer.balanced(
        money=5000,
        crops=5,
        animals=4,
        fertilizer=5,
    )


def test_imbalance():

    analyzer = ResourceBalanceAnalyzer()

    value = analyzer.imbalance(
        money=500,
        crops=10,
        animals=1,
        fertilizer=0,
    )

    assert value > 0