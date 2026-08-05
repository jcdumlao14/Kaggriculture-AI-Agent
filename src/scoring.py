"""
scoring.py

Crop scoring engine for the Kaggriculture AI Agent.

Evaluates every crop according to profitability,
investment cost, and remaining season length.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.crops import CROPS


class CropScorer:
    """
    Scores crops according to expected profitability.
    """

    SEASON_LENGTH = 30

    # ---------------------------------------------------------

    def __init__(self, parser):

        self.parser = parser

    # ---------------------------------------------------------
    # ROI
    # ---------------------------------------------------------

    def roi(
        self,
        crop_name: str,
    ) -> float:
        """
        Return the crop ROI.
        """

        crop = CROPS[crop_name]

        if crop.seed_cost <= 0:
            return 0.0

        return (
            crop.base_price - crop.seed_cost
        ) / crop.seed_cost

    # ---------------------------------------------------------
    # Days Remaining
    # ---------------------------------------------------------

    def remaining_days(self) -> int:
        """
        Return remaining season days.
        """

        return max(
            0,
            self.SEASON_LENGTH - self.parser.day,
        )

    # ---------------------------------------------------------
    # Can Finish?
    # ---------------------------------------------------------

    def can_finish(
        self,
        crop_name: str,
    ) -> bool:
        """
        Return True if the crop can
        produce before the season ends.
        """

        crop = CROPS[crop_name]

        if crop.first_yield_day is None:
            return True

        return (
            crop.first_yield_day
            <= self.remaining_days()
        )

    # ---------------------------------------------------------
    # Affordable?
    # ---------------------------------------------------------

    def affordable(
        self,
        crop_name: str,
    ) -> bool:
        """
        Return True if enough money exists.
        """

        crop = CROPS[crop_name]

        return (
            self.parser.money
            >= crop.seed_cost
        )

    # ---------------------------------------------------------
    # Profit
    # ---------------------------------------------------------

    def expected_profit(
        self,
        crop_name: str,
    ) -> float:
        """
        Expected single harvest profit.
        """

        crop = CROPS[crop_name]

        return float(
            crop.base_price - crop.seed_cost
        )

    # ---------------------------------------------------------
    # Score
    # ---------------------------------------------------------

    def score(
        self,
        crop_name: str,
    ) -> float:
        """
        Return a weighted crop score.
        """

        if crop_name not in CROPS:
            return -1.0

        if not self.can_finish(crop_name):
            return -1.0

        if not self.affordable(crop_name):
            return -1.0

        crop = CROPS[crop_name]

        score = 0.0

        # ----------------------------------
        # Base selling value
        # ----------------------------------

        score += float(crop.base_price)

        # ----------------------------------
        # Seed cost penalty
        # ----------------------------------

        score -= float(crop.seed_cost) * 0.30

        # ----------------------------------
        # ROI bonus
        # ----------------------------------

        score += self.roi(crop_name) * 20.0

        # ----------------------------------
        # Fast crops receive a bonus
        # ----------------------------------

        if crop.first_yield_day is not None:

            score += max(
                0,
                10 - crop.first_yield_day,
            )

        # ----------------------------------
        # End-of-season penalty
        # ----------------------------------

        remaining = self.remaining_days()

        if (
            crop.first_yield_day is not None
            and crop.first_yield_day > remaining
        ):
            score -= 1000

        return float(score)

    # ---------------------------------------------------------
    # Rank Crops
    # ---------------------------------------------------------

    def ranked_crops(self):
        """
        Return crops ranked by score.
        """

        scores = {
            crop: self.score(crop)
            for crop in CROPS
        }

        return sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True,
        )

    # ---------------------------------------------------------
    # Best Crop
    # ---------------------------------------------------------

    def best_crop(self) -> str:
        """
        Return highest scoring crop.
        """

        return self.ranked_crops()[0][0]

    # ---------------------------------------------------------
    # Best Score
    # ---------------------------------------------------------

    def best_score(self) -> float:
        """
        Return highest crop score.
        """

        return self.ranked_crops()[0][1]