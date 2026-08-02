"""
decision_engine.py

Central decision engine for the Kaggriculture AI Agent.

Author: Jocelyn C. Dumlao
"""

from src.world import World
from src.market import Market
from src.planner import Planner
from src.scheduler import Scheduler


class DecisionEngine:
    """
    Combines all AI modules into one decision pipeline.
    """

    def __init__(self, parser):
        self.parser = parser

        self.world = World(parser)
        self.market = Market(parser)

        self.planner = Planner(
            parser,
            self.world,
            self.market,
        )

        self.scheduler = Scheduler()

    def next_task(self):
        """
        Return the highest-priority task.
        """

        tasks = self.planner.plan()

        for task in tasks:
            self.scheduler.add(
                priority=task["priority"],
                action=task["task"],
                target=task.get("target"),
                crop=task.get("crop"),
                product=task.get("product"),
                amount=task.get("amount"),
            )

        return self.scheduler.next_task()