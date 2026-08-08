"""
resource_aware_execution_analytics.py

Resource-Aware Execution Analytics for the
Kaggriculture AI Agent.

Analyzes historical resource-aware execution results.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAwareExecutionAnalytics:
    """
    Analyze execution history.
    """

    # ---------------------------------------------------------

    def success_count(
        self,
        *,
        results: list[dict],
    ) -> int:
        """
        Return the number of successful results.
        """

        return sum(
            1
            for result in results
            if result.get("success", False)
        )

    # ---------------------------------------------------------

    def failure_count(
        self,
        *,
        results: list[dict],
    ) -> int:
        """
        Return the number of failed results.
        """

        return sum(
            1
            for result in results
            if not result.get("success", False)
        )

    # ---------------------------------------------------------

    def success_rate(
        self,
        *,
        results: list[dict],
    ) -> float:
        """
        Return the execution success rate.
        """

        if not results:
            return 0.0

        return self.success_count(
            results=results,
        ) / len(results)

    # ---------------------------------------------------------

    def average_task_count(
        self,
        *,
        results: list[dict],
    ) -> float:
        """
        Return the average number of tasks per result.
        """

        if not results:
            return 0.0

        counts = [
            len(result.get("plan", []))
            if isinstance(
                result.get("plan", []),
                list,
            )
            else 0
            for result in results
        ]

        return sum(counts) / len(counts)

    # ---------------------------------------------------------

    def total_tasks(
        self,
        *,
        results: list[dict],
    ) -> int:
        """
        Return the total number of planned tasks.
        """

        return sum(
            len(result.get("plan", []))
            if isinstance(
                result.get("plan", []),
                list,
            )
            else 0
            for result in results
        )

    # ---------------------------------------------------------

    def resource_consumption(
        self,
        *,
        results: list[dict],
    ) -> dict:
        """
        Aggregate resource consumption.
        """

        totals: dict = {}

        for result in results:

            resources = result.get(
                "resources",
                {},
            )

            remaining = result.get(
                "remaining",
                resources,
            )

            if not isinstance(
                resources,
                dict,
            ):
                continue

            if not isinstance(
                remaining,
                dict,
            ):
                continue

            keys = (
                set(resources)
                | set(remaining)
            )

            for resource in keys:

                consumed = (
                    resources.get(
                        resource,
                        0,
                    )
                    - remaining.get(
                        resource,
                        0,
                    )
                )

                totals[resource] = (
                    totals.get(
                        resource,
                        0,
                    )
                    + consumed
                )

        return totals

    # ---------------------------------------------------------

    def rejection_reasons(
        self,
        *,
        results: list[dict],
    ) -> dict:
        """
        Count execution rejection reasons.
        """

        reasons: dict = {}

        for result in results:

            if result.get(
                "success",
                False,
            ):
                continue

            reason = result.get(
                "reason"
            )

            if reason is None:
                continue

            reasons[reason] = (
                reasons.get(reason, 0)
                + 1
            )

        return reasons

    # ---------------------------------------------------------

    def build(
        self,
        *,
        results: list[dict],
    ) -> dict:
        """
        Build a complete analytics summary.
        """

        return {
            "total_results": len(results),
            "success_count": self.success_count(
                results=results,
            ),
            "failure_count": self.failure_count(
                results=results,
            ),
            "success_rate": self.success_rate(
                results=results,
            ),
            "total_tasks": self.total_tasks(
                results=results,
            ),
            "average_task_count": (
                self.average_task_count(
                    results=results,
                )
            ),
            "resource_consumption": (
                self.resource_consumption(
                    results=results,
                )
            ),
            "rejection_reasons": (
                self.rejection_reasons(
                    results=results,
                )
            ),
        }