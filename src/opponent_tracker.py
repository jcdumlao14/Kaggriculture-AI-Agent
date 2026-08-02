"""
opponent_tracker.py

Tracks the opponent's farm state and strategy.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class OpponentTracker:
    """
    Tracks information about the opposing player.
    """

    def __init__(self):
        self.previous_money = None
        self.current_money = None

    # ---------------------------------------------------------

    def update(self, observation: dict):
        """
        Update opponent information from the latest observation.
        """

        opponent = 1 - observation["player"]

        self.previous_money = self.current_money
        self.current_money = observation["farms"][opponent]["money"]

    # ---------------------------------------------------------

    def money_change(self) -> int:
        """
        Return the change in opponent money.
        """

        if self.previous_money is None:
            return 0

        return self.current_money - self.previous_money

    # ---------------------------------------------------------

    def expanding(self) -> bool:
        """
        Detect whether the opponent appears to be spending heavily.
        """

        return self.money_change() < -1000

    # ---------------------------------------------------------

    def getting_richer(self) -> bool:
        """
        Detect whether the opponent is earning significant income.
        """

        return self.money_change() > 1000