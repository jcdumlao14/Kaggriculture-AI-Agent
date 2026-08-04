"""
self_play_trainer.py

Self-Play Trainer for the Kaggriculture AI Agent.

Runs self-play simulations and records rewards.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class SelfPlayTrainer:
    """
    Records results from self-play sessions.
    """

    def __init__(self):
        self.history = []

    # ---------------------------------------------------------

    def record(self, reward: float):
        """
        Store a game reward.
        """
        self.history.append(reward)

    # ---------------------------------------------------------

    def average_reward(self) -> float:
        """
        Compute the average reward.
        """
        if not self.history:
            return 0.0

        return sum(self.history) / len(self.history)

    # ---------------------------------------------------------

    def best_reward(self):
        """
        Return the highest reward.
        """
        if not self.history:
            return None

        return max(self.history)

    # ---------------------------------------------------------

    def games_played(self) -> int:
        """
        Number of recorded games.
        """
        return len(self.history)

    # ---------------------------------------------------------

    def reset(self):
        """
        Remove all recorded games.
        """
        self.history.clear()
        