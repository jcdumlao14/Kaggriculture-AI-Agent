from src.alpha_beta import AlphaBeta


def test_maximize():

    engine = AlphaBeta()

    assert engine.maximize([10, 40, 20]) == 40


def test_minimize():

    engine = AlphaBeta()

    assert engine.minimize([10, 40, 20]) == 10


def test_choose_max():

    engine = AlphaBeta()

    assert engine.choose([5, 8, 2], True) == 8


def test_choose_min():

    engine = AlphaBeta()

    assert engine.choose([5, 8, 2], False) == 2


def test_empty():

    engine = AlphaBeta()

    assert engine.choose([], True) == 0.0
    