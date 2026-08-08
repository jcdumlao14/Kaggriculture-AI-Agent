"""
worker_travel_cost_analyzer.py

Worker Travel Cost Analyzer for the Kaggriculture AI Agent.

Estimates worker movement cost between positions
using Manhattan distance.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class WorkerTravelCostAnalyzer:
    """
    Analyze worker movement cost.
    """

    # ---------------------------------------------------------

    def distance(
        self,
        *,
        start: tuple[int, int],
        target: tuple[int, int],
    ) -> int:
        """
        Return Manhattan distance between two positions.
        """

        return (
            abs(start[0] - target[0])
            + abs(start[1] - target[1])
        )

    # ---------------------------------------------------------

    def travel_cost(
        self,
        *,
        start: tuple[int, int],
        target: tuple[int, int],
        cost_per_step: float = 1.0,
    ) -> float:
        """
        Return movement cost between two positions.
        """

        if cost_per_step < 0:
            raise ValueError(
                "cost_per_step must be non-negative"
            )

        return (
            self.distance(
                start=start,
                target=target,
            )
            * cost_per_step
        )

    # ---------------------------------------------------------

    def closer(
        self,
        *,
        start: tuple[int, int],
        first_target: tuple[int, int],
        second_target: tuple[int, int],
    ) -> tuple[int, int]:
        """
        Return whichever target is closer.

        If both targets are equally distant,
        return first_target.
        """

        first_distance = self.distance(
            start=start,
            target=first_target,
        )

        second_distance = self.distance(
            start=start,
            target=second_target,
        )

        if first_distance <= second_distance:
            return first_target

        return second_target