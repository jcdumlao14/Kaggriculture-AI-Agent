"""
resource_aware_execution_summary.py

Resource-Aware Execution Summary for the
Kaggriculture AI Agent.

Provides compact summaries of resource-aware
execution outcomes.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAwareExecutionSummary:
    """
    Summarize resource-aware execution results.
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

    def resource_change(
        self,
        *,
        result: dict,
    ) -> dict:
        """
        Return the amount of each resource consumed.
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

    def success(
        self,
        *,
        result: dict,
    ) -> bool:
        """
        Return whether execution succeeded.
        """

        return bool(
            result.get("success", False)
        )

    # ---------------------------------------------------------

    def reason(
        self,
        *,
        result: dict,
    ) -> str | None:
        """
        Return the execution reason.
        """

        return result.get("reason")

    # ---------------------------------------------------------

    def build(
        self,
        *,
        result: dict,
    ) -> dict:
        """
        Build a compact execution summary.
        """

        return {
            "success": self.success(
                result=result,
            ),
            "executed": bool(
                result.get(
                    "executed",
                    False,
                )
            ),
            "task_count": self.task_count(
                result=result,
            ),
            "resource_change": self.resource_change(
                result=result,
            ),
            "reason": self.reason(
                result=result,
            ),
        }