from src.planning_facade import (
    PlanningFacade,
)


def test_prepare_features():

    facade = PlanningFacade()

    features = facade.prepare_features(
        state_id="a",
        game_state={
            "money": 500,
        },
    )

    assert features["money"] == 500


def test_normalized():

    facade = PlanningFacade()

    features = facade.prepare_features(
        state_id="b",
        game_state={
            "money": 50,
        },
        maximums={
            "money": 100,
        },
    )

    assert features["money"] == 0.5


def test_selected():

    facade = PlanningFacade()

    features = facade.prepare_features(
        state_id="c",
        game_state={
            "money": 100,
            "day": 2,
        },
        selected=["money"],
    )

    assert "money" in features
    assert "day" not in features


def test_cache():

    facade = PlanningFacade()

    first = facade.prepare_features(
        state_id="x",
        game_state={
            "money": 100,
        },
    )

    second = facade.prepare_features(
        state_id="x",
        game_state={
            "money": 999,
        },
    )

    assert first == second


def test_clear_cache():

    facade = PlanningFacade()

    facade.workflow.service.feature_service.features(
        state_id="z",
        game_state={},
    )

    facade.clear_cache()

    assert (
        facade.workflow.service.feature_service.pipeline.cache.size()
        == 0
    )