"""
turn_execution_planner.py

Turn Execution Planner for the Kaggriculture AI Agent.

Creates an ordered execution plan for the
current turn based on worker assignments.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class TurnExecutionPlanner:
    """
    Build the execution order for one turn.
    """

    # ---------------------------------------------------------

    def build_plan(
        self,
        *,
        assignments: dict[str, dict],
    ) -> list[dict]:
        """
        Convert worker assignments into an
        ordered execution plan.
        """

        plan = []

        for worker, task in assignments.items():

            plan.append(
                {
                    "worker": worker,
                    "task": task.get("name"),
                    "priority": task.get(
                        "priority",
                        0.0,
                    ),
                }
            )

        return sorted(
            plan,
            key=lambda step: step["priority"],
            reverse=True,
        )

    # ---------------------------------------------------------

    def next_step(
        self,
        plan: list[dict],
    ) -> dict | None:
        """
        Return the next step in the plan.
        """

        if not plan:
            return None

        return plan[0]

    # ---------------------------------------------------------

    def total_steps(
        self,
        plan: list[dict],
    ) -> int:
        """
        Return the number of planned steps.
        """

        return len(plan)