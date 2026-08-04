from src.search_engine import SearchEngine


def test_add_move():

    engine = SearchEngine()

    engine.add_move("PLANT", 120)

    assert len(engine) == 1


def test_best_move():

    engine = SearchEngine()

    engine.add_move("WATER", 100)
    engine.add_move("HARVEST", 250)
    engine.add_move("PLANT", 150)

    best = engine.best_move()

    assert best["action"] == "HARVEST"


def test_ranking():

    engine = SearchEngine()

    engine.add_move("A", 10)
    engine.add_move("B", 30)
    engine.add_move("C", 20)

    ranking = engine.ranking()

    assert ranking[0]["score"] == 30


def test_clear():

    engine = SearchEngine()

    engine.add_move("PLANT", 100)

    engine.clear()

    assert len(engine) == 0


def test_empty():

    engine = SearchEngine()

    assert engine.best_move() is None