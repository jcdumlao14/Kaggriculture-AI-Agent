from src.resource_usage_monitor import (
    ResourceUsageMonitor,
)


def test_update_cpu():

    monitor = ResourceUsageMonitor()

    monitor.update_cpu(42.5)

    assert monitor.usage()["cpu"] == 42.5


def test_update_memory():

    monitor = ResourceUsageMonitor()

    monitor.update_memory(61.2)

    assert monitor.usage()["memory"] == 61.2


def test_update_disk():

    monitor = ResourceUsageMonitor()

    monitor.update_disk(75.8)

    assert monitor.usage()["disk"] == 75.8


def test_usage():

    monitor = ResourceUsageMonitor()

    monitor.update_cpu(10)
    monitor.update_memory(20)
    monitor.update_disk(30)

    usage = monitor.usage()

    assert usage == {
        "cpu": 10,
        "memory": 20,
        "disk": 30,
    }


def test_reset():

    monitor = ResourceUsageMonitor()

    monitor.update_cpu(80)
    monitor.update_memory(70)
    monitor.update_disk(60)

    monitor.reset()

    assert monitor.usage() == {
        "cpu": 0.0,
        "memory": 0.0,
        "disk": 0.0,
    }