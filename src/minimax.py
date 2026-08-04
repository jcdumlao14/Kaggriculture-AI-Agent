"""
minimax.py

Minimax Engine for the Kaggriculture AI Agent.

Provides a simplified minimax evaluator.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class Minimax:
    """
    Basic Minimax evaluator.
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------

    def maximize(self, scores: list[float]) -> float:
        """
        Return the maximum score.
        """

        if not scores:
            return 0.0

        return max(scores)

    # ---------------------------------------------------------

    def minimize(self, scores: list[float]) -> float:
        """
        Return the minimum score.
        """

        if not scores:
            return 0.0

        return min(scores)

    # ---------------------------------------------------------

    def choose(
        self,
        scores: list[float],
        maximizing: bool = True,
    ) -> float:
        """
        Choose the best score depending on the player.
        """

        if maximizing:
            return self.maximize(scores)

        return self.minimize(scores)