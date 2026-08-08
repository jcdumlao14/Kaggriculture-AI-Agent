"""
resource_aware_execution_snapshot.py

Resource-Aware Execution Snapshot for the
Kaggriculture AI Agent.

Creates immutable-style snapshots of execution
analytics at a specific point in time.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from copy import deepcopy


class ResourceAwareExecutionSnapshot:
    """
    Build and manage execution analytics snapshots.
    """

    # ---------------------------------------------------------

    def create(
        self,
        *,
        analytics: dict,
    ) -> dict:
        """
        Create an independent snapshot of analytics.
        """

        return deepcopy(analytics)

    # ---------------------------------------------------------

    def total_results(
        self,
        *,
        snapshot: dict,
    ) -> int:
        """
        Return the number of recorded results.
        """

        return int(
            snapshot.get(
                "total_results",
                0,
            )
        )

    # ---------------------------------------------------------

    def success_count(
        self,
        *,
        snapshot: dict,
    ) -> int:
        """
        Return the number of successful results.
        """

        return int(
            snapshot.get(
                "success_count",
                0,
            )
        )

    # ---------------------------------------------------------

    def failure_count(
        self,
        *,
        snapshot: dict,
    ) -> int:
        """
        Return the number of failed results.
        """

        return int(
            snapshot.get(
                "failure_count",
                0,
            )
        )

    # ---------------------------------------------------------

    def success_rate(
        self,
        *,
        snapshot: dict,
    ) -> float:
        """
        Return the success rate.
        """

        return float(
            snapshot.get(
                "success_rate",
                0.0,
            )
        )

    # ---------------------------------------------------------

    def resource_consumption(
        self,
        *,
        snapshot: dict,
    ) -> dict:
        """
        Return resource consumption.
        """

        consumption = snapshot.get(
            "resource_consumption",
            {},
        )

        if not isinstance(
            consumption,
            dict,
        ):
            return {}

        return dict(consumption)

    # ---------------------------------------------------------

    def rejection_reasons(
        self,
        *,
        snapshot: dict,
    ) -> dict:
        """
        Return rejection reason counts.
        """

        reasons = snapshot.get(
            "rejection_reasons",
            {},
        )

        if not isinstance(
            reasons,
            dict,
        ):
            return {}

        return dict(reasons)

    # ---------------------------------------------------------

    def is_empty(
        self,
        *,
        snapshot: dict,
    ) -> bool:
        """
        Return True when the snapshot contains
        no execution results.
        """

        return (
            self.total_results(
                snapshot=snapshot,
            )
            == 0
        )

    # ---------------------------------------------------------

    def build(
        self,
        *,
        analytics: dict,
    ) -> dict:
        """
        Create a normalized analytics snapshot.
        """

        snapshot = self.create(
            analytics=analytics,
        )

        return {
            "total_results": self.total_results(
                snapshot=snapshot,
            ),
            "success_count": self.success_count(
                snapshot=snapshot,
            ),
            "failure_count": self.failure_count(
                snapshot=snapshot,
            ),
            "success_rate": self.success_rate(
                snapshot=snapshot,
            ),
            "total_tasks": int(
                snapshot.get(
                    "total_tasks",
                    0,
                )
            ),
            "average_task_count": float(
                snapshot.get(
                    "average_task_count",
                    0.0,
                )
            ),
            "resource_consumption": (
                self.resource_consumption(
                    snapshot=snapshot,
                )
            ),
            "rejection_reasons": (
                self.rejection_reasons(
                    snapshot=snapshot,
                )
            ),
        }