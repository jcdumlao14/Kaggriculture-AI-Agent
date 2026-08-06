from src.unified_action_evaluator import (
    UnifiedActionEvaluator,
)


def test_evaluate():

    evaluator = UnifiedActionEvaluator()

    score = evaluator.evaluate(
        "HARVEST",
    )

    assert isinstance(
        score,
        float,
    )


def test_evaluate_details():

    evaluator = UnifiedActionEvaluator()

    details = evaluator.evaluate_details(
        "SELL",
    )

    assert details["action"] == "SELL"
    assert "action_score" in details
    assert "opportunity_score" in details
    assert "risk_score" in details
    assert "final_score" in details


def test_rank_actions():

    evaluator = UnifiedActionEvaluator()

    ranking = evaluator.rank_actions(
        [
            "WATER",
            "PLANT",
            "HARVEST",
        ]
    )

    assert len(ranking) == 3

    assert (
        ranking[0][1]
        >= ranking[1][1]
        >= ranking[2][1]
    )


def test_best_action():

    evaluator = UnifiedActionEvaluator()

    action = evaluator.best_action(
        [
            "WATER",
            "PLANT",
            "HARVEST",
        ]
    )

    assert action == "HARVEST"


def test_empty_actions():

    evaluator = UnifiedActionEvaluator()

    assert (
        evaluator.best_action([])
        is None
    )

def test_learning_bonus():

    evaluator = UnifiedActionEvaluator()

    evaluator.record_outcome(
        "HARVEST",
        100,
    )

    assert (
        evaluator.learned_reward(
            "HARVEST",
        )
        == 100.0
    )


def test_learning_affects_score():

    evaluator = UnifiedActionEvaluator()

    before = evaluator.evaluate(
        "HARVEST",
    )

    evaluator.record_outcome(
        "HARVEST",
        100,
    )

    after = evaluator.evaluate(
        "HARVEST",
    )

    assert after > before