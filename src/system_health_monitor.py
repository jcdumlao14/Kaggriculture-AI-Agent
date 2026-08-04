"""
system_health_monitor.py

System Health Monitor for the Kaggriculture AI Agent.

Tracks the health status of system services.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class SystemHealthMonitor:
    """
    Tracks service health.
    """

    def __init__(self):
        self._services = {}

    # ---------------------------------------------------------

    def register(
        self,
        service: str,
    ):
        """
        Register a service as healthy.
        """

        self._services[service] = "healthy"

    # ---------------------------------------------------------

    def update(
        self,
        service: str,
        status: str,
    ):
        """
        Update service status.
        """

        if service in self._services:
            self._services[service] = status

    # ---------------------------------------------------------

    def status(
        self,
        service: str,
    ):
        """
        Return service status.
        """

        return self._services.get(service)

    # ---------------------------------------------------------

    def services(self):
        """
        Return a copy of registered services.
        """

        return dict(self._services)

    # ---------------------------------------------------------

    def healthy_count(self) -> int:
        """
        Count healthy services.
        """

        return sum(
            status == "healthy"
            for status in self._services.values()
        )

    # ---------------------------------------------------------

    def is_healthy(
        self,
        service: str,
    ) -> bool:
        """
        Return True if the service is healthy.
        """

        return self.status(service) == "healthy"