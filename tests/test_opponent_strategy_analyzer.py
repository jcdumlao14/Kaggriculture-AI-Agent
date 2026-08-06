from src.opponent_model import (
    OpponentModel,
)

from src.opponent_strategy_analyzer import (
    OpponentStrategyAnalyzer,
)


def test_unknown():

    analyzer = OpponentStrategyAnalyzer(
        OpponentModel(),
    )

    assert (
        analyzer.strategy()
        == "UNKNOWN"
    )


def test_economic():

    model = OpponentModel()

    model.record("SELL")
    model.record("SELL")
    model.record("PLANT")

    analyzer = OpponentStrategyAnalyzer(
        model,
    )

    assert analyzer.is_economic()


def test_aggressive():

    model = OpponentModel()

    model.record("HARVEST")
    model.record("HARVEST")
    model.record("PLANT")

    analyzer = OpponentStrategyAnalyzer(
        model,
    )

    assert analyzer.is_aggressive()


def test_expansion():

    model = OpponentModel()

    model.record("EXPAND")
    model.record("EXPAND")
    model.record("SELL")

    analyzer = OpponentStrategyAnalyzer(
        model,
    )

    assert analyzer.is_expansion()


def test_strategy_string():

    model = OpponentModel()

    model.record("SELL")

    analyzer = OpponentStrategyAnalyzer(
        model,
    )

    assert isinstance(
        analyzer.strategy(),
        str,
    )