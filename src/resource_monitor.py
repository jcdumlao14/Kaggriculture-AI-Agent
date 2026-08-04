"""
resource_monitor.py

Resource Monitor for the Kaggriculture AI Agent.

Tracks runtime resource usage and custom metrics.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceMonitor:
    """
    Tracks runtime statistics.
    """

    def __init__(self):
        self._execution_count = 0
        self._memory_usage = 0.0
        self._metrics = {}

    # ---------------------------------------------------------

    def increment_execution(self):
        """
        Increment execution count.
        """
        self._execution_count += 1

    # ---------------------------------------------------------

    def execution_count(self) -> int:
        """
        Return execution count.
        """
        return self._execution_count

    # ---------------------------------------------------------

    def set_memory_usage(self, memory_mb: float):
        """
        Store memory usage in MB.
        """
        self._memory_usage = memory_mb

    # ---------------------------------------------------------

    def memory_usage(self) -> float:
        """
        Return memory usage.
        """
        return self._memory_usage

    # ---------------------------------------------------------

    def set_metric(self, name: str, value):
        """
        Store a custom metric.
        """
        self._metrics[name] = value

    # ---------------------------------------------------------

    def get_metric(self, name: str):
        """
        Retrieve a custom metric.
        """
        return self._metrics.get(name)

    # ---------------------------------------------------------

    def summary(self):
        """
        Return monitoring summary.
        """
        return {
            "execution_count": self._execution_count,
            "memory_usage": self._memory_usage,
            "metrics": dict(self._metrics),
        }

    # ---------------------------------------------------------

    def reset(self):
        """
        Reset monitoring data.
        """
        self._execution_count = 0
        self._memory_usage = 0.0
        self._metrics.clear()