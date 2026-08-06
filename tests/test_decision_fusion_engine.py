from src.decision_fusion_engine import (
    DecisionFusionEngine,
)


def test_fuse():

    engine = DecisionFusionEngine()

    score = engine.fuse(
        action_score=50,
        opportunity_score=30,
        market_score=10,
        strategy_score=20,
        risk_score=15,
    )

    assert score == 95


def test_better():

    engine = DecisionFusionEngine()

    assert engine.better(
        90,
        80,
    )


def test_normalize():

    engine = DecisionFusionEngine()

    assert (
        engine.normalize(200)
        == 100
    )


def test_rank():

    engine = DecisionFusionEngine()

    ranking = engine.rank(
        {
            "A": 50,
            "B": 80,
            "C": 20,
        }
    )

    assert ranking[0][0] == "B"


def test_best():

    engine = DecisionFusionEngine()

    action = engine.best(
        {
            "SELL": 80,
            "HARVEST": 120,
        }
    )

    assert action == "HARVEST"