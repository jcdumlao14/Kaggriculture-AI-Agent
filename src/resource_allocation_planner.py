"""
resource_allocation_planner.py

Resource Allocation Planner for the Kaggriculture AI Agent.

Determines whether an action fits within
the available budget.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAllocationPlanner:
    """
    Plans spending decisions.
    """

    # ---------------------------------------------------------

    def can_afford(
        self,
        *,
        money: int,
        cost: int,
    ) -> bool:
        """
        Return True if enough money exists.
        """

        return money >= cost

    # ---------------------------------------------------------

    def remaining_budget(
        self,
        *,
        money: int,
        cost: int,
    ) -> int:
        """
        Return remaining budget.
        """

        return max(
            0,
            money - cost,
        )

    # ---------------------------------------------------------

    def spend(
        self,
        *,
        money: int,
        cost: int,
    ) -> int:
        """
        Spend money if affordable.
        """

        if not self.can_afford(
            money=money,
            cost=cost,
        ):
            return money

        return money - cost