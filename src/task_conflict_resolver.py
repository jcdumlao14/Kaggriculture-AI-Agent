"""
task_conflict_resolver.py

Task Conflict Resolver for the Kaggriculture AI Agent.

Resolves competing task assignments by keeping
the highest-priority task.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class TaskConflictResolver:
    """
    Resolve conflicts between task assignments.
    """

    # ---------------------------------------------------------

    def resolve(
        self,
        *,
        assignments: dict[str, list[dict]],
    ) -> dict[str, dict]:
        """
        Keep the highest-priority task for each worker.
        """

        resolved: dict[str, dict] = {}

        for worker, tasks in assignments.items():

            if not tasks:
                continue

            best = max(
                tasks,
                key=lambda task: task.get(
                    "priority",
                    0.0,
                ),
            )

            resolved[worker] = best

        return resolved

    # ---------------------------------------------------------

    def conflicts(
        self,
        *,
        assignments: dict[str, list[dict]],
    ) -> dict[str, list[dict]]:
        """
        Return workers with multiple competing tasks.
        """

        return {
            worker: tasks
            for worker, tasks in assignments.items()
            if len(tasks) > 1
        }

    # ---------------------------------------------------------

    def has_conflicts(
        self,
        *,
        assignments: dict[str, list[dict]],
    ) -> bool:
        """
        Return True when any worker has
        multiple assigned tasks.
        """

        return any(
            len(tasks) > 1
            for tasks in assignments.values()
        )