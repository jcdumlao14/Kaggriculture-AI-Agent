"""
economy.py

Economic analysis for the Kaggriculture AI Agent.

Computes ROI, profit, and crop rankings.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CropEconomics:

    seed_cost: int
    sell_price: int
    grow_days: int
    max_yield: int

    @property
    def revenue(self):

        return self.sell_price * self.max_yield

    @property
    def profit(self):

        return self.revenue - self.seed_cost

    @property
    def roi(self):

        return self.profit / self.seed_cost

    @property
    def profit_per_day(self):

        return self.profit / self.grow_days


class Economy:

    """
    Performs economic calculations.
    """

    def __init__(self):

        self.crops = {

            "WHEAT": CropEconomics(
                seed_cost=10,
                sell_price=25,
                grow_days=4,
                max_yield=6,
            ),

            "CARROT": CropEconomics(
                seed_cost=20,
                sell_price=35,
                grow_days=3,
                max_yield=4,
            ),

            "TOMATO": CropEconomics(
                seed_cost=50,
                sell_price=60,
                grow_days=8,
                max_yield=4,
            ),

            "STRAWBERRY": CropEconomics(
                seed_cost=100,
                sell_price=120,
                grow_days=10,
                max_yield=4,
            ),

            "MELON": CropEconomics(
                seed_cost=80,
                sell_price=250,
                grow_days=12,
                max_yield=6,
            ),
        }

    # ------------------------------------------------------

    def best_crop(self):

        """
        Highest ROI.
        """

        return max(
            self.crops.items(),
            key=lambda x: x[1].roi,
        )

    # ------------------------------------------------------

    def best_profit(self):

        """
        Highest total profit.
        """

        return max(
            self.crops.items(),
            key=lambda x: x[1].profit,
        )

    # ------------------------------------------------------

    def fastest_profit(self):

        """
        Highest daily profit.
        """

        return max(
            self.crops.items(),
            key=lambda x: x[1].profit_per_day,
        )

    # ------------------------------------------------------

    def summary(self):

        result = {}

        for name, crop in self.crops.items():

            result[name] = {

                "ROI": round(crop.roi, 2),

                "Profit": crop.profit,

                "Profit/Day": round(crop.profit_per_day, 2),

            }

        return result