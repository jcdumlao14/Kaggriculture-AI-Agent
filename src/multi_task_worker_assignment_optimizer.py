"""
multi_task_worker_assignment_optimizer.py

Multi-Task Worker Assignment Optimizer for the
Kaggriculture AI Agent.

Assigns multiple tasks to available workers while
considering task priority and movement cost.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.worker_assignment_cost_optimizer import (
    WorkerAssignmentCostOptimizer,
)


class MultiTaskWorkerAssignmentOptimizer:
    """
    Optimize assignments across multiple workers
    and tasks.
    """

    def __init__(
        self,
        travel_weight: float = 1.0,
    ):
        self.optimizer = (
            WorkerAssignmentCostOptimizer(
                travel_weight=travel_weight,
            )
        )

    # ---------------------------------------------------------

    def assign(
        self,
        *,
        workers: dict[str, tuple[int, int]],
        tasks: list[dict],
    ) -> dict[str, dict]:
        """
        Assign tasks to workers.

        Each worker receives at most one task.
        Tasks are considered by descending priority.
        """

        assignments: dict[str, dict] = {}

        if not workers or not tasks:
            return assignments

        remaining_workers = dict(workers)

        ranked_tasks = sorted(
            tasks,
            key=lambda task: task.get(
                "priority",
                0.0,
            ),
            reverse=True,
        )

        for task in ranked_tasks:

            if not remaining_workers:
                break

            worker = self.optimizer.best_worker(
                workers=remaining_workers,
                task_priority=task.get(
                    "priority",
                    0.0,
                ),
                task_position=task.get(
                    "position",
                    (0, 0),
                ),
            )

            if worker is None:
                continue

            assignments[worker] = task

            del remaining_workers[worker]

        return assignments

    # ---------------------------------------------------------

    def unassigned_tasks(
        self,
        *,
        workers: dict[str, tuple[int, int]],
        tasks: list[dict],
    ) -> list[dict]:
        """
        Return tasks that could not be assigned.
        """

        assignments = self.assign(
            workers=workers,
            tasks=tasks,
        )

        assigned_tasks = list(
            assignments.values()
        )

        return [
            task
            for task in tasks
            if task not in assigned_tasks
        ]

    # ---------------------------------------------------------

    def idle_workers(
        self,
        *,
        workers: dict[str, tuple[int, int]],
        tasks: list[dict],
    ) -> list[str]:
        """
        Return workers that received no task.
        """

        assignments = self.assign(
            workers=workers,
            tasks=tasks,
        )

        return [
            worker
            for worker in workers
            if worker not in assignments
        ]