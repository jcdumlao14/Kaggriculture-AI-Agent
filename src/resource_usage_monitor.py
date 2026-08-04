"""
resource_usage_monitor.py

Resource Usage Monitor for the Kaggriculture AI Agent.

Tracks simulated CPU, memory, and disk usage.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceUsageMonitor:
    """
    Tracks system resource usage.
    """

    def __init__(self):
        self.reset()

    # ---------------------------------------------------------

    def update_cpu(
        self,
        percent: float,
    ):
        """
        Update CPU usage.
        """
        self._cpu = percent

    # ---------------------------------------------------------

    def update_memory(
        self,
        percent: float,
    ):
        """
        Update memory usage.
        """
        self._memory = percent

    # ---------------------------------------------------------

    def update_disk(
        self,
        percent: float,
    ):
        """
        Update disk usage.
        """
        self._disk = percent

    # ---------------------------------------------------------

    def usage(self):
        """
        Return current resource usage.
        """
        return {
            "cpu": self._cpu,
            "memory": self._memory,
            "disk": self._disk,
        }

    # ---------------------------------------------------------

    def reset(self):
        """
        Reset all resource metrics.
        """
        self._cpu = 0.0
        self._memory = 0.0
        self._disk = 0.0