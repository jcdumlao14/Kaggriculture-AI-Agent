"""
profitability.py

Economic evaluation utilities for the Kaggriculture AI Agent.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.crops import CROPS


class Profitability:
    """
    Computes profit-related metrics for crops.
    """

    def __init__(self, parser):
        self.parser = parser
        self.market = parser.prices

    # ---------------------------------------------------------
    # Current Market Price
    # ---------------------------------------------------------

    def market_price(self, crop: str) -> float:
        """
        Return today's market price.
        """

        info = CROPS[crop]

        return self.market.get(crop, info.base_price)

    # ---------------------------------------------------------
    # Revenue
    # ---------------------------------------------------------

    def revenue(self, crop: str) -> float:
        """
        Expected gross revenue.
        """

        info = CROPS[crop]

        return self.market_price(crop) * info.max_yield

    # ---------------------------------------------------------
    # Cost
    # ---------------------------------------------------------

    def total_cost(self, crop: str) -> float:
        """
        Total planting cost.
        """

        info = CROPS[crop]

        return info.seed_cost + info.action_cost

    # ---------------------------------------------------------
    # Net Profit
    # ---------------------------------------------------------

    def profit(self, crop: str) -> float:
        """
        Net expected profit.
        """

        return self.revenue(crop) - self.total_cost(crop)

    # ---------------------------------------------------------
    # ROI
    # ---------------------------------------------------------

    def roi(self, crop: str) -> float:
        """
        Return on investment.
        """

        cost = self.total_cost(crop)

        if cost == 0:
            return 0

        return self.profit(crop) / cost

    # ---------------------------------------------------------
    # Profit Per Day
    # ---------------------------------------------------------

    def profit_per_day(self, crop: str) -> float:
        """
        Expected daily profit.
        """

        info = CROPS[crop]

        days = max(info.first_yield_day, 1)

        return self.profit(crop) / days

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def summary(self, crop: str):

        return {
            "crop": crop,
            "price": self.market_price(crop),
            "revenue": self.revenue(crop),
            "cost": self.total_cost(crop),
            "profit": self.profit(crop),
            "roi": self.roi(crop),
            "profit_per_day": self.profit_per_day(crop),
        }