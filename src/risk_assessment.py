"""
risk_assessment.py

Risk evaluation for the Kaggriculture AI Agent.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class RiskAssessment:
    """
    Evaluate economic risk before making decisions.
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------

    def price_volatility(self, history: list[float]) -> float:
        """
        Calculate the price range.
        """

        if len(history) < 2:
            return 0.0

        return max(history) - min(history)

    # ---------------------------------------------------------

    def is_stable(self, history: list[float]) -> bool:
        """
        Return True if prices have been relatively stable.
        """

        return self.price_volatility(history) <= 20

    # ---------------------------------------------------------

    def risk_score(self, history: list[float]) -> float:
        """
        Compute a normalized risk score.
        """

        if len(history) < 2:
            return 0.0

        average = sum(history) / len(history)

        if average == 0:
            return 0.0

        return self.price_volatility(history) / average

    # ---------------------------------------------------------

    def should_invest(self, history: list[float]) -> bool:
        """
        Recommend investment when market risk is acceptable.
        """

        return self.risk_score(history) < 0.25