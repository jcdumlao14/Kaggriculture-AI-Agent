"""
resource_allocation_advisor.py

Resource Allocation Advisor for the Kaggriculture AI Agent.

Recommends how available resources should be
distributed among major farm activities.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAllocationAdvisor:
    """
    Recommend resource allocation.
    """

    # ---------------------------------------------------------

    def allocate(
        self,
        *,
        money: float,
        crop_need: float,
        animal_need: float,
        expansion_need: float,
    ) -> dict:
        """
        Allocate available money proportionally
        to requested needs.
        """

        total_need = (
            crop_need
            + animal_need
            + expansion_need
        )

        if total_need <= 0:
            return {
                "crops": 0.0,
                "animals": 0.0,
                "expansion": 0.0,
            }

        return {
            "crops": money * crop_need / total_need,
            "animals": money * animal_need / total_need,
            "expansion": money * expansion_need / total_need,
        }

    # ---------------------------------------------------------

    def highest_priority(
        self,
        allocation: dict,
    ) -> str:
        """
        Return the category receiving the
        largest allocation.
        """

        return max(
            allocation,
            key=allocation.get,
        )

    # ---------------------------------------------------------

    def remaining(
        self,
        *,
        money: float,
        allocation: dict,
    ) -> float:
        """
        Return any unallocated money.
        """

        return max(
            0.0,
            money - sum(allocation.values()),
        )