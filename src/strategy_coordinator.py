"""
strategy_coordinator.py

Strategy Coordinator for the Kaggriculture AI Agent.

Coordinates season, turn phase, and search
strategy selection.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.search_controller import SearchController
from src.turn_phase_manager import TurnPhaseManager


class StrategyCoordinator:
    """
    Coordinate high-level strategy.
    """

    def __init__(self):

        self.search = SearchController()
        self.turn_phase = TurnPhaseManager()

    # ---------------------------------------------------------

    def strategy(
        self,
        observation: dict,
    ) -> dict:
        """
        Return the current strategy profile.
        """

        day = observation.get("day", 0)
        hour = observation.get("hour", 0)

        return {
            "day": day,
            "hour": hour,
            "phase": self.turn_phase.phase(hour),
            "algorithm": self.search.select_algorithm(
                turn=day,
            ),
        }

    # ---------------------------------------------------------

    def search_algorithm(
        self,
        observation: dict,
    ) -> str:

        return self.strategy(
            observation,
        )["algorithm"]

    # ---------------------------------------------------------

    def turn_phase_name(
        self,
        observation: dict,
    ) -> str:

        return self.strategy(
            observation,
        )["phase"]

    # ---------------------------------------------------------

    def is_late_game(
        self,
        observation: dict,
    ) -> bool:

        return observation.get(
            "day",
            0,
        ) >= 25

    # ---------------------------------------------------------

    def is_end_of_day(
        self,
        observation: dict,
    ) -> bool:

        return observation.get(
            "hour",
            0,
        ) >= 20