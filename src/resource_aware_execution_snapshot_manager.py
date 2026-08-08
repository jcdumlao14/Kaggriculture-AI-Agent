"""
resource_aware_execution_snapshot_manager.py

Resource-Aware Execution Snapshot Manager for the
Kaggriculture AI Agent.

Maintains current and previous execution analytics
snapshots for comparison.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from copy import deepcopy

from src.resource_aware_execution_snapshot import (
    ResourceAwareExecutionSnapshot,
)


class ResourceAwareExecutionSnapshotManager:
    """
    Manage execution analytics snapshots.
    """

    def __init__(self):
        self.snapshotter = (
            ResourceAwareExecutionSnapshot()
        )

        self._current: dict | None = None
        self._previous: dict | None = None

    # ---------------------------------------------------------

    def create(
        self,
        *,
        analytics: dict,
    ) -> dict:
        """
        Create and store a new current snapshot.

        The existing current snapshot becomes previous.
        """

        snapshot = self.snapshotter.build(
            analytics=analytics,
        )

        if self._current is not None:
            self._previous = deepcopy(
                self._current
            )

        self._current = deepcopy(
            snapshot
        )

        return deepcopy(snapshot)

    # ---------------------------------------------------------

    def current(
        self,
    ) -> dict | None:
        """
        Return the current snapshot.
        """

        if self._current is None:
            return None

        return deepcopy(
            self._current
        )

    # ---------------------------------------------------------

    def previous(
        self,
    ) -> dict | None:
        """
        Return the previous snapshot.
        """

        if self._previous is None:
            return None

        return deepcopy(
            self._previous
        )

    # ---------------------------------------------------------

    def has_current(
        self,
    ) -> bool:
        """
        Return True when a current snapshot exists.
        """

        return self._current is not None

    # ---------------------------------------------------------

    def has_previous(
        self,
    ) -> bool:
        """
        Return True when a previous snapshot exists.
        """

        return self._previous is not None

    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clear current and previous snapshots.
        """

        self._current = None
        self._previous = None

    # ---------------------------------------------------------

    def current_success_rate(
        self,
    ) -> float:
        """
        Return the current success rate.
        """

        if self._current is None:
            return 0.0

        return self.snapshotter.success_rate(
            snapshot=self._current,
        )

    # ---------------------------------------------------------

    def previous_success_rate(
        self,
    ) -> float:
        """
        Return the previous success rate.
        """

        if self._previous is None:
            return 0.0

        return self.snapshotter.success_rate(
            snapshot=self._previous,
        )

    # ---------------------------------------------------------

    def success_rate_change(
        self,
    ) -> float:
        """
        Return current success rate minus previous
        success rate.
        """

        return round(
            self.current_success_rate()
            - self.previous_success_rate(),
            10,
        )