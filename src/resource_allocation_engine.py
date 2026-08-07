"""
resource_allocation_engine.py

Resource Allocation Engine for the Kaggriculture AI Agent.

Manages available resources and determines whether
planned actions are affordable.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAllocationEngine:
    """
    Allocate economic resources.
    """

    def __init__(self):

        self.resources = {}

    # ---------------------------------------------------------

    def set_resource(
        self,
        name: str,
        amount: float,
    ) -> None:
        """
        Store a resource quantity.
        """

        self.resources[name.upper()] = float(amount)

    # ---------------------------------------------------------

    def available(
        self,
        name: str,
    ) -> float:
        """
        Return available quantity.
        """

        return self.resources.get(
            name.upper(),
            0.0,
        )

    # ---------------------------------------------------------

    def can_afford(
        self,
        name: str,
        cost: float,
    ) -> bool:
        """
        Return True if enough resource exists.
        """

        return self.available(name) >= cost

    # ---------------------------------------------------------

    def spend(
        self,
        name: str,
        amount: float,
    ) -> bool:
        """
        Spend a resource if available.
        """

        if not self.can_afford(
            name,
            amount,
        ):
            return False

        self.resources[name.upper()] -= amount
        return True

    # ---------------------------------------------------------

    def add(
        self,
        name: str,
        amount: float,
    ) -> None:
        """
        Increase a resource.
        """

        self.resources[name.upper()] = (
            self.available(name)
            + amount
        )