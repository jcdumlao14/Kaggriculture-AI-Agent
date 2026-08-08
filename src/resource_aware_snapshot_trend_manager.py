"""
resource_aware_snapshot_trend_manager.py

Resource-Aware Snapshot Trend Manager for the
Kaggriculture AI Agent.

Coordinates snapshot comparison and trend analysis.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.resource_aware_snapshot_comparison_manager import (
    ResourceAwareSnapshotComparisonManager,
)
from src.resource_aware_snapshot_trend_analyzer import (
    ResourceAwareSnapshotTrendAnalyzer,
)


class ResourceAwareSnapshotTrendManager:
    """
    Manage execution snapshot trends.
    """

    def __init__(self):
        self.comparisons = (
            ResourceAwareSnapshotComparisonManager()
        )

        self.analyzer = (
            ResourceAwareSnapshotTrendAnalyzer()
        )

    # ---------------------------------------------------------

    def create_snapshot(
        self,
        *,
        analytics: dict,
    ) -> dict:
        """
        Create a new analytics snapshot.
        """

        return self.comparisons.create_snapshot(
            analytics=analytics,
        )

    # ---------------------------------------------------------

    def current(
        self,
    ) -> dict | None:
        """
        Return the current snapshot.
        """

        return self.comparisons.current()

    # ---------------------------------------------------------

    def previous(
        self,
    ) -> dict | None:
        """
        Return the previous snapshot.
        """

        return self.comparisons.previous()

    # ---------------------------------------------------------

    def can_analyze(
        self,
    ) -> bool:
        """
        Return True when enough snapshots exist
        for trend analysis.
        """

        return self.comparisons.can_compare()

    # ---------------------------------------------------------

    def comparison(
        self,
    ) -> dict | None:
        """
        Return the current snapshot comparison.
        """

        return self.comparisons.compare()

    # ---------------------------------------------------------

    def trend(
        self,
    ) -> dict | None:
        """
        Return the current trend analysis.

        Returns None when there is no previous
        snapshot to compare against.
        """

        comparison = self.comparison()

        if comparison is None:
            return None

        return self.analyzer.build(
            comparison=comparison,
        )

    # ---------------------------------------------------------

    def performance(
        self,
    ) -> str:
        """
        Return the performance classification.
        """

        return self.comparisons.performance()

    # ---------------------------------------------------------

    def success_rate_change(
        self,
    ) -> float:
        """
        Return the success-rate change.
        """

        return self.comparisons.success_rate_change()

    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clear all snapshots.
        """

        self.comparisons.clear()