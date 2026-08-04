"""
training_statistics.py

Training Statistics for the Kaggriculture AI Agent.

Tracks reinforcement learning performance across episodes.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class TrainingStatistics:
    """
    Collects training metrics.
    """

    def __init__(self):
        self.rewards = []

    # ---------------------------------------------------------

    def add_episode(self, reward: float):
        """
        Record an episode reward.
        """
        self.rewards.append(reward)

    # ---------------------------------------------------------

    def total_episodes(self) -> int:
        """
        Number of completed episodes.
        """
        return len(self.rewards)

    # ---------------------------------------------------------

    def best_reward(self) -> float:
        """
        Highest reward obtained.
        """
        if not self.rewards:
            return 0.0

        return max(self.rewards)

    # ---------------------------------------------------------

    def worst_reward(self) -> float:
        """
        Lowest reward obtained.
        """
        if not self.rewards:
            return 0.0

        return min(self.rewards)

    # ---------------------------------------------------------

    def average_reward(self) -> float:
        """
        Mean reward.
        """
        if not self.rewards:
            return 0.0

        return sum(self.rewards) / len(self.rewards)

    # ---------------------------------------------------------

    def latest_reward(self) -> float:
        """
        Most recent reward.
        """
        if not self.rewards:
            return 0.0

        return self.rewards[-1]

    # ---------------------------------------------------------

    def summary(self):
        """
        Return all statistics.
        """
        return {
            "episodes": self.total_episodes(),
            "best": self.best_reward(),
            "worst": self.worst_reward(),
            "average": self.average_reward(),
            "latest": self.latest_reward(),
        }

    # ---------------------------------------------------------

    def reset(self):
        """
        Clear all statistics.
        """
        self.rewards.clear()