"""
resource_aware_plan_selector.py

Resource-Aware Plan Selector for the
Kaggriculture AI Agent.

Selects the best candidate plan subject to
a minimum acceptable evaluation score.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.resource_aware_plan_comparator import (
    ResourceAwarePlanComparator,
)


class ResourceAwarePlanSelector:
    """
    Select the best resource-aware plan.
    """

    def __init__(
        self,
        minimum_score: float = 0.0,
    ):
        self.minimum_score = minimum_score

        self.comparator = (
            ResourceAwarePlanComparator()
        )

    # ---------------------------------------------------------

    def score(
        self,
        *,
        plan: list[dict],
    ) -> float:
        """
        Return the plan score.
        """

        return self.comparator.score(
            plan=plan,
        )

    # ---------------------------------------------------------

    def is_acceptable(
        self,
        *,
        plan: list[dict],
    ) -> bool:
        """
        Return True when a plan reaches the
        minimum acceptable score.
        """

        return (
            self.score(plan=plan)
            >= self.minimum_score
        )

    # ---------------------------------------------------------

    def select(
        self,
        *,
        plans: list[list[dict]],
    ) -> list[dict]:
        """
        Select the highest-scoring acceptable plan.

        Return an empty plan when no candidate
        satisfies the minimum score.
        """

        acceptable = [
            plan
            for plan in plans
            if self.is_acceptable(
                plan=plan,
            )
        ]

        if not acceptable:
            return []

        return self.comparator.best(
            plans=acceptable,
        )

    # ---------------------------------------------------------

    def select_with_score(
        self,
        *,
        plans: list[list[dict]],
    ) -> tuple[list[dict], float]:
        """
        Return the selected plan together with
        its score.
        """

        selected = self.select(
            plans=plans,
        )

        if not selected:
            return [], 0.0

        return (
            selected,
            self.score(plan=selected),
        )

    # ---------------------------------------------------------

    def accepted_plans(
        self,
        *,
        plans: list[list[dict]],
    ) -> list[list[dict]]:
        """
        Return all plans meeting the minimum score.
        """

        return [
            plan
            for plan in plans
            if self.is_acceptable(
                plan=plan,
            )
        ]