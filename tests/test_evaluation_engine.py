from src.evaluation_engine import EvaluationEngine


def test_add_score():

    engine = EvaluationEngine()

    engine.add_score(100)

    assert engine.scores() == [100]


def test_average_score():

    engine = EvaluationEngine()

    engine.add_score(100)
    engine.add_score(200)
    engine.add_score(300)

    assert engine.average_score() == 200


def test_best_score():

    engine = EvaluationEngine()

    engine.add_score(50)
    engine.add_score(150)

    assert engine.best_score() == 150


def test_summary():

    engine = EvaluationEngine()

    engine.add_score(80)
    engine.add_score(120)

    summary = engine.summary()

    assert summary["count"] == 2
    assert summary["average"] == 100
    assert summary["best"] == 120


def test_reset():

    engine = EvaluationEngine()

    engine.add_score(100)

    engine.reset()

    assert engine.scores() == []
    