"""
resource_aware_execution_result.py

Resource-Aware Execution Result for the
Kaggriculture AI Agent.

Represents the outcome of a resource-aware
execution decision.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAwareExecutionResult:
    """
    Build structured execution results.
    """

    # ---------------------------------------------------------

    def success(
        self,
        *,
        plan: list[dict],
        resources: dict,
        remaining: dict,
    ) -> dict:
        """
        Build a successful execution result.
        """

        return {
            "success": True,
            "executed": True,
            "plan": list(plan),
            "resources": dict(resources),
            "remaining": dict(remaining),
            "reason": None,
        }

    # ---------------------------------------------------------

    def failure(
        self,
        *,
        plan: list[dict],
        resources: dict,
        reason: str,
    ) -> dict:
        """
        Build a failed execution result.
        """

        return {
            "success": False,
            "executed": False,
            "plan": list(plan),
            "resources": dict(resources),
            "remaining": dict(resources),
            "reason": reason,
        }

    # ---------------------------------------------------------

    def is_success(
        self,
        *,
        result: dict,
    ) -> bool:
        """
        Return True when the result represents
        successful execution.
        """

        return bool(
            result.get("success", False)
        )

    # ---------------------------------------------------------

    def is_failure(
        self,
        *,
        result: dict,
    ) -> bool:
        """
        Return True when execution failed.
        """

        return not self.is_success(
            result=result,
        )

    # ---------------------------------------------------------

    def executed_tasks(
        self,
        *,
        result: dict,
    ) -> list[dict]:
        """
        Return tasks that were executed.
        """

        if not self.is_success(
            result=result,
        ):
            return []

        return list(
            result.get("plan", [])
        )

    # ---------------------------------------------------------

    def reason(
        self,
        *,
        result: dict,
    ) -> str | None:
        """
        Return the execution result reason.
        """

        return result.get("reason")