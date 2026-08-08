"""
resource_aware_plan_evaluator.py

Resource-Aware Plan Evaluator for the
Kaggriculture AI Agent.

Evaluates multi-turn plans using priority,
resource usage, and feasibility.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAwarePlanEvaluator:
    """
    Evaluate resource-aware multi-turn plans.
    """

    # ---------------------------------------------------------

    def total_priority(
        self,
        *,
        plan: list[dict],
    ) -> float:
        """
        Return the total priority of all tasks.
        """

        return sum(
            float(
                task.get("priority", 0.0)
            )
            for task in plan
        )

    # ---------------------------------------------------------

    def resource_cost(
        self,
        *,
        plan: list[dict],
    ) -> float:
        """
        Return the total amount of resources consumed.

        Each consumed resource unit contributes one
        point to the cost.
        """

        total = 0.0

        for task in plan:

            requirements = task.get(
                "requirements",
                {},
            )

            total += sum(
                float(amount)
                for amount in requirements.values()
            )

        return total

    # ---------------------------------------------------------

    def evaluate(
        self,
        *,
        plan: list[dict],
    ) -> float:
        """
        Calculate an overall plan score.

        Higher priority improves the score while
        resource consumption reduces it.
        """

        priority = self.total_priority(
            plan=plan,
        )

        cost = self.resource_cost(
            plan=plan,
        )

        return priority - cost

    # ---------------------------------------------------------

    def is_better(
        self,
        *,
        first: list[dict],
        second: list[dict],
    ) -> bool:
        """
        Return True when the first plan scores higher.
        """

        return (
            self.evaluate(plan=first)
            > self.evaluate(plan=second)
        )

    # ---------------------------------------------------------

    def best_plan(
        self,
        *,
        plans: list[list[dict]],
    ) -> list[dict]:
        """
        Return the highest-scoring plan.

        Return an empty plan when no candidates exist.
        """

        if not plans:
            return []

        return max(
            plans,
            key=lambda plan: self.evaluate(
                plan=plan,
            ),
        )