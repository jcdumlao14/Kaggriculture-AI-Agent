from src.feature_pipeline_coordinator import (
    FeaturePipelineCoordinator,
)


def test_process():

    engine = FeaturePipelineCoordinator()

    features = engine.process(
        state_id="a",
        game_state={
            "money": 100,
        },
    )

    assert features["money"] == 100


def test_cache():

    engine = FeaturePipelineCoordinator()

    engine.process(
        state_id="x",
        game_state={"money": 10},
    )

    engine.process(
        state_id="x",
        game_state={"money": 999},
    )

    assert (
        engine.cache.retrieve("x")["money"]
        == 10
    )


def test_normalize():

    engine = FeaturePipelineCoordinator()

    features = engine.process(
        state_id="n",
        game_state={"money": 50},
        maximums={"money": 100},
    )

    assert features["money"] == 0.5


def test_select():

    engine = FeaturePipelineCoordinator()

    features = engine.process(
        state_id="b",
        game_state={
            "money": 10,
            "day": 3,
        },
        selected=["money"],
    )

    assert "money" in features
    assert "day" not in features


def test_clear_cache():

    engine = FeaturePipelineCoordinator()

    engine.process(
        state_id="z",
        game_state={},
    )

    engine.clear_cache()

    assert engine.cache.size() == 0