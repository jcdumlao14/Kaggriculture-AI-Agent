"""
resource_aware_execution_insights.py

Resource-Aware Execution Insights for the
Kaggriculture AI Agent.

Provides one high-level interface for creating
execution snapshots and retrieving comparisons
and trends.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.resource_aware_snapshot_trend_manager import (
    ResourceAwareSnapshotTrendManager,
)


class ResourceAwareExecutionInsights:
    """
    High-level interface for resource-aware execution
    snapshot and trend analysis.
    """

    def __init__(self):
        self.manager = (
            ResourceAwareSnapshotTrendManager()
        )

    # ---------------------------------------------------------

    def record(
        self,
        *,
        analytics: dict,
    ) -> dict:
        """
        Record a new execution analytics snapshot.
        """

        return self.manager.create_snapshot(
            analytics=analytics,
        )

    # ---------------------------------------------------------

    def current(
        self,
    ) -> dict | None:
        """
        Return the current snapshot.
        """

        return self.manager.current()

    # ---------------------------------------------------------

    def previous(
        self,
    ) -> dict | None:
        """
        Return the previous snapshot.
        """

        return self.manager.previous()

    # ---------------------------------------------------------

    def comparison(
        self,
    ) -> dict | None:
        """
        Return the comparison between the current
        and previous snapshots.
        """

        return self.manager.comparison()

    # ---------------------------------------------------------

    def trend(
        self,
    ) -> dict | None:
        """
        Return the current execution trend.
        """

        return self.manager.trend()

    # ---------------------------------------------------------

    def performance(
        self,
    ) -> str:
        """
        Return the current performance classification.
        """

        return self.manager.performance()

    # ---------------------------------------------------------

    def success_rate_change(
        self,
    ) -> float:
        """
        Return the change in success rate.
        """

        return self.manager.success_rate_change()

    # ---------------------------------------------------------

    def ready_for_comparison(
        self,
    ) -> bool:
        """
        Return True when two snapshots are available
        for comparison.
        """

        return self.manager.can_analyze()

    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clear all stored execution insights.
        """

        self.manager.clear()