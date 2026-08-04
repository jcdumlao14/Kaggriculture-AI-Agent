from src.minimax import Minimax


def test_maximize():

    engine = Minimax()

    assert engine.maximize([10, 20, 5]) == 20


def test_minimize():

    engine = Minimax()

    assert engine.minimize([10, 20, 5]) == 5


def test_choose_max():

    engine = Minimax()

    assert engine.choose([3, 8, 2], True) == 8


def test_choose_min():

    engine = Minimax()

    assert engine.choose([3, 8, 2], False) == 2


def test_empty():

    engine = Minimax()

    assert engine.choose([], True) == 0.0