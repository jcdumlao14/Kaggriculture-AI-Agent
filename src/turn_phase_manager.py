"""
turn_phase_manager.py

Turn Phase Manager for the Kaggriculture AI Agent.

Determines the current phase of the day
based on the in-game hour.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class TurnPhaseManager:
    """
    Manage turn phases within a day.
    """

    TURNS_PER_DAY = 24

    # ---------------------------------------------------------

    def phase(
        self,
        hour: int,
    ) -> str:
        """
        Return the phase of the current day.
        """

        if hour < 8:
            return "EARLY"

        if hour < 16:
            return "MID"

        return "LATE"

    # ---------------------------------------------------------

    def remaining_turns(
        self,
        hour: int,
    ) -> int:
        """
        Return the remaining turns in the day.
        """

        return max(
            0,
            self.TURNS_PER_DAY - hour,
        )

    # ---------------------------------------------------------

    def is_final_turn(
        self,
        hour: int,
    ) -> bool:
        """
        Return True if this is the final turn.
        """

        return hour >= (
            self.TURNS_PER_DAY - 1
        )

    # ---------------------------------------------------------

    def should_finish_tasks(
        self,
        hour: int,
    ) -> bool:
        """
        Return True during the late phase.
        """

        return self.phase(hour) == "LATE"

    # ---------------------------------------------------------

    def progress(
        self,
        hour: int,
    ) -> float:
        """
        Return daily progress between 0 and 1.
        """

        return min(
            max(hour / self.TURNS_PER_DAY, 0.0),
            1.0,
        )