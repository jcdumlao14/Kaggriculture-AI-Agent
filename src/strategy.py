"""
strategy.py

High-level strategic decision making.

The strategy module determines the long-term direction of the AI.
It does not issue farmer actions directly.

Planner asks Strategy what overall objective to pursue.
"""

from __future__ import annotations

from enum import Enum


class StrategyMode(str, Enum):

    EARLY_GAME = "EARLY_GAME"

    MID_GAME = "MID_GAME"

    LATE_GAME = "LATE_GAME"

    END_GAME = "END_GAME"


class Strategy:

    def __init__(self, parser):

        self.parser = parser

    # ---------------------------------------------------------
    # Determine Season Phase
    # ---------------------------------------------------------

    @property
    def mode(self):

        day = self.parser.day

        if day < 6:
            return StrategyMode.EARLY_GAME

        if day < 15:
            return StrategyMode.MID_GAME

        if day < 25:
            return StrategyMode.LATE_GAME

        return StrategyMode.END_GAME

    # ---------------------------------------------------------
    # Recommended Crop
    # ---------------------------------------------------------

    def preferred_crop(self):

        mode = self.mode

        if mode == StrategyMode.EARLY_GAME:
            return "WHEAT"

        if mode == StrategyMode.MID_GAME:
            return "CARROT"

        if mode == StrategyMode.LATE_GAME:
            return "TOMATO"

        return "STRAWBERRY"

    # ---------------------------------------------------------
    # Buy Land?
    # ---------------------------------------------------------

    def should_expand(self):

        return self.parser.money >= 1200

    # ---------------------------------------------------------
    # Hire Workers?
    # ---------------------------------------------------------

    def should_hire(self):

        return self.parser.money >= 2000

    # ---------------------------------------------------------
    # Sell Immediately?
    # ---------------------------------------------------------

    def sell_now(self):

        return self.mode == StrategyMode.END_GAME