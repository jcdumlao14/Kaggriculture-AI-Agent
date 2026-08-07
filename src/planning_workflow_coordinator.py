"""
planning_workflow_coordinator.py

Planning Workflow Coordinator for the Kaggriculture AI Agent.

Coordinates feature preparation, plan evaluation,
execution, and comparison into a unified planning
workflow.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.plan_comparator import PlanComparator
from src.plan_evaluator import PlanEvaluator
from src.plan_executor import PlanExecutor
from src.planning_service_coordinator import (
    PlanningServiceCoordinator,
)


from src.base_workflow_coordinator import (
    BaseWorkflowCoordinator,
)

class PlanningWorkflowCoordinator(
    BaseWorkflowCoordinator,
):
    
    """
    Coordinate the planning workflow.
    """

    def __init__(self):

        self.service = PlanningServiceCoordinator()
        self.evaluator = PlanEvaluator()
        self.comparator = PlanComparator()
        self.executor = PlanExecutor()

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

        return self.service.prepare_features(
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

        self.service.clear_cache()