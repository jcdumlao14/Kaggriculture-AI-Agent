from src.utility_engine import UtilityEngine


def test_score_returns_number():

    utility = UtilityEngine()

    score = utility.score(
        profit=80,
        season=70,
        inventory=50,
        money=60,
        goal=90,
        opponent=40,
        risk=20,
    )

    assert isinstance(score, float)


def test_better():

    utility = UtilityEngine()

    assert utility.better(20, 10)


def test_best_action():

    utility = UtilityEngine()

    actions = [
        ("PLANT", 45.2),
        ("HARVEST", 81.5),
        ("SELL", 60.1),
    ]

    best = utility.best(actions)

    assert best[0] == "HARVEST"


def test_normalize():

    utility = UtilityEngine()

    assert utility.normalize(50, 100) == 0.5


def test_summary():

    utility = UtilityEngine()

    assert "profit" in utility.summary()