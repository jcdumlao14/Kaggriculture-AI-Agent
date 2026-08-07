from src.feature_statistics_engine import (
    FeatureStatisticsEngine,
)


def test_update():

    engine = FeatureStatisticsEngine()

    engine.update(
        {
            "money": 100,
        }
    )

    assert engine.count("money") == 1


def test_mean():

    engine = FeatureStatisticsEngine()

    engine.update(
        {
            "money": 100,
        }
    )

    engine.update(
        {
            "money": 300,
        }
    )

    assert engine.mean("money") == 200.0


def test_empty():

    engine = FeatureStatisticsEngine()

    assert engine.mean("unknown") == 0.0


def test_reset():

    engine = FeatureStatisticsEngine()

    engine.update(
        {
            "money": 100,
        }
    )

    engine.reset()

    assert engine.count("money") == 0


def test_multiple_features():

    engine = FeatureStatisticsEngine()

    engine.update(
        {
            "money": 100,
            "day": 5,
        }
    )

    assert engine.count("money") == 1
    assert engine.count("day") == 1