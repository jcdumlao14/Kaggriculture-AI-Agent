"""
planning_feature_service.py

Planning Feature Service for the Kaggriculture AI Agent.

Provides processed feature dictionaries for
planning components using the feature pipeline.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.feature_pipeline_coordinator import (
    FeaturePipelineCoordinator,
)


class PlanningFeatureService:
    """
    Prepare planning features.
    """

    def __init__(self):

        self.pipeline = FeaturePipelineCoordinator()

    # ---------------------------------------------------------

    def features(
        self,
        *,
        state_id: str,
        game_state: dict,
        maximums: dict[str, float] | None = None,
        selected: list[str] | None = None,
    ) -> dict:
        """
        Return processed planning features.
        """

        return self.pipeline.process(
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

        self.pipeline.clear_cache()