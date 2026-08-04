"""
metrics_registry.py

Metrics Registry for the Kaggriculture AI Agent.

Stores runtime metrics for monitoring and analysis.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class MetricsRegistry:
    """
    Central registry for runtime metrics.
    """

    def __init__(self):
        self._metrics = {}

    # ---------------------------------------------------------

    def register(self, name: str, initial_value=0):
        """
        Register a new metric.
        """
        self._metrics[name] = initial_value

    # ---------------------------------------------------------

    def set(self, name: str, value):
        """
        Set a metric value.
        """
        self._metrics[name] = value

    # ---------------------------------------------------------

    def get(self, name: str):
        """
        Retrieve a metric value.
        """
        return self._metrics.get(name)

    # ---------------------------------------------------------

    def export(self):
        """
        Return a copy of all metrics.
        """
        return dict(self._metrics)

    # ---------------------------------------------------------

    def reset(self):
        """
        Remove every metric.
        """
        self._metrics.clear()