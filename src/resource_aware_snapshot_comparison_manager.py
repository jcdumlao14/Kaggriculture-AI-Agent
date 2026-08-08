"""
resource_aware_snapshot_comparison_manager.py

Resource-Aware Snapshot Comparison Manager for the
Kaggriculture AI Agent.

Manages comparisons between execution analytics
snapshots.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.resource_aware_execution_snapshot_comparator import (
    ResourceAwareExecutionSnapshotComparator,
)
from src.resource_aware_execution_snapshot_manager import (
    ResourceAwareExecutionSnapshotManager,
)


class ResourceAwareSnapshotComparisonManager:
    """
    Manage execution snapshot comparisons.
    """

    def __init__(self):
        self.snapshots = (
            ResourceAwareExecutionSnapshotManager()
        )

        self.comparator = (
            ResourceAwareExecutionSnapshotComparator()
        )

    # ---------------------------------------------------------

    def create_snapshot(
        self,
        *,
        analytics: dict,
    ) -> dict:
        """
        Create and store an execution snapshot.
        """

        return self.snapshots.create(
            analytics=analytics,
        )

    # ---------------------------------------------------------

    def current(
        self,
    ) -> dict | None:
        """
        Return the current snapshot.
        """

        return self.snapshots.current()

    # ---------------------------------------------------------

    def previous(
        self,
    ) -> dict | None:
        """
        Return the previous snapshot.
        """

        return self.snapshots.previous()

    # ---------------------------------------------------------

    def can_compare(
        self,
    ) -> bool:
        """
        Return True when current and previous
        snapshots are available.
        """

        return (
            self.snapshots.has_current()
            and self.snapshots.has_previous()
        )

    # ---------------------------------------------------------

    def compare(
        self,
    ) -> dict | None:
        """
        Compare the current and previous snapshots.

        Return None when a previous snapshot is unavailable.
        """

        current = self.current()
        previous = self.previous()

        if current is None or previous is None:
            return None

        return self.comparator.build(
            current=current,
            previous=previous,
        )

    # ---------------------------------------------------------

    def performance(
        self,
    ) -> str:
        """
        Return the current performance classification.

        If there is no previous snapshot, return
        'unknown'.
        """

        comparison = self.compare()

        if comparison is None:
            return "unknown"

        return comparison["performance"]

    # ---------------------------------------------------------

    def success_rate_change(
        self,
    ) -> float:
        """
        Return the change in success rate.

        Returns zero when there is no previous snapshot.
        """

        comparison = self.compare()

        if comparison is None:
            return 0.0

        return comparison[
            "success_rate_change"
        ]

    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clear all snapshots.
        """

        self.snapshots.clear()