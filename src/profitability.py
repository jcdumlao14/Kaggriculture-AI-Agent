"""
profitability.py

Profit calculation utilities for Kaggriculture AI.
"""

from __future__ import annotations


class ProfitCalculator:
    """
    Calculates simple crop profitability from market prices.
    """

    def __init__(self, parser):
        self.parser = parser

        # Example seed costs (replace with official values later if needed)
        self.seed_costs = {
            "WHEAT": 50,
            "CARROT": 80,
            "TOMATO": 120,
            "STRAWBERRY": 180,
            "MELON": 250,
        }

    def profit(self, crop: str) -> float:
        sell_price = self.parser.prices.get(crop, 0)
        seed_cost = self.seed_costs.get(crop, 0)
        return sell_price - seed_cost

    def all_profits(self):
        return {
            crop: self.profit(crop)
            for crop in self.seed_costs
        }

    def best_crop(self):
        profits = self.all_profits()
        return max(profits, key=profits.get)