"""
agent.py

Main AI Agent for Kaggriculture.

This module coordinates every subsystem and returns
valid Kaggle actions.
"""

from __future__ import annotations

from src.parser import ObservationParser
from src.world import World
from src.strategy import Strategy
from src.planner import Planner
from src.scheduler import Scheduler
from src.market import Market
from src.economy import Economy
from src.state import StateManager


class KaggricultureAgent:
    """
    Main competition agent.

    Coordinates every module.
    """

    def __init__(self):

        self.state = StateManager()

        self.parser = None
        self.world = None

        self.market = None
        self.economy = Economy()

        self.strategy = None

        self.planner = None

        self.scheduler = Scheduler()

    # ------------------------------------------------------

    def update(self, observation):

        """
        Parse latest observation.
        """

        self.parser = ObservationParser(observation)

        self.state.update(self.parser)

        self.world = World(self.parser)

        self.market = Market(self.parser)

        self.strategy = Strategy(self.parser)

        self.planner = Planner(
            self.parser,
            self.world,
        )

    # ------------------------------------------------------

    def think(self):
        """
        Main decision loop.

        For now this only asks the planner for the
        highest priority task.
        """

        task = self.planner.plan()

        return task

    # ------------------------------------------------------

    def act(self, observation):

        self.update(observation)

        task = self.think()

        return task