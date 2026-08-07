from src.learning_feature_service import (
    LearningFeatureService,
)


def test_features():

    service = LearningFeatureService()

    features = service.features(
        state_id="a",
        game_state={
            "money": 500,
        },
    )

    assert features["money"] == 500


def test_normalized():

    service = LearningFeatureService()

    features = service.features(
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

    service = LearningFeatureService()

    features = service.features(
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

    service = LearningFeatureService()

    first = service.features(
        state_id="x",
        game_state={
            "money": 100,
        },
    )

    second = service.features(
        state_id="x",
        game_state={
            "money": 999,
        },
    )

    assert first == second


def test_clear():

    service = LearningFeatureService()

    service.features(
        state_id="y",
        game_state={},
    )

    service.clear_cache()

    assert (
        service.pipeline.cache.size()
        == 0
    )