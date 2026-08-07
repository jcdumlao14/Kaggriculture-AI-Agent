from src.feature_normalization_engine import (
    FeatureNormalizationEngine,
)


def test_normalize():

    engine = FeatureNormalizationEngine()

    values = engine.normalize(
        {
            "money": 500,
            "day": 5,
        },
        {
            "money": 1000,
            "day": 10,
        },
    )

    assert values["money"] == 0.5
    assert values["day"] == 0.5


def test_clip():

    engine = FeatureNormalizationEngine()

    assert engine.clip(2.5) == 1.0


def test_clip_negative():

    engine = FeatureNormalizationEngine()

    assert engine.clip(-1.0) == 0.0


def test_vector():

    engine = FeatureNormalizationEngine()

    values = engine.normalize_vector(
        [5, 20],
        [10, 40],
    )

    assert values == [0.5, 0.5]


def test_zero_maximum():

    engine = FeatureNormalizationEngine()

    values = engine.normalize(
        {"money": 10},
        {"money": 0},
    )

    assert values["money"] == 0.0