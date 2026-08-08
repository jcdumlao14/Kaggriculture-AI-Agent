"""
resource_aware_task_scheduler.py

Resource-Aware Task Scheduler for the
Kaggriculture AI Agent.

Filters and prioritizes tasks according to
the resources currently available.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAwareTaskScheduler:
    """
    Schedule tasks while respecting resource
    requirements.
    """

    DEFAULT_REQUIREMENTS = {
        "WATER": {"water": 1},
        "FEED": {"wheat": 1},
        "FERTILIZE": {"fertilizer": 1},
        "BUY_LAND": {"money": 5000},
        "BUY_ANIMAL": {"money": 1000},
    }

    # ---------------------------------------------------------

    def can_execute(
        self,
        *,
        task: dict,
        resources: dict,
    ) -> bool:
        """
        Return True when enough resources exist
        for the task.
        """

        requirements = task.get(
            "requirements",
            self.DEFAULT_REQUIREMENTS.get(
                task.get("name", ""),
                {},
            ),
        )

        for resource, required in requirements.items():

            if resources.get(
                resource,
                0,
            ) < required:
                return False

        return True

    # ---------------------------------------------------------

    def filter_tasks(
        self,
        *,
        tasks: list[dict],
        resources: dict,
    ) -> list[dict]:
        """
        Return only executable tasks.
        """

        return [
            task
            for task in tasks
            if self.can_execute(
                task=task,
                resources=resources,
            )
        ]

    # ---------------------------------------------------------

    def schedule(
        self,
        *,
        tasks: list[dict],
        resources: dict,
    ) -> list[dict]:
        """
        Filter and prioritize executable tasks.
        """

        executable = self.filter_tasks(
            tasks=tasks,
            resources=resources,
        )

        return sorted(
            executable,
            key=lambda task: task.get(
                "priority",
                0.0,
            ),
            reverse=True,
        )

    # ---------------------------------------------------------

    def next_task(
        self,
        *,
        tasks: list[dict],
        resources: dict,
    ) -> dict | None:
        """
        Return the highest-priority executable task.
        """

        scheduled = self.schedule(
            tasks=tasks,
            resources=resources,
        )

        if not scheduled:
            return None

        return scheduled[0]