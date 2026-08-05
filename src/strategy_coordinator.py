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
from src.crop_planner import CropPlanner
from src.animal_planner import AnimalPlanner
from src.expansion_planner import ExpansionPlanner
from src.worker_planner import WorkerPlanner


class StrategyCoordinator:
    """
    Coordinate high-level strategy.
    """

    def __init__(self):

        self.search = SearchController()
        self.turn_phase = TurnPhaseManager()
        self.crop_planner = None
        self.animal_planner = AnimalPlanner()
        self.expansion_planner = ExpansionPlanner()
        self.worker_planner = WorkerPlanner()

        # ---------------------------------------------------------

    def worker_count(
        self,
        game_state: dict,
    ) -> int:

        return self.worker_planner.worker_count(
            game_state,
        )

    # ---------------------------------------------------------

    def best_animal_action(
        self,
        animal: dict,
    ) -> str:

        return self.animal_planner.best_action(
            animal,
        )

    # ---------------------------------------------------------

    def should_expand(
        self,
        *,
        money: float,
        available_land: int,
    ) -> bool:

        return self.expansion_planner.should_expand(
            money=money,
            available_land=available_land,
        )

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