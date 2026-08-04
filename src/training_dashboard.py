"""
training_dashboard.py

Training Dashboard Backend for the Kaggriculture AI Agent.

Reads training logs and computes statistics for visualization.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

import json
from pathlib import Path


class TrainingDashboard:
    """
    Backend analytics for training logs.
    """

    def __init__(self, filename):
        self.path = Path(filename)

    # ---------------------------------------------------------

    def load(self):
        """
        Load all training records.
        """

        if not self.path.exists():
            return []

        with self.path.open("r", encoding="utf-8") as f:
            return [json.loads(line) for line in f if line.strip()]

    # ---------------------------------------------------------

    def rewards(self):
        """
        Return reward history.
        """

        return [record["reward"] for record in self.load()]

    # ---------------------------------------------------------

    def best_reward(self):
        """
        Return highest reward.
        """

        rewards = self.rewards()

        return max(rewards) if rewards else 0

    # ---------------------------------------------------------

    def average_reward(self):
        """
        Return average reward.
        """

        rewards = self.rewards()

        if not rewards:
            return 0

        return sum(rewards) / len(rewards)

    # ---------------------------------------------------------

    def moving_average(self, window=3):
        """
        Compute moving average.
        """

        rewards = self.rewards()

        if len(rewards) < window:
            return []

        averages = []

        for i in range(len(rewards) - window + 1):
            values = rewards[i:i + window]
            averages.append(sum(values) / window)

        return averages

    # ---------------------------------------------------------

    def summary(self):
        """
        Return dashboard summary.
        """

        rewards = self.rewards()

        return {
            "episodes": len(rewards),
            "best_reward": self.best_reward(),
            "average_reward": self.average_reward(),
            "latest_reward": rewards[-1] if rewards else 0,
        }