"""
path_planner.py

Path Planner for the Kaggriculture AI Agent.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class PathPlanner:
    """
    Computes simple Manhattan paths.
    """

    def distance(
        self,
        start,
        goal,
    ) -> int:
        """
        Return Manhattan distance.
        """
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    def next_step(
        self,
        start,
        goal,
    ):
        """
        Return the next movement direction.
        """

        sx, sy = start
        gx, gy = goal

        if sx < gx:
            return "EAST"

        if sx > gx:
            return "WEST"

        if sy < gy:
            return "SOUTH"

        if sy > gy:
            return "NORTH"

        return "PASS"