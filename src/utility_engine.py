"""
utility_engine.py

Utility Scoring Engine for the Kaggriculture AI Agent.

Combines multiple AI modules into a single decision score.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class UtilityEngine:
    """
    Combines reward and penalties into one score.
    """

    def __init__(self):

        self.weights = {
            "profit": 0.35,
            "season": 0.15,
            "inventory": 0.10,
            "money": 0.10,
            "goal": 0.10,
            "opponent": 0.10,
            "risk": 0.10,
        }

    # ---------------------------------------------------------

    def score(
        self,
        *,
        profit=0,
        season=0,
        inventory=0,
        money=0,
        goal=0,
        opponent=0,
        risk=0,
    ):
        """
        Compute weighted utility score.
        """

        return (
            profit * self.weights["profit"]
            + season * self.weights["season"]
            + inventory * self.weights["inventory"]
            + money * self.weights["money"]
            + goal * self.weights["goal"]
            + opponent * self.weights["opponent"]
            - risk * self.weights["risk"]
        )

    # ---------------------------------------------------------

    def better(self, score_a, score_b):
        """
        Return True if score_a is better.
        """

        return score_a > score_b

    # ---------------------------------------------------------

    def best(self, scored_actions):
        """
        Return the action with the highest score.

        Parameters
        ----------
        scored_actions : list[(action, score)]
        """

        if not scored_actions:
            return None

        return max(
            scored_actions,
            key=lambda item: item[1],
        )

    # ---------------------------------------------------------

    def normalize(self, value, maximum):

        if maximum <= 0:
            return 0

        return value / maximum

    # ---------------------------------------------------------

    def summary(self):

        return dict(self.weights)