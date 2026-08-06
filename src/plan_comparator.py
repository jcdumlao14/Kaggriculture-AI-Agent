"""
plan_comparator.py

Plan Comparator for the Kaggriculture AI Agent.

Ranks candidate action plans and selects the
highest-scoring strategy.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.plan_evaluator import PlanEvaluator


class PlanComparator:
    """
    Compare multiple plans.
    """

    def __init__(
        self,
        evaluator: PlanEvaluator | None = None,
    ):
        self.evaluator = evaluator or PlanEvaluator()

    # ---------------------------------------------------------

    def best_plan(
        self,
        plans: list[list[dict]],
        *,
        game_state: dict | None = None,
    ) -> list[dict]:

        if not plans:
            return []

        return max(
            plans,
            key=lambda plan: self.evaluator.evaluate(
                plan,
                game_state=game_state,
            ),
        )

    # ---------------------------------------------------------

    def rank_plans(
        self,
        plans: list[list[dict]],
        *,
        game_state: dict | None = None,
    ) -> list[list[dict]]:

        return sorted(
            plans,
            key=lambda plan: self.evaluator.evaluate(
                plan,
                game_state=game_state,
            ),
            reverse=True,
        )

    # ---------------------------------------------------------

    def best_score(
        self,
        plans: list[list[dict]],
        *,
        game_state: dict | None = None,
    ) -> float:

        if not plans:
            return 0.0

        return self.evaluator.evaluate(
            self.best_plan(
                plans,
                game_state=game_state,
            ),
            game_state=game_state,
        )

    # ---------------------------------------------------------

    def has_plans(
        self,
        plans: list[list[dict]],
    ) -> bool:

        return bool(plans)