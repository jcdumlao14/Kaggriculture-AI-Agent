"""
money_manager.py

Money management module for the Kaggriculture AI Agent.

Controls spending, savings, and investment decisions.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class MoneyManager:
    """
    Handles farm finances.
    """

    def __init__(self, parser):

        self.parser = parser
        self.money = parser.money

    # ---------------------------------------------------------
    # Cash Reserve
    # ---------------------------------------------------------

    def reserve(self) -> int:
        """
        Minimum cash to always keep.
        """

        return 500

    # ---------------------------------------------------------

    def available_cash(self) -> int:
        """
        Money available for spending.
        """

        return max(0, self.money - self.reserve())

    # ---------------------------------------------------------

    def can_afford(self, cost: int) -> bool:
        """
        Check whether an item can be purchased.
        """

        return self.available_cash() >= cost

    # ---------------------------------------------------------

    def should_save(self) -> bool:
        """
        True if money is running low.
        """

        return self.money < self.reserve()

    # ---------------------------------------------------------

    def spending_ratio(self) -> float:
        """
        Percentage of money available for investment.
        """

        if self.money <= 0:
            return 0.0

        return self.available_cash() / self.money

    # ---------------------------------------------------------

    def summary(self):

        return {
            "money": self.money,
            "reserve": self.reserve(),
            "available": self.available_cash(),
            "saving": self.should_save(),
        }