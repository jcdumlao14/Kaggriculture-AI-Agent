"""
profit_estimator.py

Profit Estimator for the Kaggriculture AI Agent.

Estimates expected profit for crops and market actions.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ProfitEstimator:
    """
    Estimates crop profitability.
    """

    # ---------------------------------------------------------

    def crop_profit(
    self,
    *,
    sell_price: float,
    seed_cost: float,
    yield_units: int,
) -> float:
        """
        Return the total expected profit.
        """

        return float(
            (sell_price * yield_units)
            - seed_cost
        )
    # ---------------------------------------------------------

    def profit_per_day(
        self,
        *,
        sell_price: float,
        seed_cost: float,
        yield_units: int,
        grow_days: int,
    ) -> float:
        """
        Return profit normalized by grow time.
        """

        if grow_days <= 0:
            grow_days = 1

        profit = self.crop_profit(
            sell_price=sell_price,
            seed_cost=seed_cost,
            yield_units=yield_units,
        )

        return profit / grow_days

    # ---------------------------------------------------------

    def better_crop(
        self,
        crop_a: dict,
        crop_b: dict,
    ) -> dict:
        """
        Return the more profitable crop.
        """

        score_a = self.profit_per_day(**crop_a)
        score_b = self.profit_per_day(**crop_b)

        return crop_a if score_a >= score_b else crop_b