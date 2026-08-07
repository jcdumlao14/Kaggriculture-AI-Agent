from src.feature_version_manager import (
    FeatureVersionManager,
)


def test_initial_version():

    engine = FeatureVersionManager()

    assert engine.current() == 1


def test_increment():

    engine = FeatureVersionManager()

    engine.increment()

    assert engine.current() == 2


def test_history():

    engine = FeatureVersionManager()

    engine.increment()
    engine.increment()

    assert engine.history() == [1, 2, 3]


def test_reset():

    engine = FeatureVersionManager()

    engine.increment()
    engine.reset()

    assert engine.current() == 1


def test_history_after_reset():

    engine = FeatureVersionManager()

    engine.increment()
    engine.reset()

    assert engine.history() == [1]