"""
crop_strategy.py

Intelligent crop selection.

Chooses the most profitable crop based on
expected selling price, seed cost, growth time,
and yield.

Author: Jocelyn Dumlao
"""

from __future__ import annotations

from src.crops import CROPS


class CropStrategy:
    """
    Select the best crop to plant.
    """

    def __init__(self, parser):
        self.parser = parser
        self.market = parser.prices

    # -----------------------------------------------------

    def expected_profit(self, crop: str) -> float:
        """
        Estimate expected profit for one planting cycle.
        """

        info = CROPS[crop]

        # Use current market price if available.
        # Otherwise fall back to the crop's base price.
        price = self.market.get(crop, info.base_price)

        revenue = price * info.max_yield

        cost = info.seed_cost

        return revenue - cost

    # -----------------------------------------------------

    def rank_crops(self):
        """
        Return crops sorted by profitability.
        """

        ranking = []

        for crop in CROPS:

            ranking.append(
                (
                    crop,
                    self.expected_profit(crop),
                )
            )

        ranking.sort(
            key=lambda x: x[1],
            reverse=True,
        )

        return ranking

    # -----------------------------------------------------

    def best_crop(self):
        """
        Return the most profitable crop.
        """

        return self.rank_crops()[0][0]

    # -----------------------------------------------------
    # Crop Score
    # -----------------------------------------------------

    def crop_score(self, crop: str) -> float:
        """
        Calculate an overall score for a crop.

        Higher score = better crop.
        """

        info = CROPS[crop]

        # Base profit
        profit = self.expected_profit(crop)

        # Faster crops are generally better
        growth_bonus = max(
            0,
            15 - info.first_yield_day,
        )

        # More harvest units are better
        yield_bonus = info.max_yield * 5

        # Expensive seeds are slightly penalized
        cost_penalty = info.seed_cost * 0.10

        return (
            profit
            + growth_bonus
            + yield_bonus
            - cost_penalty
        )

    # -----------------------------------------------------
    # Game-Aware Crop Scoring
    # -----------------------------------------------------

    def adjusted_crop_score(self, crop: str) -> float:
        """
        Adjust crop score based on the current game day.
        """

        score = self.crop_score(crop)

        day = self.parser.day

        info = CROPS[crop]

        # Early game: reward fast-growing crops
        if day <= 5:
            score += max(0, 12 - info.first_yield_day) * 8

        # Late game: penalize crops that won't mature in time
        days_remaining = 30 - day

        if info.first_yield_day > days_remaining:
            score -= 10000

        return score