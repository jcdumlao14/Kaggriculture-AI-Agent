from src.search_feature_service import (
    SearchFeatureService,
)


def test_features():

    service = SearchFeatureService()

    features = service.features(
        state_id="a",
        game_state={
            "money": 500,
        },
    )

    assert features["money"] == 500


def test_normalized():

    service = SearchFeatureService()

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

    service = SearchFeatureService()

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

    service = SearchFeatureService()

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

    service = SearchFeatureService()

    service.features(
        state_id="y",
        game_state={},
    )

    service.clear_cache()

    assert (
        service.pipeline.cache.size()
        == 0
    )