"""
resource_aware_execution_coordinator.py

Resource-Aware Execution Coordinator for the
Kaggriculture AI Agent.

Coordinates final validation, resource checks,
and structured execution results.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.resource_aware_execution_guard import (
    ResourceAwareExecutionGuard,
)
from src.resource_aware_execution_result import (
    ResourceAwareExecutionResult,
)


class ResourceAwareExecutionCoordinator:
    """
    Coordinate resource-aware plan execution decisions.
    """

    def __init__(self):
        self.guard = ResourceAwareExecutionGuard()
        self.result_builder = (
            ResourceAwareExecutionResult()
        )

    # ---------------------------------------------------------

    def execute(
        self,
        *,
        resources: dict,
        plan: list[dict],
    ) -> dict:
        """
        Validate and execute a resource-aware plan.

        This method models the execution decision and
        returns the resulting resource state.
        """

        if not self.guard.can_execute(
            resources=resources,
            plan=plan,
        ):
            reason = self.guard.reject_reason(
                resources=resources,
                plan=plan,
            )

            return self.result_builder.failure(
                plan=plan,
                resources=resources,
                reason=reason or "execution_rejected",
            )

        remaining = self.guard.remaining_resources(
            resources=resources,
            plan=plan,
        )

        return self.result_builder.success(
            plan=plan,
            resources=resources,
            remaining=remaining,
        )

    # ---------------------------------------------------------

    def can_execute(
        self,
        *,
        resources: dict,
        plan: list[dict],
    ) -> bool:
        """
        Return True when the plan can execute.
        """

        return self.guard.can_execute(
            resources=resources,
            plan=plan,
        )

    # ---------------------------------------------------------

    def remaining_resources(
        self,
        *,
        resources: dict,
        plan: list[dict],
    ) -> dict:
        """
        Return the resources remaining after execution.

        If execution is rejected, the original resources
        are preserved.
        """

        return self.guard.remaining_resources(
            resources=resources,
            plan=plan,
        )

    # ---------------------------------------------------------

    def rejection_reason(
        self,
        *,
        resources: dict,
        plan: list[dict],
    ) -> str | None:
        """
        Return the reason a plan cannot execute.
        """

        return self.guard.reject_reason(
            resources=resources,
            plan=plan,
        )