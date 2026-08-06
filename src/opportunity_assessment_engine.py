"""
opportunity_assessment_engine.py

Opportunity Assessment Engine for the Kaggriculture AI Agent.

Estimates the opportunity value of candidate actions.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class OpportunityAssessmentEngine:
    """
    Estimates opportunity values.
    """

    OPPORTUNITY = {
        "HARVEST": 90.0,
        "SELL": 85.0,
        "PLANT": 70.0,
        "BUY": 50.0,
        "BUY_SEED": 60.0,
        "EXPAND": 95.0,
        "WATER": 40.0,
        "FERTILIZE": 45.0,
        "FEED": 35.0,
        "COLLECT": 55.0,
    }

    # ---------------------------------------------------------

    def value(
        self,
        action: str,
    ) -> float:
        """
        Return opportunity value.
        """

        return float(
            self.OPPORTUNITY.get(
                action.upper(),
                0.0,
            )
        )

    # ---------------------------------------------------------

    def best_action(
        self,
        actions: list[str],
    ) -> str | None:
        """
        Return highest-value action.
        """

        if not actions:
            return None

        return max(
            actions,
            key=self.value,
        )

    # ---------------------------------------------------------

    def worst_action(
        self,
        actions: list[str],
    ) -> str | None:
        """
        Return lowest-value action.
        """

        if not actions:
            return None

        return min(
            actions,
            key=self.value,
        )

    # ---------------------------------------------------------

    def worthwhile(
        self,
        action: str,
        threshold: float = 50.0,
    ) -> bool:
        """
        Return True if action exceeds threshold.
        """

        return self.value(action) >= threshold

    # ---------------------------------------------------------

    def supported_actions(
        self,
    ) -> list[str]:
        """
        Return supported actions.
        """

        return sorted(
            self.OPPORTUNITY.keys()
        )