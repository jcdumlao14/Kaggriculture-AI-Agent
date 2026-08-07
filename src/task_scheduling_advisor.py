"""
task_scheduling_advisor.py

Task Scheduling Advisor for the Kaggriculture AI Agent.

Prioritizes farm tasks when only a limited
number of actions can be performed.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class TaskSchedulingAdvisor:
    """
    Prioritize farm tasks.
    """

    # ---------------------------------------------------------

    def schedule(
        self,
        tasks: list[dict],
    ) -> list[dict]:
        """
        Return tasks sorted by priority.
        """

        return sorted(
            tasks,
            key=lambda task: (
                task.get("priority", 0.0),
                task.get("urgency", 0.0),
            ),
            reverse=True,
        )

    # ---------------------------------------------------------

    def next_task(
        self,
        tasks: list[dict],
    ) -> dict | None:
        """
        Return the highest-priority task.
        """

        ranked = self.schedule(tasks)

        if not ranked:
            return None

        return ranked[0]

    # ---------------------------------------------------------

    def top_tasks(
        self,
        tasks: list[dict],
        *,
        limit: int,
    ) -> list[dict]:
        """
        Return the top N scheduled tasks.
        """

        return self.schedule(tasks)[:limit]