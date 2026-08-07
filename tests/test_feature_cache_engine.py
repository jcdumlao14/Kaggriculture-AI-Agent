from src.feature_cache_engine import (
    FeatureCacheEngine,
)


def test_store():

    engine = FeatureCacheEngine()

    engine.store(
        "state1",
        {"money": 100},
    )

    assert engine.contains("state1")


def test_retrieve():

    engine = FeatureCacheEngine()

    engine.store(
        "state1",
        {"money": 500},
    )

    features = engine.retrieve("state1")

    assert features["money"] == 500


def test_missing():

    engine = FeatureCacheEngine()

    assert engine.retrieve("unknown") is None


def test_clear():

    engine = FeatureCacheEngine()

    engine.store(
        "state1",
        {"money": 100},
    )

    engine.clear()

    assert engine.size() == 0


def test_size():

    engine = FeatureCacheEngine()

    engine.store("a", {})
    engine.store("b", {})

    assert engine.size() == 2