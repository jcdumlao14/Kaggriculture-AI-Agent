"""
market.py

Market Intelligence module for the Kaggriculture AI Agent.

Analyzes market prices and provides simple trading
recommendations.

Author: Jocelyn Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class Market:
    """
    Market analysis.
    """

    def __init__(self, parser):

        self.parser = parser

        self.market = parser.market

        self.inventory = self.market.get("inventory", {})
        self.prices = self.market.get("prices", {})

    # ---------------------------------------------------------
    # Basic Information
    # ---------------------------------------------------------

    def price(self, product: str) -> int:
        """
        Current market price.
        """
        return self.prices.get(product, 0)

    def inventory_level(self, product: str) -> int:
        """
        Current market inventory.
        """
        return self.inventory.get(product, 0)

    # ---------------------------------------------------------
    # Price Evaluation
    # ---------------------------------------------------------

    def is_expensive(self, product: str, base_price: int) -> bool:
        """
        Returns True if price is above its base value.
        """
        return self.price(product) > base_price

    def is_cheap(self, product: str, base_price: int) -> bool:
        """
        Returns True if price is below its base value.
        """
        return self.price(product) < base_price

    # ---------------------------------------------------------
    # Trading Decisions
    # ---------------------------------------------------------

    def should_sell(self, product: str, base_price: int) -> bool:
        """
        Sell when price is favorable.
        """
        return self.price(product) >= base_price

    def should_buy(self, product: str, base_price: int) -> bool:
        """
        Buy when price is discounted.
        """
        return self.price(product) <= base_price

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def summary(self):
        """
        Return current market snapshot.
        """
        return {
            "prices": self.prices,
            "inventory": self.inventory,
        }