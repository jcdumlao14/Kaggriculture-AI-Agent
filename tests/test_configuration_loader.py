from pathlib import Path

from src.configuration_loader import ConfigurationLoader


def test_set_get():

    loader = ConfigurationLoader()

    loader.set("learning_rate", 0.1)

    assert loader.get("learning_rate") == 0.1


def test_default():

    loader = ConfigurationLoader()

    assert loader.get("unknown", 42) == 42


def test_save_load(tmp_path):

    loader = ConfigurationLoader()

    loader.set("gamma", 0.95)
    loader.set("epsilon", 0.2)

    filename = tmp_path / "config.json"

    loader.save(filename)

    new_loader = ConfigurationLoader()
    new_loader.load(filename)

    assert new_loader.get("gamma") == 0.95
    assert new_loader.get("epsilon") == 0.2


def test_all():

    loader = ConfigurationLoader()

    loader.set("a", 1)
    loader.set("b", 2)

    config = loader.all()

    assert len(config) == 2


def test_reset():

    loader = ConfigurationLoader()

    loader.set("learning_rate", 0.1)

    loader.reset()

    assert loader.all() == {}