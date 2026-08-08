"""
resource_aware_execution_pipeline.py

Resource-Aware Execution Pipeline for the
Kaggriculture AI Agent.

Connects candidate-plan selection with resource-aware
execution.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.resource_aware_plan_selector import (
    ResourceAwarePlanSelector,
)
from src.resource_aware_execution_coordinator import (
    ResourceAwareExecutionCoordinator,
)


class ResourceAwareExecutionPipeline:
    """
    Select and execute the best resource-aware plan.
    """

    def __init__(
        self,
        minimum_score: float = 0.0,
    ):
        self.selector = ResourceAwarePlanSelector(
            minimum_score=minimum_score,
        )

        self.coordinator = (
            ResourceAwareExecutionCoordinator()
        )

    # ---------------------------------------------------------

    def select(
        self,
        *,
        plans: list[list[dict]],
    ) -> list[dict]:
        """
        Select the best acceptable candidate plan.
        """

        return self.selector.select(
            plans=plans,
        )

    # ---------------------------------------------------------

    def can_execute(
        self,
        *,
        resources: dict,
        plan: list[dict],
    ) -> bool:
        """
        Return True when the selected plan
        can be executed.
        """

        return self.coordinator.can_execute(
            resources=resources,
            plan=plan,
        )

    # ---------------------------------------------------------

    def run(
        self,
        *,
        resources: dict,
        plans: list[list[dict]],
    ) -> dict:
        """
        Select the best candidate and attempt execution.

        If no acceptable plan exists, return a structured
        failure result.
        """

        selected = self.select(
            plans=plans,
        )

        if not selected:
            return {
                "success": False,
                "executed": False,
                "plan": [],
                "resources": dict(resources),
                "remaining": dict(resources),
                "reason": "no_acceptable_plan",
            }

        return self.coordinator.execute(
            resources=resources,
            plan=selected,
        )

    # ---------------------------------------------------------

    def remaining_resources(
        self,
        *,
        resources: dict,
        plans: list[list[dict]],
    ) -> dict:
        """
        Return resources remaining after selecting
        and executing the best acceptable plan.
        """

        result = self.run(
            resources=resources,
            plans=plans,
        )

        return dict(
            result.get(
                "remaining",
                resources,
            )
        )

    # ---------------------------------------------------------

    def selected_score(
        self,
        *,
        plans: list[list[dict]],
    ) -> float:
        """
        Return the score of the selected plan.

        Return 0 when no plan is selected.
        """

        selected = self.select(
            plans=plans,
        )

        if not selected:
            return 0.0

        return self.selector.score(
            plan=selected,
        )