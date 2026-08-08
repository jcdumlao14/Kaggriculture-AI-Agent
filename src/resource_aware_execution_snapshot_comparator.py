"""
resource_aware_execution_snapshot_comparator.py

Resource-Aware Execution Snapshot Comparator for the
Kaggriculture AI Agent.

Compares execution analytics snapshots.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAwareExecutionSnapshotComparator:
    """
    Compare two execution analytics snapshots.
    """

    # ---------------------------------------------------------

    def success_rate_change(
        self,
        *,
        current: dict,
        previous: dict,
    ) -> float:
        """
        Return the change in success rate.
        """

        return round(
            float(
                current.get(
                    "success_rate",
                    0.0,
                )
            )
            - float(
                previous.get(
                    "success_rate",
                    0.0,
                )
            ),
            10,
        )

    # ---------------------------------------------------------

    def task_count_change(
        self,
        *,
        current: dict,
        previous: dict,
    ) -> int:
        """
        Return the change in total task count.
        """

        return int(
            current.get(
                "total_tasks",
                0,
            )
        ) - int(
            previous.get(
                "total_tasks",
                0,
            )
        )

    # ---------------------------------------------------------

    def result_count_change(
        self,
        *,
        current: dict,
        previous: dict,
    ) -> int:
        """
        Return the change in total result count.
        """

        return int(
            current.get(
                "total_results",
                0,
            )
        ) - int(
            previous.get(
                "total_results",
                0,
            )
        )

    # ---------------------------------------------------------

    def resource_change(
        self,
        *,
        current: dict,
        previous: dict,
    ) -> dict:
        """
        Return the change in resource consumption.
        """

        current_resources = current.get(
            "resource_consumption",
            {},
        )

        previous_resources = previous.get(
            "resource_consumption",
            {},
        )

        if not isinstance(
            current_resources,
            dict,
        ):
            current_resources = {}

        if not isinstance(
            previous_resources,
            dict,
        ):
            previous_resources = {}

        keys = (
            set(current_resources)
            | set(previous_resources)
        )

        return {
            key: current_resources.get(
                key,
                0,
            )
            - previous_resources.get(
                key,
                0,
            )
            for key in keys
        }

    # ---------------------------------------------------------

    def performance(
        self,
        *,
        current: dict,
        previous: dict,
    ) -> str:
        """
        Classify performance based on success-rate change.
        """

        change = self.success_rate_change(
            current=current,
            previous=previous,
        )

        if change > 0:
            return "improved"

        if change < 0:
            return "declined"

        return "unchanged"

    # ---------------------------------------------------------

    def build(
        self,
        *,
        current: dict,
        previous: dict,
    ) -> dict:
        """
        Build a complete snapshot comparison.
        """

        return {
            "success_rate_change": (
                self.success_rate_change(
                    current=current,
                    previous=previous,
                )
            ),
            "task_count_change": (
                self.task_count_change(
                    current=current,
                    previous=previous,
                )
            ),
            "result_count_change": (
                self.result_count_change(
                    current=current,
                    previous=previous,
                )
            ),
            "resource_change": (
                self.resource_change(
                    current=current,
                    previous=previous,
                )
            ),
            "performance": self.performance(
                current=current,
                previous=previous,
            ),
        }