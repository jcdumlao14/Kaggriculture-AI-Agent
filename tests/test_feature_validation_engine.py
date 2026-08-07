from src.feature_validation_engine import (
    FeatureValidationEngine,
)


def test_valid():

    engine = FeatureValidationEngine()

    assert engine.valid(
        {
            "money": 100,
            "day": 2,
        }
    )


def test_nan():

    engine = FeatureValidationEngine()

    assert not engine.valid(
        {
            "money": float("nan"),
        }
    )


def test_inf():

    engine = FeatureValidationEngine()

    assert not engine.valid(
        {
            "money": float("inf"),
        }
    )


def test_type():

    engine = FeatureValidationEngine()

    assert not engine.valid(
        {
            "money": "abc",
        }
    )


def test_sanitize():

    engine = FeatureValidationEngine()

    result = engine.sanitize(
        {
            "money": float("nan"),
            "day": 3,
        }
    )

    assert result["money"] == 0.0
    assert result["day"] == 3.0