"""
resource_aware_plan_validator.py

Resource-Aware Plan Validator for the
Kaggriculture AI Agent.

Validates selected plans before execution.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAwarePlanValidator:
    """
    Validate resource-aware plans.
    """

    # ---------------------------------------------------------

    def is_valid_task(
        self,
        *,
        task: dict,
    ) -> bool:
        """
        Return True when a task has a valid structure.
        """

        if not isinstance(task, dict):
            return False

        if not task:
            return False

        requirements = task.get(
            "requirements",
            {},
        )

        if not isinstance(requirements, dict):
            return False

        for amount in requirements.values():

            if not isinstance(
                amount,
                (int, float),
            ):
                return False

            if amount < 0:
                return False

        return True

    # ---------------------------------------------------------

    def validate(
        self,
        *,
        plan: list[dict],
    ) -> bool:
        """
        Return True when every task in the plan
        is structurally valid.
        """

        if not isinstance(plan, list):
            return False

        return all(
            self.is_valid_task(task=task)
            for task in plan
        )

    # ---------------------------------------------------------

    def invalid_tasks(
        self,
        *,
        plan: list[dict],
    ) -> list[dict]:
        """
        Return all structurally invalid tasks.
        """

        if not isinstance(plan, list):
            return []

        return [
            task
            for task in plan
            if not self.is_valid_task(
                task=task,
            )
        ]

    # ---------------------------------------------------------

    def task_count(
        self,
        *,
        plan: list[dict],
    ) -> int:
        """
        Return the number of tasks in a plan.
        """

        if not isinstance(plan, list):
            return 0

        return len(plan)

    # ---------------------------------------------------------

    def has_tasks(
        self,
        *,
        plan: list[dict],
    ) -> bool:
        """
        Return True when the plan contains tasks.
        """

        return self.task_count(
            plan=plan,
        ) > 0