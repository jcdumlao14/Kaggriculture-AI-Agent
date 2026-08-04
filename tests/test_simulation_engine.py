from src.simulation_engine import SimulationEngine


def test_add_simulation():

    engine = SimulationEngine()

    engine.simulate("Aggressive", 120)

    assert len(engine) == 1


def test_best_result():

    engine = SimulationEngine()

    engine.simulate("Balanced", 90)
    engine.simulate("Aggressive", 130)
    engine.simulate("Economic", 110)

    best = engine.best()

    assert best["strategy"] == "Aggressive"


def test_ranking():

    engine = SimulationEngine()

    engine.simulate("A", 10)
    engine.simulate("B", 40)
    engine.simulate("C", 20)

    ranking = engine.ranking()

    assert ranking[0]["reward"] == 40


def test_clear():

    engine = SimulationEngine()

    engine.simulate("A", 100)

    engine.clear()

    assert len(engine) == 0


def test_empty():

    engine = SimulationEngine()

    assert engine.best() is None