"""
performance_analyzer.py

Performance Analytics Engine for the Kaggriculture AI Agent.

Tracks long-term statistics about the AI's decisions.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class PerformanceAnalyzer:
    """
    Collects long-term statistics.
    """

    def __init__(self):

        self.turns = 0
        self.harvests = 0
        self.plants = 0
        self.market_trades = 0
        self.total_profit = 0.0
        self.utility_scores = []

    # ---------------------------------------------------------

    def record_turn(self):
        self.turns += 1

    # ---------------------------------------------------------

    def record_harvest(self):
        self.harvests += 1

    # ---------------------------------------------------------

    def record_plant(self):
        self.plants += 1

    # ---------------------------------------------------------

    def record_trade(self):
        self.market_trades += 1

    # ---------------------------------------------------------

    def add_profit(self, amount: float):
        self.total_profit += amount

    # ---------------------------------------------------------

    def add_utility(self, score: float):
        self.utility_scores.append(score)

    # ---------------------------------------------------------

    def average_utility(self):

        if not self.utility_scores:
            return 0.0

        return sum(self.utility_scores) / len(self.utility_scores)

    # ---------------------------------------------------------

    def summary(self):

        return {
            "turns": self.turns,
            "harvests": self.harvests,
            "plants": self.plants,
            "market_trades": self.market_trades,
            "profit": self.total_profit,
            "average_utility": round(
                self.average_utility(),
                2,
            ),
        }

    # ---------------------------------------------------------

    def reset(self):

        self.__init__()