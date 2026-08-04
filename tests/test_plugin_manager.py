from src.plugin_manager import PluginManager


class DummyPlugin:
    pass


def test_register():

    manager = PluginManager()

    plugin = DummyPlugin()

    manager.register("dummy", plugin)

    assert manager.exists("dummy")


def test_get():

    manager = PluginManager()

    plugin = DummyPlugin()

    manager.register("dummy", plugin)

    assert manager.get("dummy") is plugin


def test_unregister():

    manager = PluginManager()

    manager.register("dummy", DummyPlugin())

    manager.unregister("dummy")

    assert not manager.exists("dummy")


def test_list_plugins():

    manager = PluginManager()

    manager.register("planner", DummyPlugin())
    manager.register("strategy", DummyPlugin())

    assert manager.list_plugins() == [
        "planner",
        "strategy",
    ]


def test_clear():

    manager = PluginManager()

    manager.register("dummy", DummyPlugin())

    manager.clear()

    assert manager.list_plugins() == []