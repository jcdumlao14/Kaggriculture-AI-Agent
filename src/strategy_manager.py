"""
strategy_manager.py

High-level strategy selection for the Kaggriculture AI Agent.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class StrategyManager:
    """
    Select the AI's overall strategy based on
    goals, season, and risk.
    """

    def __init__(self):
        self.strategy = "BALANCED"

    # ---------------------------------------------------------

    def update(
        self,
        goal: str,
        risk: float,
        day: int,
    ):
        """
        Update the active strategy.
        """

        if day >= 28:
            self.strategy = "ENDGAME"

        elif goal == "SAVE_MONEY":
            self.strategy = "CONSERVATIVE"

        elif goal == "EXPAND_FARM":
            self.strategy = "EXPANSION"

        elif risk > 0.7:
            self.strategy = "SAFE"

        else:
            self.strategy = "BALANCED"

    # ---------------------------------------------------------

    def current(self):
        """
        Return the current strategy.
        """

        return self.strategy

    # ---------------------------------------------------------

    def is_strategy(self, name: str):
        """
        Check whether the strategy matches.
        """

        return self.strategy == name

    # ---------------------------------------------------------

    def reset(self):
        """
        Reset to the default strategy.
        """

        self.strategy = "BALANCED"