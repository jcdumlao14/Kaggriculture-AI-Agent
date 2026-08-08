"""
resource_aware_execution_metrics.py

Resource-Aware Execution Metrics for the
Kaggriculture AI Agent.

Extracts reusable metrics from resource-aware
execution results.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAwareExecutionMetrics:
    """
    Extract execution metrics.
    """

    # ---------------------------------------------------------

    def task_count(
        self,
        *,
        result: dict,
    ) -> int:
        """
        Return the number of tasks in the result.
        """

        plan = result.get("plan", [])

        if not isinstance(plan, list):
            return 0

        return len(plan)

    # ---------------------------------------------------------

    def executed_count(
        self,
        *,
        result: dict,
    ) -> int:
        """
        Return the number of tasks actually executed.
        """

        if not result.get("executed", False):
            return 0

        return self.task_count(
            result=result,
        )

    # ---------------------------------------------------------

    def success_rate(
        self,
        *,
        results: list[dict],
    ) -> float:
        """
        Return the fraction of successful executions.
        """

        if not results:
            return 0.0

        successful = sum(
            1
            for result in results
            if result.get("success", False)
        )

        return successful / len(results)

    # ---------------------------------------------------------

    def failure_count(
        self,
        *,
        results: list[dict],
    ) -> int:
        """
        Return the number of failed executions.
        """

        return sum(
            1
            for result in results
            if not result.get("success", False)
        )

    # ---------------------------------------------------------

    def resource_consumption(
        self,
        *,
        result: dict,
    ) -> dict:
        """
        Return resources consumed by the execution.
        """

        resources = result.get(
            "resources",
            {},
        )

        remaining = result.get(
            "remaining",
            resources,
        )

        if not isinstance(resources, dict):
            return {}

        if not isinstance(remaining, dict):
            return {}

        keys = set(resources) | set(remaining)

        return {
            key: resources.get(key, 0)
            - remaining.get(key, 0)
            for key in keys
        }

    # ---------------------------------------------------------

    def total_resource_consumption(
        self,
        *,
        results: list[dict],
    ) -> dict:
        """
        Return total resource consumption across results.
        """

        totals: dict = {}

        for result in results:

            consumption = self.resource_consumption(
                result=result,
            )

            for resource, amount in consumption.items():
                totals[resource] = (
                    totals.get(resource, 0)
                    + amount
                )

        return totals

    # ---------------------------------------------------------

    def build(
        self,
        *,
        result: dict,
    ) -> dict:
        """
        Build a compact metrics dictionary.
        """

        return {
            "success": bool(
                result.get(
                    "success",
                    False,
                )
            ),
            "task_count": self.task_count(
                result=result,
            ),
            "executed_count": self.executed_count(
                result=result,
            ),
            "resource_consumption": (
                self.resource_consumption(
                    result=result,
                )
            ),
        }