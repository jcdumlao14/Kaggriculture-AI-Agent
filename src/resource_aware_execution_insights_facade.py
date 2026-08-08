"""
resource_aware_execution_insights_facade.py

Resource-Aware Execution Insights Facade for the
Kaggriculture AI Agent.

Provides a simple public interface for recording
and inspecting resource-aware execution insights.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.resource_aware_execution_insights import (
    ResourceAwareExecutionInsights,
)


class ResourceAwareExecutionInsightsFacade:
    """
    Public facade for resource-aware execution insights.
    """

    def __init__(self):
        self.insights = (
            ResourceAwareExecutionInsights()
        )

    # ---------------------------------------------------------

    def record(
        self,
        *,
        analytics: dict,
    ) -> dict:
        """
        Record execution analytics.
        """

        return self.insights.record(
            analytics=analytics,
        )

    # ---------------------------------------------------------

    def current(
        self,
    ) -> dict | None:
        """
        Return the current execution snapshot.
        """

        return self.insights.current()

    # ---------------------------------------------------------

    def previous(
        self,
    ) -> dict | None:
        """
        Return the previous execution snapshot.
        """

        return self.insights.previous()

    # ---------------------------------------------------------

    def comparison(
        self,
    ) -> dict | None:
        """
        Return the comparison between snapshots.
        """

        return self.insights.comparison()

    # ---------------------------------------------------------

    def trend(
        self,
    ) -> dict | None:
        """
        Return the current execution trend.
        """

        return self.insights.trend()

    # ---------------------------------------------------------

    def performance(
        self,
    ) -> str:
        """
        Return the current performance classification.
        """

        return self.insights.performance()

    # ---------------------------------------------------------

    def success_rate_change(
        self,
    ) -> float:
        """
        Return the success-rate change.
        """

        return self.insights.success_rate_change()

    # ---------------------------------------------------------

    def ready(
        self,
    ) -> bool:
        """
        Return whether enough snapshots exist
        for comparison.
        """

        return self.insights.ready_for_comparison()

    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clear stored execution insights.
        """

        self.insights.clear()