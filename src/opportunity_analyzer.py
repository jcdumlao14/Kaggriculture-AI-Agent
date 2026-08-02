"""
opportunity_analyzer.py

Opportunity evaluation for the Kaggriculture AI Agent.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class OpportunityAnalyzer:
    """
    Scores possible actions so the planner can choose
    the most valuable opportunity.
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------

    def score(
        self,
        reward: float,
        risk: float,
        urgency: float,
    ) -> float:
        """
        Calculate a weighted opportunity score.
        Higher reward and urgency increase the score,
        while higher risk decreases it.
        """

        return reward - risk + urgency

    # ---------------------------------------------------------

    def best(self, opportunities):
        """
        Return the highest-scoring opportunity.
        """

        if not opportunities:
            return None

        return max(
            opportunities,
            key=lambda item: item["score"],
        )

    # ---------------------------------------------------------

    def rank(self, opportunities):
        """
        Return opportunities sorted by score.
        """

        return sorted(
            opportunities,
            key=lambda item: item["score"],
            reverse=True,
        )