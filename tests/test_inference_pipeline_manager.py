from src.inference_pipeline_manager import (
    InferencePipelineManager,
)

from src.prediction_cache_manager import (
    PredictionCacheManager,
)


def dummy_model(payload):

    return payload["money"] * 2


def test_validate():

    pipeline = InferencePipelineManager()

    assert pipeline.validate(
        {"money": 100}
    )


def test_lookup_cache():

    pipeline = InferencePipelineManager()

    cache = PredictionCacheManager()

    cache.put(
        "key",
        {"prediction": 200},
    )

    result = pipeline.lookup_cache(
        cache,
        "key",
    )

    assert result["prediction"] == 200


def test_infer():

    pipeline = InferencePipelineManager()

    result = pipeline.infer(
        dummy_model,
        {"money": 100},
    )

    assert result == 200


def test_postprocess():

    pipeline = InferencePipelineManager()

    result = pipeline.postprocess(
        250,
    )

    assert result["prediction"] == 250


def test_run():

    pipeline = InferencePipelineManager()

    result = pipeline.run(
        {"money": 75},
        dummy_model,
    )

    assert result["prediction"] == 150