"""
opponent_analyzer.py

Opponent behavior analysis for the Kaggriculture AI Agent.

Tracks historical opponent actions and identifies
their dominant strategy.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class OpponentAnalyzer:
    """
    Learns opponent tendencies.
    """

    def __init__(self):
        self.actions = []

    # ---------------------------------------------------------

    def record(self, action: str):
        """
        Record one observed opponent action.
        """

        self.actions.append(action)

    # ---------------------------------------------------------

    def total_actions(self):
        """
        Total recorded actions.
        """

        return len(self.actions)

    # ---------------------------------------------------------

    def frequency(self, action: str):
        """
        Count how often an action occurred.
        """

        return self.actions.count(action)

    # ---------------------------------------------------------

    def most_common(self):
        """
        Return the opponent's most frequent action.
        """

        if not self.actions:
            return None

        counts = {}

        for action in self.actions:
            counts[action] = counts.get(action, 0) + 1

        return max(counts, key=counts.get)

    # ---------------------------------------------------------

    def aggression_score(self):
        """
        Estimate aggression from expansion-oriented actions.
        """

        aggressive = {
            "BUY_LAND",
            "PLANT",
            "BUY_ANIMAL",
        }

        if not self.actions:
            return 0.0

        total = sum(
            1 for action in self.actions
            if action in aggressive
        )

        return total / len(self.actions)

    # ---------------------------------------------------------

    def reset(self):
        """
        Clear all observations.
        """

        self.actions.clear()