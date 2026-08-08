"""
resource_aware_plan_comparator.py

Resource-Aware Plan Comparator for the
Kaggriculture AI Agent.

Compares candidate plans using their priority,
resource consumption, and overall evaluation score.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.resource_aware_plan_evaluator import (
    ResourceAwarePlanEvaluator,
)


class ResourceAwarePlanComparator:
    """
    Compare candidate resource-aware plans.
    """

    def __init__(self):
        self.evaluator = (
            ResourceAwarePlanEvaluator()
        )

    # ---------------------------------------------------------

    def score(
        self,
        *,
        plan: list[dict],
    ) -> float:
        """
        Return the score of a plan.
        """

        return self.evaluator.evaluate(
            plan=plan,
        )

    # ---------------------------------------------------------

    def compare(
        self,
        *,
        first: list[dict],
        second: list[dict],
    ) -> int:
        """
        Compare two plans.

        Returns:

        1  -> first is better
        0  -> equal
        -1 -> second is better
        """

        first_score = self.score(
            plan=first,
        )

        second_score = self.score(
            plan=second,
        )

        if first_score > second_score:
            return 1

        if first_score < second_score:
            return -1

        return 0

    # ---------------------------------------------------------

    def rank(
        self,
        *,
        plans: list[list[dict]],
    ) -> list[list[dict]]:
        """
        Rank plans from highest to lowest score.
        """

        return sorted(
            plans,
            key=lambda plan: self.score(
                plan=plan,
            ),
            reverse=True,
        )

    # ---------------------------------------------------------

    def best(
        self,
        *,
        plans: list[list[dict]],
    ) -> list[dict]:
        """
        Return the highest-scoring plan.
        """

        if not plans:
            return []

        return self.rank(
            plans=plans,
        )[0]

    # ---------------------------------------------------------

    def scores(
        self,
        *,
        plans: list[list[dict]],
    ) -> list[float]:
        """
        Return scores in the same order as
        the supplied plans.
        """

        return [
            self.score(plan=plan)
            for plan in plans
        ]