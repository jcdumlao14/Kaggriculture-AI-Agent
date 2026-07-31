"""
market.py

Market intelligence module.

Evaluates prices, buying opportunities,
selling opportunities, and profitability.
"""

from __future__ import annotations

from src.constants import Crop


class Market:
    """
    Handles market analysis.

    Uses current prices from the observation.
    """

    def __init__(self, parser):

        self.parser = parser

        self.market = parser.market

        self.prices = self.market.get("prices", {})

        self.inventory = self.market.get("inventory", {})

    # -----------------------------------------------------
    # Price
    # -----------------------------------------------------

    def price(self, product):

        return self.prices.get(product, 0)

    # -----------------------------------------------------
    # Inventory
    # -----------------------------------------------------

    def inventory_level(self, product):

        return self.inventory.get(product, 0)

    # -----------------------------------------------------
    # Expensive?
    # -----------------------------------------------------

    def is_expensive(self, product):

        base = {
            "WHEAT": 25,
            "CARROT": 35,
            "TOMATO": 60,
            "STRAWBERRY": 120,
            "MELON": 250,
            "EGG": 50,
            "MILK": 160,
            "WOOL": 200,
            "FERTILIZER": 100,
        }

        return self.price(product) > base.get(product, 0)

    # -----------------------------------------------------
    # Cheap?
    # -----------------------------------------------------

    def is_cheap(self, product):

        base = {
            "WHEAT": 25,
            "CARROT": 35,
            "TOMATO": 60,
            "STRAWBERRY": 120,
            "MELON": 250,
            "EGG": 50,
            "MILK": 160,
            "WOOL": 200,
            "FERTILIZER": 100,
        }

        return self.price(product) < base.get(product, 0)

    # -----------------------------------------------------
    # Best Crop
    # -----------------------------------------------------

    def best_crop(self):

        profits = {
            Crop.WHEAT.value: self.price("WHEAT") - 10,
            Crop.CARROT.value: self.price("CARROT") - 20,
            Crop.TOMATO.value: self.price("TOMATO") - 50,
            Crop.STRAWBERRY.value: self.price("STRAWBERRY") - 100,
            Crop.MELON.value: self.price("MELON") - 80,
        }

        return max(profits, key=profits.get)

    # -----------------------------------------------------
    # Sell?
    # -----------------------------------------------------

    def should_sell(self, product):

        return self.is_expensive(product)

    # -----------------------------------------------------
    # Buy Fertilizer?
    # -----------------------------------------------------

    def should_buy_fertilizer(self):

        return self.is_cheap("FERTILIZER")

    # -----------------------------------------------------
    # Buy Wheat?
    # -----------------------------------------------------

    def should_buy_wheat(self):

        return self.is_cheap("WHEAT")

    # -----------------------------------------------------
    # Summary
    # -----------------------------------------------------

    def summary(self):

        return {
            "best_crop": self.best_crop(),
            "buy_fertilizer": self.should_buy_fertilizer(),
            "buy_wheat": self.should_buy_wheat(),
        }