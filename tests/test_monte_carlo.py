from src.monte_carlo import MonteCarlo


def test_add():

    mc = MonteCarlo()

    mc.add("Aggressive", 100)

    assert len(mc) == 1


def test_average():

    mc = MonteCarlo()

    mc.add("A", 100)
    mc.add("A", 200)

    assert mc.average("A") == 150


def test_best():

    mc = MonteCarlo()

    mc.add("A", 100)
    mc.add("A", 120)

    mc.add("B", 200)
    mc.add("B", 220)

    assert mc.best() == "B"


def test_clear():

    mc = MonteCarlo()

    mc.add("A", 10)

    mc.clear()

    assert len(mc) == 0


def test_unknown_average():

    mc = MonteCarlo()

    assert mc.average("UNKNOWN") == 0.0
    