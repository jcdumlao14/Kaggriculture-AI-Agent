"""
planning_facade.py

Planning Facade for the Kaggriculture AI Agent.

Provides a simple interface for the complete
planning workflow.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.planning_workflow_coordinator import (
    PlanningWorkflowCoordinator,
)


class PlanningFacade:
    """
    High-level interface for planning.
    """

    def __init__(self):

        self.workflow = PlanningWorkflowCoordinator()

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

        return self.workflow.prepare_features(
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

        self.workflow.clear_cache()