from src.metrics_registry import MetricsRegistry


def test_register():

    registry = MetricsRegistry()

    registry.register("reward")

    assert registry.get("reward") == 0


def test_set():

    registry = MetricsRegistry()

    registry.register("accuracy")

    registry.set("accuracy", 0.95)

    assert registry.get("accuracy") == 0.95


def test_export():

    registry = MetricsRegistry()

    registry.register("loss", 1.2)

    metrics = registry.export()

    assert metrics["loss"] == 1.2


def test_reset():

    registry = MetricsRegistry()

    registry.register("episodes")

    registry.reset()

    assert registry.export() == {}


def test_missing_metric():

    registry = MetricsRegistry()

    assert registry.get("unknown") is None