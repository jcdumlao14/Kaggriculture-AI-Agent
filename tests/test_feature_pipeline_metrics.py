from src.feature_pipeline_metrics import (
    FeaturePipelineMetrics,
)


def test_processed():

    metrics = FeaturePipelineMetrics()

    metrics.record_processed()

    assert metrics.processed == 1


def test_cache_hit():

    metrics = FeaturePipelineMetrics()

    metrics.record_processed()
    metrics.record_cache_hit()

    assert metrics.cache_hits == 1


def test_hit_rate():

    metrics = FeaturePipelineMetrics()

    for _ in range(4):
        metrics.record_processed()

    metrics.record_cache_hit()
    metrics.record_cache_hit()

    assert metrics.cache_hit_rate() == 0.5


def test_validation():

    metrics = FeaturePipelineMetrics()

    metrics.record_validation_failure()

    assert metrics.validation_failures == 1


def test_reset():

    metrics = FeaturePipelineMetrics()

    metrics.record_processed()
    metrics.record_cache_hit()

    metrics.reset()

    assert metrics.processed == 0
    assert metrics.cache_hits == 0