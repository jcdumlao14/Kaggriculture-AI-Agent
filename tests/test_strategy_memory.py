from src.strategy_memory import StrategyMemory


def test_record():

    memory = StrategyMemory()

    memory.record("EARLY_EXPANSION")

    assert memory.count() == 1


def test_last():

    memory = StrategyMemory()

    memory.record("HARVEST")

    assert memory.last() == "HARVEST"


def test_history():

    memory = StrategyMemory()

    memory.record("PLANT")

    memory.record("SELL")

    assert len(memory.history()) == 2


def test_clear():

    memory = StrategyMemory()

    memory.record("BUY")

    memory.clear()

    assert memory.count() == 0


def test_empty():

    memory = StrategyMemory()

    assert memory.last() is None