from src.action_scoring_engine import (
    ActionScoringEngine,
)


def test_score():

    engine = ActionScoringEngine()

    score = engine.score(
        action="HARVEST",
        farm_score=100,
        crop_profit=80,
        animal_profit=20,
        market_score=10,
    )

    assert score == 260


def test_bonus():

    engine = ActionScoringEngine()

    assert engine.action_bonus(
        "PLANT",
    ) == 25


def test_supported():

    engine = ActionScoringEngine()

    assert engine.is_supported(
        "SELL",
    )


def test_unknown_action():

    engine = ActionScoringEngine()

    assert not engine.is_supported(
        "UNKNOWN",
    )


def test_supported_actions():

    engine = ActionScoringEngine()

    actions = engine.supported_actions()

    assert "HARVEST" in actions
    assert "PLANT" in actions