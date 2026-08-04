"""
state_evaluator.py

State evaluation module for the Kaggriculture AI Agent.

Assigns a numeric score to the current game state.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class StateEvaluator:
    """
    Evaluates how favorable the current game state is.
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------

    def evaluate(
        self,
        money: float,
        crops: int,
        animals: int,
        inventory: int,
    ) -> float:
        """
        Compute a weighted state score.
        """

        return (
            money * 0.10
            + crops * 15
            + animals * 25
            + inventory * 5
        )

    # ---------------------------------------------------------

    def better(
        self,
        score_a: float,
        score_b: float,
    ) -> bool:
        """
        Return True if score_a is better.
        """

        return score_a > score_b

    # ---------------------------------------------------------

    def difference(
        self,
        score_a: float,
        score_b: float,
    ) -> float:
        """
        Return the score difference.
        """

        return score_a - score_b