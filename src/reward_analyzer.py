"""
reward_analyzer.py

Reward Analyzer for the Kaggriculture AI Agent.

Analyzes reward trends across reinforcement learning episodes.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class RewardAnalyzer:
    """
    Analyze reward history.
    """

    def __init__(self, rewards):
        self.rewards = list(rewards)

    # ---------------------------------------------------------

    def improving(self) -> bool:
        """
        Returns True if rewards are generally increasing.
        """

        if len(self.rewards) < 2:
            return False

        return self.rewards[-1] > self.rewards[0]

    # ---------------------------------------------------------

    def plateau(self) -> bool:
        """
        Returns True if all rewards are identical.
        """

        if not self.rewards:
            return False

        return len(set(self.rewards)) == 1

    # ---------------------------------------------------------

    def regression(self) -> bool:
        """
        Returns True if performance has declined.
        """

        if len(self.rewards) < 2:
            return False

        return self.rewards[-1] < self.rewards[0]

    # ---------------------------------------------------------

    def growth(self) -> float:
        """
        Net reward growth.
        """

        if len(self.rewards) < 2:
            return 0.0

        return self.rewards[-1] - self.rewards[0]

    # ---------------------------------------------------------

    def best_jump(self) -> float:
        """
        Largest positive improvement between consecutive episodes.
        """

        if len(self.rewards) < 2:
            return 0.0

        jumps = [
            self.rewards[i + 1] - self.rewards[i]
            for i in range(len(self.rewards) - 1)
        ]

        return max(jumps)
    