"""
strategy.py

High-level strategy module for the Kaggriculture AI Agent.

The Strategy decides the overall objective for the
current game state. It does not generate actions.

Author: Jocelyn Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class Strategy:
    """
    Determines the current high-level farming strategy.
    """

    def __init__(self, parser):

        self.parser = parser

        self.day = parser.day
        self.hour = parser.hour

        self.player = parser.player
        self.money = parser.money

    # ---------------------------------------------------------
    # Current Strategy
    # ---------------------------------------------------------

    def current_strategy(self):
        """
        Return the current strategy.

        Returns
        -------
        str
        """

        if self.day < 5:
            return "EARLY_GAME"

        if self.day < 15:
            return "EXPANSION"

        if self.day < 25:
            return "PRODUCTION"

        return "END_GAME"

    # ---------------------------------------------------------
    # Expansion
    # ---------------------------------------------------------

    def should_expand(self):
        """
        Decide whether land expansion is worthwhile.
        """

        return self.money >= 1000

    # ---------------------------------------------------------
    # Hiring
    # ---------------------------------------------------------

    def should_hire(self):
        """
        Decide whether another farm hand should be hired.
        """

        return self.money >= 1500

    # ---------------------------------------------------------
    # Animals
    # ---------------------------------------------------------

    def should_buy_animals(self):
        """
        Decide whether to invest in livestock.
        """

        return self.day >= 10 and self.money >= 500

    # ---------------------------------------------------------
    # Fertilizer
    # ---------------------------------------------------------

    def use_fertilizer(self):
        """
        Decide whether fertilizer should be used.
        """

        return self.day >= 8

    # ---------------------------------------------------------
    # Market
    # ---------------------------------------------------------

    def sell_aggressively(self):
        """
        Sell immediately during the final week.
        """

        return self.day >= 24