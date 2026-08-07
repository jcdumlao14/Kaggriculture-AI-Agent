from src.planning_service_coordinator import (
    PlanningServiceCoordinator,
)


def test_prepare_features():

    service = PlanningServiceCoordinator()

    features = service.prepare_features(
        state_id="a",
        game_state={
            "money": 500,
        },
    )

    assert features["money"] == 500


def test_normalized():

    service = PlanningServiceCoordinator()

    features = service.prepare_features(
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

    service = PlanningServiceCoordinator()

    features = service.prepare_features(
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

    service = PlanningServiceCoordinator()

    first = service.prepare_features(
        state_id="x",
        game_state={
            "money": 100,
        },
    )

    second = service.prepare_features(
        state_id="x",
        game_state={
            "money": 999,
        },
    )

    assert first == second


def test_clear_cache():

    service = PlanningServiceCoordinator()

    service.prepare_features(
        state_id="z",
        game_state={},
    )

    service.clear_cache()

    assert (
        service.feature_service.pipeline.cache.size()
        == 0
    )