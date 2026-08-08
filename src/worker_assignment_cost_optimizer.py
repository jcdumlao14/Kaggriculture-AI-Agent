"""
worker_assignment_cost_optimizer.py

Worker Assignment Cost Optimizer for the Kaggriculture AI Agent.

Selects worker-task assignments using task priority
and movement cost.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.worker_travel_cost_analyzer import (
    WorkerTravelCostAnalyzer,
)


class WorkerAssignmentCostOptimizer:
    """
    Optimize worker assignments using priority
    and travel cost.
    """

    def __init__(
        self,
        travel_weight: float = 1.0,
    ):
        if travel_weight < 0:
            raise ValueError(
                "travel_weight must be non-negative"
            )

        self.travel_weight = travel_weight
        self.travel_analyzer = (
            WorkerTravelCostAnalyzer()
        )

    # ---------------------------------------------------------

    def assignment_score(
        self,
        *,
        task_priority: float,
        worker_position: tuple[int, int],
        task_position: tuple[int, int],
    ) -> float:
        """
        Calculate assignment score.

        Higher priority increases the score.
        Greater travel distance decreases the score.
        """

        travel_cost = (
            self.travel_analyzer.travel_cost(
                start=worker_position,
                target=task_position,
            )
        )

        return (
            float(task_priority)
            - (
                travel_cost
                * self.travel_weight
            )
        )

    # ---------------------------------------------------------

    def best_worker(
        self,
        *,
        workers: dict[str, tuple[int, int]],
        task_priority: float,
        task_position: tuple[int, int],
    ) -> str | None:
        """
        Return the worker with the best
        priority-adjusted travel score.
        """

        if not workers:
            return None

        best_worker = None
        best_score = float("-inf")

        for worker, position in workers.items():

            score = self.assignment_score(
                task_priority=task_priority,
                worker_position=position,
                task_position=task_position,
            )

            if score > best_score:
                best_score = score
                best_worker = worker

        return best_worker

    # ---------------------------------------------------------

    def rank_workers(
        self,
        *,
        workers: dict[str, tuple[int, int]],
        task_priority: float,
        task_position: tuple[int, int],
    ) -> list[dict]:
        """
        Rank workers for a task.
        """

        ranked = []

        for worker, position in workers.items():

            score = self.assignment_score(
                task_priority=task_priority,
                worker_position=position,
                task_position=task_position,
            )

            ranked.append(
                {
                    "worker": worker,
                    "score": score,
                }
            )

        return sorted(
            ranked,
            key=lambda item: item["score"],
            reverse=True,
        )