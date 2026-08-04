from src.configuration_manager import (
    ConfigurationManager,
)


def test_set_get():

    manager = ConfigurationManager()

    manager.set(
        "host",
        "localhost",
    )

    assert manager.get("host") == "localhost"


def test_update():

    manager = ConfigurationManager()

    manager.update(
        {
            "host": "localhost",
            "port": 8000,
        }
    )

    assert manager.get("port") == 8000


def test_remove():

    manager = ConfigurationManager()

    manager.set(
        "debug",
        True,
    )

    manager.remove("debug")

    assert not manager.exists("debug")


def test_count():

    manager = ConfigurationManager()

    manager.set("a", 1)
    manager.set("b", 2)

    assert manager.count() == 2


def test_reset():

    manager = ConfigurationManager()

    manager.set("host", "localhost")

    manager.reset()

    assert manager.count() == 0