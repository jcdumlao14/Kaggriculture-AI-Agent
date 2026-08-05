"""
action_scoring_engine.py

Action Scoring Engine for the Kaggriculture AI Agent.

Scores candidate actions using evaluation components.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ActionScoringEngine:
    """
    Scores candidate actions.
    """

    ACTION_BONUSES = {
        "HARVEST": 50.0,
        "PLANT": 25.0,
        "WATER": 10.0,
        "FERTILIZE": 15.0,
        "BUY": 5.0,
        "SELL": 20.0,
        "FEED": 10.0,
        "COLLECT": 30.0,
        "EXPAND": 40.0,
    }

    def score(
        self,
        *,
        action: str,
        farm_score: float = 0.0,
        crop_profit: float = 0.0,
        animal_profit: float = 0.0,
        market_score: float = 0.0,
    ) -> float:
        """
        Compute a score for a candidate action.
        """

        bonus = self.ACTION_BONUSES.get(
            action.upper(),
            0.0,
        )

        return (
            farm_score
            + crop_profit
            + animal_profit
            + market_score
            + bonus
        )

    # ---------------------------------------------------------

    def action_bonus(
        self,
        action: str,
    ) -> float:
        """
        Return the configured bonus for an action.
        """

        return self.ACTION_BONUSES.get(
            action.upper(),
            0.0,
        )

    # ---------------------------------------------------------

    def supported_actions(self):
        """
        Return supported action names.
        """

        return sorted(self.ACTION_BONUSES.keys())

    # ---------------------------------------------------------

    def is_supported(
        self,
        action: str,
    ) -> bool:
        """
        Return True if the action has a configured bonus.
        """

        return action.upper() in self.ACTION_BONUSES