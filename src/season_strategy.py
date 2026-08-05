"""
season_strategy.py

Season-aware strategy for the Kaggriculture AI Agent.

Determines how the agent should adapt its behavior
based on the current day of the season.

Author: Jocelyn Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class SeasonStrategy:
    """
    Provides season-aware decision rules.
    """

    SEASON_LENGTH = 30

    def __init__(self, parser):
        """
        Initialize the strategy using an ObservationParser.
        """
        self.day = parser.day

    # ---------------------------------------------------------

    def remaining_days(self) -> int:
        """
        Return the number of days remaining in the season.

        Never returns a negative value.
        """
        return max(
            0,
            self.SEASON_LENGTH - self.day,
        )

    # ---------------------------------------------------------

    def phase(self) -> str:
        """
        Return the current phase of the season.
        """

        if self.day <= 8:
            return "EARLY"

        if self.day <= 20:
            return "MID"

        if self.day <= 26:
            return "LATE"

        return "END"

    # ---------------------------------------------------------

    def should_invest(self) -> bool:
        """
        Return True if long-term investments are worthwhile.
        """
        return self.phase() in (
            "EARLY",
            "MID",
        )

    # ---------------------------------------------------------

    def should_sell_all(self) -> bool:
        """
        Return True during the final days of the season.
        """
        return self.phase() == "END"

    # ---------------------------------------------------------

    def can_plant(
        self,
        growth_days: int,
    ) -> bool:
        """
        Return True if a crop can mature before
        the season ends.
        """
        return growth_days <= self.remaining_days()