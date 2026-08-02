from src.strategy_manager import StrategyManager


def test_default_strategy():

    manager = StrategyManager()

    assert manager.current() == "BALANCED"


def test_conservative():

    manager = StrategyManager()

    manager.update(
        goal="SAVE_MONEY",
        risk=0.2,
        day=5,
    )

    assert manager.current() == "CONSERVATIVE"


def test_expansion():

    manager = StrategyManager()

    manager.update(
        goal="EXPAND_FARM",
        risk=0.2,
        day=8,
    )

    assert manager.current() == "EXPANSION"


def test_safe():

    manager = StrategyManager()

    manager.update(
        goal="MAKE_PROFIT",
        risk=0.9,
        day=10,
    )

    assert manager.current() == "SAFE"


def test_endgame():

    manager = StrategyManager()

    manager.update(
        goal="MAKE_PROFIT",
        risk=0.2,
        day=29,
    )

    assert manager.current() == "ENDGAME"


def test_reset():

    manager = StrategyManager()

    manager.update(
        goal="SAVE_MONEY",
        risk=0.2,
        day=4,
    )

    manager.reset()

    assert manager.current() == "BALANCED"