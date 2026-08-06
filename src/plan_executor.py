"""
plan_executor.py

Plan Executor for the Kaggriculture AI Agent.

Executes action plans one action at a time.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class PlanExecutor:
    """
    Executes planned actions.
    """

    def __init__(self):
        self._plan = []

    # ---------------------------------------------------------

    def load_plan(
        self,
        plan: list[dict],
    ) -> None:
        """
        Load a new action plan.
        """

        self._plan = list(plan)

    # ---------------------------------------------------------

    def next_action(
        self,
    ) -> dict | None:
        """
        Return and remove the next action.
        """

        if not self._plan:
            return None

        return self._plan.pop(0)

    # ---------------------------------------------------------

    def remaining_actions(
        self,
    ) -> int:
        """
        Return remaining action count.
        """

        return len(self._plan)

    # ---------------------------------------------------------

    def has_actions(
        self,
    ) -> bool:
        """
        Return True if actions remain.
        """

        return bool(self._plan)

    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clear the current plan.
        """

        self._plan.clear()