from src.strategy_evaluator import (
    StrategyEvaluator,
)


def test_record():

    evaluator = StrategyEvaluator()

    evaluator.record(
        "HARVEST",
        50,
    )

    assert evaluator.average(
        "HARVEST",
    ) == 50.0


def test_average():

    evaluator = StrategyEvaluator()

    evaluator.record(
        "SELL",
        40,
    )

    evaluator.record(
        "SELL",
        60,
    )

    assert evaluator.average(
        "SELL",
    ) == 50.0


def test_best_strategy():

    evaluator = StrategyEvaluator()

    evaluator.record(
        "PLANT",
        20,
    )

    evaluator.record(
        "HARVEST",
        80,
    )

    assert (
        evaluator.best_strategy()
        == "HARVEST"
    )


def test_strategies():

    evaluator = StrategyEvaluator()

    evaluator.record(
        "A",
        1,
    )

    evaluator.record(
        "B",
        2,
    )

    assert len(
        evaluator.strategies()
    ) == 2


def test_clear():

    evaluator = StrategyEvaluator()

    evaluator.record(
        "SELL",
        10,
    )

    evaluator.clear()

    assert (
        evaluator.best_strategy()
        is None
    )