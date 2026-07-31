"""
scoring.py

Crop scoring engine for the Kaggriculture AI Agent.

Evaluates crops and selects the best planting choice.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.crops import CROPS


class CropScorer:
    """
    Scores every crop according to expected profitability.
    """

    def __init__(self, parser):

        self.parser = parser

    # ---------------------------------------------------------
    # ROI
    # ---------------------------------------------------------

    def roi(self, crop_name: str) -> float:
        """
        Return the return-on-investment.
        """

        crop = CROPS[crop_name]

        return (crop.base_price - crop.seed_cost) / crop.seed_cost

    # ---------------------------------------------------------
    # Can Grow?
    # ---------------------------------------------------------

    def can_finish(self, crop_name: str) -> bool:
        """
        Check whether there is enough season left.
        """

        crop = CROPS[crop_name]

        if crop.first_yield_day is None:
            return True

        days_remaining = 30 - self.parser.day

        return crop.first_yield_day <= days_remaining

    # ---------------------------------------------------------
    # Afford?
    # ---------------------------------------------------------

    def affordable(self, crop_name: str) -> bool:

        crop = CROPS[crop_name]

        return self.parser.money >= crop.seed_cost

    # ---------------------------------------------------------
    # Score
    # ---------------------------------------------------------

    def score(self, crop_name: str) -> float:

        if not self.can_finish(crop_name):
            return -1

        if not self.affordable(crop_name):
            return -1

        crop = CROPS[crop_name]

        score = 0

        # Profit
        score += crop.base_price

        # Cheap seeds
        score -= crop.seed_cost * 0.30

        # ROI
        score += self.roi(crop_name) * 20

        return score

    # ---------------------------------------------------------
    # Best Crop
    # ---------------------------------------------------------

    def best_crop(self):

        scores = {
            crop: self.score(crop)
            for crop in CROPS
        }

        return max(scores, key=scores.get)