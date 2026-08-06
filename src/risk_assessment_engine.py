"""
risk_assessment_engine.py

Risk Assessment Engine for the Kaggriculture AI Agent.

Evaluates the relative risk of candidate actions.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class RiskAssessmentEngine:
    """
    Estimates action risk.
    """

    RISK = {
        "HARVEST": 10.0,
        "SELL": 15.0,
        "PLANT": 30.0,
        "BUY": 40.0,
        "BUY_SEED": 35.0,
        "EXPAND": 60.0,
        "WATER": 5.0,
        "FERTILIZE": 8.0,
        "FEED": 5.0,
        "COLLECT": 12.0,
    }

    # ---------------------------------------------------------

    def risk(
        self,
        action: str,
    ) -> float:
        """
        Return the configured risk.
        """

        return float(
            self.RISK.get(
                action.upper(),
                50.0,
            )
        )

    # ---------------------------------------------------------

    def safest_action(
        self,
        actions: list[str],
    ) -> str | None:
        """
        Return the lowest-risk action.
        """

        if not actions:
            return None

        return min(
            actions,
            key=self.risk,
        )

    # ---------------------------------------------------------

    def highest_risk(
        self,
        actions: list[str],
    ) -> str | None:
        """
        Return the highest-risk action.
        """

        if not actions:
            return None

        return max(
            actions,
            key=self.risk,
        )

    # ---------------------------------------------------------

    def is_safe(
        self,
        action: str,
        threshold: float = 20.0,
    ) -> bool:
        """
        Return True if the action is below the risk threshold.
        """

        return self.risk(action) <= threshold

    # ---------------------------------------------------------

    def supported_actions(
        self,
    ) -> list[str]:
        """
        Return supported actions.
        """

        return sorted(self.RISK.keys())