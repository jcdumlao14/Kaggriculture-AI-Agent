from src.opening_optimizer import OpeningOptimizer


def test_record():

    opt = OpeningOptimizer()

    opt.record("PLANT_WHEAT", 100)

    assert opt.move_count("PLANT_WHEAT") == 1


def test_average():

    opt = OpeningOptimizer()

    opt.record("PLANT_WHEAT", 100)
    opt.record("PLANT_WHEAT", 200)

    assert opt.average("PLANT_WHEAT") == 150


def test_best_move():

    opt = OpeningOptimizer()

    opt.record("A", 10)
    opt.record("B", 50)
    opt.record("C", 20)

    assert opt.best_move() == "B"


def test_unknown_average():

    opt = OpeningOptimizer()

    assert opt.average("UNKNOWN") == 0


def test_reset():

    opt = OpeningOptimizer()

    opt.record("A", 10)

    opt.reset()

    assert opt.best_move() is None
    