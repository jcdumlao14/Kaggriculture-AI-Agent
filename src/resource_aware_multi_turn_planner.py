"""
resource_aware_multi_turn_planner.py

Resource-Aware Multi-Turn Planner for the
Kaggriculture AI Agent.

Builds a feasible multi-turn task sequence while
tracking resource consumption after each task.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.resource_consumption_planner import (
    ResourceConsumptionPlanner,
)


class ResourceAwareMultiTurnPlanner:
    """
    Build resource-feasible multi-turn plans.
    """

    def __init__(self):
        self.resource_planner = (
            ResourceConsumptionPlanner()
        )

    # ---------------------------------------------------------

    def can_schedule(
        self,
        *,
        resources: dict,
        task: dict,
    ) -> bool:
        """
        Return True if the task can currently
        be afforded.
        """

        return self.resource_planner.affordable(
            resources=resources,
            task=task,
        )

    # ---------------------------------------------------------

    def build_plan(
        self,
        *,
        resources: dict,
        tasks: list[dict],
        max_turns: int | None = None,
    ) -> list[dict]:
        """
        Build a resource-feasible task sequence.

        Tasks are considered by descending priority.
        Resources are updated after each selected task.
        """

        if max_turns is not None and max_turns <= 0:
            return []

        current_resources = dict(resources)

        ordered_tasks = sorted(
            tasks,
            key=lambda task: task.get(
                "priority",
                0.0,
            ),
            reverse=True,
        )

        plan: list[dict] = []

        for task in ordered_tasks:

            if (
                max_turns is not None
                and len(plan) >= max_turns
            ):
                break

            if not self.can_schedule(
                resources=current_resources,
                task=task,
            ):
                continue

            plan.append(task)

            current_resources = (
                self.resource_planner.remaining(
                    resources=current_resources,
                    task=task,
                )
            )

        return plan

    # ---------------------------------------------------------

    def remaining_resources(
        self,
        *,
        resources: dict,
        plan: list[dict],
    ) -> dict:
        """
        Return resources remaining after a plan.
        """

        return self.resource_planner.apply(
            resources=resources,
            tasks=plan,
        )

    # ---------------------------------------------------------

    def plan_cost(
        self,
        *,
        plan: list[dict],
    ) -> dict:
        """
        Return total resource consumption
        for the plan.
        """

        total: dict = {}

        for task in plan:

            for resource, amount in (
                self.resource_planner
                .consumption(task=task)
                .items()
            ):

                total[resource] = (
                    total.get(resource, 0)
                    + amount
                )

        return total