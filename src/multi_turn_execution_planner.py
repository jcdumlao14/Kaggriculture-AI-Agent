"""
multi_turn_execution_planner.py

Multi-Turn Execution Planner for the Kaggriculture AI Agent.

Builds execution plans spanning multiple turns.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class MultiTurnExecutionPlanner:
    """
    Build execution plans across multiple turns.
    """

    # ---------------------------------------------------------

    def build(
        self,
        *,
        turns: list[list[dict]],
    ) -> list[dict]:
        """
        Flatten turn plans into one execution plan.
        """

        plan = []

        for turn_index, tasks in enumerate(turns):

            for task in tasks:

                plan.append(
                    {
                        "turn": turn_index,
                        **task,
                    }
                )

        return plan

    # ---------------------------------------------------------

    def turn_plan(
        self,
        *,
        turns: list[list[dict]],
        turn: int,
    ) -> list[dict]:
        """
        Return one turn's plan.
        """

        if 0 <= turn < len(turns):
            return turns[turn]

        return []

    # ---------------------------------------------------------

    def total_actions(
        self,
        *,
        turns: list[list[dict]],
    ) -> int:
        """
        Count all planned actions.
        """

        return sum(
            len(tasks)
            for tasks in turns
        )