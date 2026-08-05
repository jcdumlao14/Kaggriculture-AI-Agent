"""
worker_planner.py

Worker Planner for the Kaggriculture AI Agent.

Assigns tasks to available workers.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class WorkerPlanner:
    """
    Plans work assignments.
    """

    def available_workers(
        self,
        game_state: dict,
    ) -> list:

        workers = []

        farmer = game_state.get(
            "farmer",
        )

        if farmer is not None:
            workers.append(farmer)

        workers.extend(
            game_state.get(
                "hands",
                [],
            )
        )

        return workers

    # ---------------------------------------------------------

    def worker_count(
        self,
        game_state: dict,
    ) -> int:

        return len(
            self.available_workers(
                game_state,
            )
        )

    # ---------------------------------------------------------

    def has_workers(
        self,
        game_state: dict,
    ) -> bool:

        return (
            self.worker_count(
                game_state,
            )
            > 0
        )

    # ---------------------------------------------------------

    def assign(
        self,
        worker,
        action: dict,
    ) -> dict:
        """
        Create a worker assignment.
        """

        return {
            "worker": worker,
            "action": action,
        }