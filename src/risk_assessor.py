"""
risk_assessor.py

Risk Assessment Engine for the Kaggriculture AI Agent.

Estimates the risk associated with potential actions.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class RiskAssessor:
    """
    Estimates action risk.
    """

    def __init__(self):
        self.risk_table = {
            "HARVEST": 0.05,
            "WATER": 0.10,
            "FEED": 0.10,
            "PLANT": 0.30,
            "BUY_PRODUCT": 0.40,
            "SELL": 0.20,
            "BUY_LAND": 0.60,
            "BUY_ANIMAL": 0.70,
            "PASS": 0.80,
        }

    # ---------------------------------------------------------

    def risk(self, action: str) -> float:
        """
        Return risk score for an action.
        """

        return self.risk_table.get(action, 0.50)

    # ---------------------------------------------------------

    def safe(self, action: str) -> bool:
        """
        Determine whether an action is considered safe.
        """

        return self.risk(action) < 0.50

    # ---------------------------------------------------------

    def dangerous(self, action: str) -> bool:
        """
        Determine whether an action is considered risky.
        """

        return self.risk(action) >= 0.50

    # ---------------------------------------------------------

    def safest(self, actions):
        """
        Return the action with the lowest risk.
        """

        if not actions:
            return None

        return min(actions, key=self.risk)

    # ---------------------------------------------------------

    def riskiest(self, actions):
        """
        Return the action with the highest risk.
        """

        if not actions:
            return None

        return max(actions, key=self.risk)

    # ---------------------------------------------------------

    def summary(self):
        """
        Return the risk table.
        """

        return dict(self.risk_table)