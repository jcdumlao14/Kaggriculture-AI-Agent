"""
resource_aware_execution_guard.py

Resource-Aware Execution Guard for the
Kaggriculture AI Agent.

Performs final validation and resource checks
before a plan is executed.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.resource_aware_plan_validator import (
    ResourceAwarePlanValidator,
)


class ResourceAwareExecutionGuard:
    """
    Guard plan execution against invalid tasks
    and insufficient resources.
    """

    def __init__(self):
        self.validator = (
            ResourceAwarePlanValidator()
        )

    # ---------------------------------------------------------

    def is_affordable(
        self,
        *,
        resources: dict,
        plan: list[dict],
    ) -> bool:
        """
        Return True when the complete plan can be
        executed with the available resources.
        """

        if not isinstance(resources, dict):
            return False

        current = dict(resources)

        for task in plan:

            requirements = task.get(
                "requirements",
                {},
            )

            for resource, amount in requirements.items():

                if current.get(
                    resource,
                    0,
                ) < amount:
                    return False

                current[resource] = (
                    current.get(resource, 0)
                    - amount
                )

        return True

    # ---------------------------------------------------------

    def can_execute(
        self,
        *,
        resources: dict,
        plan: list[dict],
    ) -> bool:
        """
        Return True when the plan is both structurally
        valid and resource-feasible.
        """

        if not self.validator.validate(
            plan=plan,
        ):
            return False

        return self.is_affordable(
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
        Return resources remaining after execution.

        If the plan cannot execute, return the
        original resource state unchanged.
        """

        if not self.can_execute(
            resources=resources,
            plan=plan,
        ):
            return dict(resources)

        remaining = dict(resources)

        for task in plan:

            for resource, amount in task.get(
                "requirements",
                {},
            ).items():

                remaining[resource] = (
                    remaining.get(resource, 0)
                    - amount
                )

        return remaining

    # ---------------------------------------------------------

    def reject_reason(
        self,
        *,
        resources: dict,
        plan: list[dict],
    ) -> str | None:
        """
        Return a reason when execution is rejected.

        Return None when execution is allowed.
        """

        if not self.validator.validate(
            plan=plan,
        ):
            return "invalid_plan"

        if not self.is_affordable(
            resources=resources,
            plan=plan,
        ):
            return "insufficient_resources"

        return None