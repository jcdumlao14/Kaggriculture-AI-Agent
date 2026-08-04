from src.system_health_monitor import (
    SystemHealthMonitor,
)


def test_register():

    monitor = SystemHealthMonitor()

    monitor.register("Serving")

    assert monitor.is_healthy("Serving")


def test_update():

    monitor = SystemHealthMonitor()

    monitor.register("Serving")

    monitor.update(
        "Serving",
        "degraded",
    )

    assert monitor.status("Serving") == "degraded"


def test_status():

    monitor = SystemHealthMonitor()

    monitor.register("Cache")

    assert monitor.status("Cache") == "healthy"


def test_services():

    monitor = SystemHealthMonitor()

    monitor.register("Serving")
    monitor.register("Router")

    services = monitor.services()

    assert len(services) == 2


def test_healthy_count():

    monitor = SystemHealthMonitor()

    monitor.register("Serving")
    monitor.register("Router")

    monitor.update(
        "Router",
        "offline",
    )

    assert monitor.healthy_count() == 1