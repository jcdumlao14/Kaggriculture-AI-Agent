"""
monte_carlo.py

Monte Carlo Simulator for the Kaggriculture AI Agent.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class MonteCarlo:
    """
    Stores multiple simulation outcomes and computes
    average rewards.
    """

    def __init__(self):
        self.results = {}

    def add(self, strategy: str, reward: float):

        self.results.setdefault(strategy, []).append(reward)

    def average(self, strategy: str):

        rewards = self.results.get(strategy, [])

        if not rewards:
            return 0.0

        return sum(rewards) / len(rewards)

    def best(self):

        if not self.results:
            return None

        return max(
            self.results,
            key=lambda strategy: self.average(strategy),
        )

    def clear(self):

        self.results.clear()

    def __len__(self):

        return len(self.results)