"""
planning_service_coordinator.py

Planning Service Coordinator for the Kaggriculture AI Agent.

Coordinates feature preparation and planning
evaluation into a unified planning workflow.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.planning_feature_service import (
    PlanningFeatureService,
)
from src.plan_evaluator import (
    PlanEvaluator,
)


class PlanningServiceCoordinator:
    """
    Coordinate planning services.
    """

    def __init__(self):

        self.feature_service = PlanningFeatureService()
        self.evaluator = PlanEvaluator()

    # ---------------------------------------------------------

    def prepare_features(
        self,
        *,
        state_id: str,
        game_state: dict,
        maximums: dict[str, float] | None = None,
        selected: list[str] | None = None,
    ) -> dict:
        """
        Prepare planning features.
        """

        return self.feature_service.features(
            state_id=state_id,
            game_state=game_state,
            maximums=maximums,
            selected=selected,
        )

    # ---------------------------------------------------------

    def clear_cache(
        self,
    ) -> None:
        """
        Clear cached planning features.
        """

        self.feature_service.clear_cache()