from src.decision_explanation_engine import (
    DecisionExplanationEngine,
)


def make_explanation(
    action,
    score,
):
    engine = DecisionExplanationEngine()

    return engine.explain(
        action=action,
        action_score=20,
        opportunity_score=30,
        risk_score=5,
        market_score=10,
        strategy_score=15,
        final_score=score,
    )


def test_explain():

    engine = DecisionExplanationEngine()

    explanation = engine.explain(
        action="HARVEST",
        action_score=20,
        opportunity_score=30,
        risk_score=5,
        market_score=10,
        strategy_score=15,
        final_score=70,
    )

    assert explanation["action"] == "HARVEST"


def test_summary():

    engine = DecisionExplanationEngine()

    explanation = make_explanation(
        "SELL",
        80,
    )

    assert "SELL" in engine.summary(explanation)


def test_best():

    engine = DecisionExplanationEngine()

    best = engine.best_action(
        [
            make_explanation("A", 50),
            make_explanation("B", 90),
        ]
    )

    assert best["action"] == "B"


def test_average():

    engine = DecisionExplanationEngine()

    average = engine.average_score(
        [
            make_explanation("A", 50),
            make_explanation("B", 70),
        ]
    )

    assert average == 60.0


def test_compare():

    engine = DecisionExplanationEngine()

    first = make_explanation("A", 80)

    second = make_explanation("B", 60)

    assert engine.compare(
        first,
        second,
    ) == 20