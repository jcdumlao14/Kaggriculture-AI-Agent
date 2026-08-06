"""
strategy_evaluator.py

Strategy Evaluator for the Kaggriculture AI Agent.

Evaluates strategy performance over time.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class StrategyEvaluator:
    """
    Tracks strategy performance.
    """

    def __init__(self):
        self._scores = {}

    # ---------------------------------------------------------

    def record(
        self,
        strategy: str,
        score: float,
    ) -> None:
        """
        Record a strategy score.
        """

        self._scores.setdefault(
            strategy,
            [],
        ).append(float(score))

    # ---------------------------------------------------------

    def average(
        self,
        strategy: str,
    ) -> float:
        """
        Return average score.
        """

        scores = self._scores.get(
            strategy,
            [],
        )

        if not scores:
            return 0.0

        return sum(scores) / len(scores)

    # ---------------------------------------------------------

    def best_strategy(
        self,
    ) -> str | None:
        """
        Return highest-performing strategy.
        """

        if not self._scores:
            return None

        return max(
            self._scores,
            key=self.average,
        )

    # ---------------------------------------------------------

    def strategies(
        self,
    ) -> list[str]:
        """
        Return known strategies.
        """

        return sorted(
            self._scores.keys()
        )

    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Remove all recorded data.
        """

        self._scores.clear()