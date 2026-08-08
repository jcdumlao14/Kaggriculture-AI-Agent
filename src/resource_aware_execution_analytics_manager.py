"""
resource_aware_execution_analytics_manager.py

Resource-Aware Execution Analytics Manager for the
Kaggriculture AI Agent.

Provides a higher-level interface for analyzing
resource-aware execution history.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.resource_aware_execution_analytics import (
    ResourceAwareExecutionAnalytics,
)
from src.resource_aware_execution_history_manager import (
    ResourceAwareExecutionHistoryManager,
)


class ResourceAwareExecutionAnalyticsManager:
    """
    Manage execution history and analytics.
    """

    def __init__(self):
        self.history = (
            ResourceAwareExecutionHistoryManager()
        )

        self.analytics = (
            ResourceAwareExecutionAnalytics()
        )

    # ---------------------------------------------------------

    def record(
        self,
        *,
        result: dict,
    ) -> dict:
        """
        Record an execution result.
        """

        return self.history.record(
            result=result,
        )

    # ---------------------------------------------------------

    def results(
        self,
    ) -> list[dict]:
        """
        Return all recorded results.
        """

        return self.history.get_all()

    # ---------------------------------------------------------

    def success_count(
        self,
    ) -> int:
        """
        Return the number of successful executions.
        """

        return self.analytics.success_count(
            results=self.results(),
        )

    # ---------------------------------------------------------

    def failure_count(
        self,
    ) -> int:
        """
        Return the number of failed executions.
        """

        return self.analytics.failure_count(
            results=self.results(),
        )

    # ---------------------------------------------------------

    def success_rate(
        self,
    ) -> float:
        """
        Return the historical success rate.
        """

        return self.analytics.success_rate(
            results=self.results(),
        )

    # ---------------------------------------------------------

    def total_tasks(
        self,
    ) -> int:
        """
        Return the total number of planned tasks.
        """

        return self.analytics.total_tasks(
            results=self.results(),
        )

    # ---------------------------------------------------------

    def average_task_count(
        self,
    ) -> float:
        """
        Return the average task count.
        """

        return self.analytics.average_task_count(
            results=self.results(),
        )

    # ---------------------------------------------------------

    def resource_consumption(
        self,
    ) -> dict:
        """
        Return aggregate resource consumption.
        """

        return self.analytics.resource_consumption(
            results=self.results(),
        )

    # ---------------------------------------------------------

    def rejection_reasons(
        self,
    ) -> dict:
        """
        Return rejection reason frequencies.
        """

        return self.analytics.rejection_reasons(
            results=self.results(),
        )

    # ---------------------------------------------------------

    def summary(
        self,
    ) -> dict:
        """
        Return a complete analytics summary.
        """

        return self.analytics.build(
            results=self.results(),
        )

    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clear recorded execution history.
        """

        self.history.clear()