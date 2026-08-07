from src.feature_drift_engine import (
    FeatureDriftEngine,
)


def test_difference():

    engine = FeatureDriftEngine()

    diff = engine.difference(
        {"money": 100},
        {"money": 150},
    )

    assert diff["money"] == 50


def test_score():

    engine = FeatureDriftEngine()

    score = engine.drift_score(
        {"a": 1},
        {"a": 3},
    )

    assert score == 2


def test_has_drift():

    engine = FeatureDriftEngine()

    assert engine.has_drift(
        {"a": 1},
        {"a": 5},
        threshold=3,
    )


def test_no_drift():

    engine = FeatureDriftEngine()

    assert not engine.has_drift(
        {"a": 1},
        {"a": 1},
    )


def test_missing_features():

    engine = FeatureDriftEngine()

    diff = engine.difference(
        {},
        {"money": 10},
    )

    assert diff["money"] == 10