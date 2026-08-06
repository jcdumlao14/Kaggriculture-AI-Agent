"""
plan_evaluator.py

Plan Evaluator for the Kaggriculture AI Agent.

Evaluates complete action plans by combining the
scores of individual actions.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.action_scoring_engine import ActionScoringEngine


class PlanEvaluator:
    """
    Evaluates action plans.
    """

    def __init__(
        self,
        scorer: ActionScoringEngine | None = None,
    ):
        self.scorer = scorer or ActionScoringEngine()

    # ---------------------------------------------------------

    def evaluate(
        self,
        actions: list[dict],
        *,
        game_state: dict | None = None,
    ) -> float:
        """
        Return the total score of a plan.
        """

        total = 0.0

        for action in actions:

            total += self.scorer.score(
                action=action["action"],
                game_state=game_state,
            )

        return float(total)

    # ---------------------------------------------------------

    def better_plan(
        self,
        first: list[dict],
        second: list[dict],
        *,
        game_state: dict | None = None,
    ) -> list[dict]:
        """
        Return the higher-scoring plan.
        """

        if self.evaluate(
            first,
            game_state=game_state,
        ) >= self.evaluate(
            second,
            game_state=game_state,
        ):
            return first

        return second

    # ---------------------------------------------------------

    def average_score(
        self,
        actions: list[dict],
        *,
        game_state: dict | None = None,
    ) -> float:
        """
        Return the average score of a plan.
        """

        if not actions:
            return 0.0

        return (
            self.evaluate(
                actions,
                game_state=game_state,
            )
            / len(actions)
        )

    # ---------------------------------------------------------

    def is_empty(
        self,
        actions: list[dict],
    ) -> bool:
        """
        Return True if the plan is empty.
        """

        return len(actions) == 0