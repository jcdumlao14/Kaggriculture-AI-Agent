from src.strategy_optimizer import StrategyOptimizer


def test_add_strategy():

    optimizer = StrategyOptimizer()

    optimizer.add("Aggressive", 90)

    assert len(optimizer) == 1


def test_best_strategy():

    optimizer = StrategyOptimizer()

    optimizer.add("Balanced", 70)
    optimizer.add("Aggressive", 95)
    optimizer.add("Economic", 80)

    best = optimizer.best()

    assert best["name"] == "Aggressive"


def test_ranking():

    optimizer = StrategyOptimizer()

    optimizer.add("A", 10)
    optimizer.add("B", 30)
    optimizer.add("C", 20)

    ranking = optimizer.ranking()

    assert ranking[0]["score"] == 30


def test_clear():

    optimizer = StrategyOptimizer()

    optimizer.add("A", 20)
    optimizer.clear()

    assert len(optimizer) == 0


def test_empty():

    optimizer = StrategyOptimizer()

    assert optimizer.best() is None