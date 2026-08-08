"""
resource_consumption_planner.py

Resource Consumption Planner for the Kaggriculture AI Agent.

Estimates resource changes caused by planned tasks.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceConsumptionPlanner:
    """
    Calculate resource changes caused by tasks.
    """

    # ---------------------------------------------------------

    def consumption(
        self,
        *,
        task: dict,
    ) -> dict:
        """
        Return resources consumed by a task.
        """

        requirements = task.get(
            "requirements",
            {},
        )

        return {
            resource: amount
            for resource, amount
            in requirements.items()
            if amount > 0
        }

    # ---------------------------------------------------------

    def remaining(
        self,
        *,
        resources: dict,
        task: dict,
    ) -> dict:
        """
        Return resources remaining after a task.
        """

        result = dict(resources)

        for resource, amount in self.consumption(
            task=task,
        ).items():

            result[resource] = (
                result.get(resource, 0)
                - amount
            )

        return result

    # ---------------------------------------------------------

    def affordable(
        self,
        *,
        resources: dict,
        task: dict,
    ) -> bool:
        """
        Return True if the task can be afforded.
        """

        for resource, amount in self.consumption(
            task=task,
        ).items():

            if resources.get(
                resource,
                0,
            ) < amount:
                return False

        return True

    # ---------------------------------------------------------

    def apply(
        self,
        *,
        resources: dict,
        tasks: list[dict],
    ) -> dict:
        """
        Apply a sequence of resource-consuming tasks.
        """

        result = dict(resources)

        for task in tasks:

            if not self.affordable(
                resources=result,
                task=task,
            ):
                break

            result = self.remaining(
                resources=result,
                task=task,
            )

        return result