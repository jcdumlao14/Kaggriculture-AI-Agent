"""
multi_turn_planner.py

Multi-turn planning for the Kaggriculture AI Agent.

Builds a short action plan instead of selecting
only the next action.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class MultiTurnPlanner:
    """
    Build a short sequence of future tasks.
    """

    def __init__(self, planner):
        self.planner = planner

    # ---------------------------------------------------------

    def plan(self, horizon: int = 3):
        """
        Return up to 'horizon' planned tasks.
        """

        tasks = self.planner.plan()

        return tasks[:horizon]

    # ---------------------------------------------------------

    def next_task(self):
        """
        Return only the first planned task.
        """

        tasks = self.plan(1)

        if tasks:
            return tasks[0]

        return None