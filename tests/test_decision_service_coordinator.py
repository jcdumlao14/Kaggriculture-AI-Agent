from src.decision_service_coordinator import (
    DecisionServiceCoordinator,
)


def test_evaluate():

    engine = DecisionServiceCoordinator()

    score = engine.evaluate(
        state_id="a",
        game_state={
            "money": 500,
        },
        action="MOVE",
    )

    assert isinstance(score, float)


def test_normalized():

    engine = DecisionServiceCoordinator()

    score = engine.evaluate(
        state_id="b",
        game_state={
            "money": 50,
        },
        maximums={
            "money": 100,
        },
        action="MOVE",
    )

    assert isinstance(score, float)


def test_selected():

    engine = DecisionServiceCoordinator()

    score = engine.evaluate(
        state_id="c",
        game_state={
            "money": 100,
            "day": 2,
        },
        selected=["money"],
        action="MOVE",
    )

    assert isinstance(score, float)


def test_clear():

    engine = DecisionServiceCoordinator()

    engine.feature_service.features(
        state_id="x",
        game_state={},
    )

    engine.clear_cache()

    assert (
        engine.feature_service.pipeline.cache.size()
        == 0
    )


def test_multiple_actions():

    engine = DecisionServiceCoordinator()

    score1 = engine.evaluate(
        state_id="d",
        game_state={},
        action="MOVE",
    )

    score2 = engine.evaluate(
        state_id="d",
        game_state={},
        action="WAIT",
    )

    assert isinstance(score1, float)
    assert isinstance(score2, float)