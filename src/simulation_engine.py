"""
simulation_engine.py

Simulation Engine for the Kaggriculture AI Agent.

Performs lightweight look-ahead evaluation of
candidate strategies.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class SimulationEngine:
    """
    Simulate future outcomes for candidate strategies.
    """

    def __init__(self):
        self.results = []

    # ---------------------------------------------------------

    def simulate(self, strategy: str, reward: float):

        self.results.append(
            {
                "strategy": strategy,
                "reward": reward,
            }
        )

    # ---------------------------------------------------------

    def best(self):

        if not self.results:
            return None

        return max(
            self.results,
            key=lambda r: r["reward"],
        )

    # ---------------------------------------------------------

    def ranking(self):

        return sorted(
            self.results,
            key=lambda r: r["reward"],
            reverse=True,
        )

    # ---------------------------------------------------------

    def clear(self):

        self.results.clear()

    # ---------------------------------------------------------

    def __len__(self):

        return len(self.results)