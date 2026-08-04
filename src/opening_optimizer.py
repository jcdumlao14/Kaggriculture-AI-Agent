"""
opening_optimizer.py

Opening Strategy Optimizer for the Kaggriculture AI Agent.

Tracks the performance of opening moves and
selects the highest-performing strategy.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class OpeningOptimizer:
    """
    Learns which opening moves perform best.
    """

    def __init__(self):
        self.scores = {}

    # ---------------------------------------------------------

    def record(self, move: str, reward: float):
        """
        Record the reward for an opening move.
        """
        self.scores.setdefault(move, [])
        self.scores[move].append(reward)

    # ---------------------------------------------------------

    def average(self, move: str) -> float:
        """
        Average reward of a move.
        """
        values = self.scores.get(move, [])

        if not values:
            return 0.0

        return sum(values) / len(values)

    # ---------------------------------------------------------

    def best_move(self):
        """
        Return the opening move with the
        highest average reward.
        """
        if not self.scores:
            return None

        return max(
            self.scores,
            key=self.average,
        )

    # ---------------------------------------------------------

    def move_count(self, move: str) -> int:
        """
        Number of recorded games.
        """
        return len(self.scores.get(move, []))

    # ---------------------------------------------------------

    def reset(self):
        """
        Clear all learned statistics.
        """
        self.scores.clear()
        