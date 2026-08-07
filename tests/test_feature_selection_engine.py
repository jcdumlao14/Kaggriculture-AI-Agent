from src.feature_selection_engine import (
    FeatureSelectionEngine,
)


def test_select():

    engine = FeatureSelectionEngine()

    features = {
        "money": 1000,
        "day": 5,
        "crop_count": 10,
    }

    selected = engine.select(
        features,
        ["money", "crop_count"],
    )

    assert selected == {
        "money": 1000,
        "crop_count": 10,
    }


def test_remove():

    engine = FeatureSelectionEngine()

    features = {
        "money": 100,
        "day": 5,
    }

    remaining = engine.remove(
        features,
        ["day"],
    )

    assert remaining == {
        "money": 100,
    }


def test_available():

    engine = FeatureSelectionEngine()

    names = engine.available(
        {
            "b": 2,
            "a": 1,
        }
    )

    assert names == ["a", "b"]


def test_unknown_feature():

    engine = FeatureSelectionEngine()

    result = engine.select(
        {"money": 100},
        ["profit"],
    )

    assert result == {}


def test_remove_unknown():

    engine = FeatureSelectionEngine()

    features = {
        "money": 100,
    }

    result = engine.remove(
        features,
        ["profit"],
    )

    assert result == features