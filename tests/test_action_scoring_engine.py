from src.action_scoring_engine import (
    ActionScoringEngine,
)

def test_sell_bonus_from_market():

    engine = ActionScoringEngine()

    game_state = {
        "market": {
            "prices": {
                "TOMATO": 200,
                "MELON": 300,
            }
        }
    }

    score = engine.score(
        action="SELL",
        game_state=game_state,
    )

    assert score == 50.0


def test_harvest_bonus():

    engine = ActionScoringEngine()

    game_state = {
        "market": {
            "prices": {
                "MELON": 300,
            }
        }
    }

    score = engine.score(
        action="HARVEST",
        game_state=game_state,
    )

    assert score == 65.0


def test_buy_seed_penalty():

    engine = ActionScoringEngine()

    game_state = {
        "market": {
            "prices": {
                "MELON": 300,
            }
        }
    }

    score = engine.score(
        action="BUY_SEED",
        game_state=game_state,
    )

    assert score == -2.5


def test_without_game_state():

    engine = ActionScoringEngine()

    score = engine.score(
        action="SELL",
    )

    assert score == 20.0


def test_unknown_action_score():

    engine = ActionScoringEngine()

    score = engine.score(
        action="UNKNOWN",
    )

    assert score == 0.0