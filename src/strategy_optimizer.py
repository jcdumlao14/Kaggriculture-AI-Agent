"""
strategy_optimizer.py

Strategy Optimizer for the Kaggriculture AI Agent.

Chooses the highest-scoring strategy from a set
of candidate strategies.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class StrategyOptimizer:
    """
    Compare strategies and choose the best one.
    """

    def __init__(self):
        self.strategies = []

    # ---------------------------------------------------------

    def add(self, name: str, score: float):

        self.strategies.append(
            {
                "name": name,
                "score": score,
            }
        )

    # ---------------------------------------------------------

    def best(self):

        if not self.strategies:
            return None

        return max(
            self.strategies,
            key=lambda s: s["score"],
        )

    # ---------------------------------------------------------

    def ranking(self):

        return sorted(
            self.strategies,
            key=lambda s: s["score"],
            reverse=True,
        )

    # ---------------------------------------------------------

    def clear(self):

        self.strategies.clear()

    # ---------------------------------------------------------

    def __len__(self):

        return len(self.strategies)