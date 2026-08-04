from src.resource_monitor import ResourceMonitor


def test_execution_count():

    monitor = ResourceMonitor()

    monitor.increment_execution()
    monitor.increment_execution()

    assert monitor.execution_count() == 2


def test_memory_usage():

    monitor = ResourceMonitor()

    monitor.set_memory_usage(256.5)

    assert monitor.memory_usage() == 256.5


def test_custom_metric():

    monitor = ResourceMonitor()

    monitor.set_metric("cpu_usage", 75)

    assert monitor.get_metric("cpu_usage") == 75


def test_summary():

    monitor = ResourceMonitor()

    monitor.increment_execution()
    monitor.set_memory_usage(128)

    summary = monitor.summary()

    assert summary["execution_count"] == 1
    assert summary["memory_usage"] == 128


def test_reset():

    monitor = ResourceMonitor()

    monitor.increment_execution()
    monitor.set_memory_usage(512)
    monitor.set_metric("gpu_usage", 90)

    monitor.reset()

    assert monitor.execution_count() == 0
    assert monitor.memory_usage() == 0.0
    assert monitor.summary()["metrics"] == {}