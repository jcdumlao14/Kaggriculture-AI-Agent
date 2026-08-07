"""
worker_assignment_optimizer.py

Worker Assignment Optimizer for the Kaggriculture AI Agent.

Assigns prioritized tasks to available workers.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class WorkerAssignmentOptimizer:
    """
    Assign tasks to workers.
    """

    # ---------------------------------------------------------

    def assign(
        self,
        *,
        workers: list[str],
        tasks: list[dict],
    ) -> dict[str, dict]:
        """
        Assign the highest-priority tasks to workers.
        """

        assignments: dict[str, dict] = {}

        ranked_tasks = sorted(
            tasks,
            key=lambda task: task.get(
                "priority",
                0.0,
            ),
            reverse=True,
        )

        for worker, task in zip(
            workers,
            ranked_tasks,
        ):
            assignments[worker] = task

        return assignments

    # ---------------------------------------------------------

    def unassigned_tasks(
        self,
        *,
        workers: list[str],
        tasks: list[dict],
    ) -> list[dict]:
        """
        Return tasks that could not be assigned.
        """

        ranked_tasks = sorted(
            tasks,
            key=lambda task: task.get(
                "priority",
                0.0,
            ),
            reverse=True,
        )

        return ranked_tasks[len(workers):]

    # ---------------------------------------------------------

    def idle_workers(
        self,
        *,
        workers: list[str],
        tasks: list[dict],
    ) -> list[str]:
        """
        Return workers that received no task.
        """

        if len(tasks) >= len(workers):
            return []

        return workers[len(tasks):]