"""
agent.py

Main AI Agent for Kaggriculture.

Coordinates every AI subsystem and returns
valid Kaggle actions.

Author: Jocelyn Dumlao
Project: Kaggriculture-AI-Agent
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
from src.actions import ActionBuilder


class KaggricultureAgent:
    """
    Main Kaggriculture AI Agent.

    Pipeline

        Observation
              ↓
           Parser
              ↓
            World
              ↓
            State
              ↓
          Economy
              ↓
           Market
              ↓
          Strategy
              ↓
           Planner
              ↓
          Scheduler
              ↓
        Action Builder
              ↓
        Kaggle Environment
    """

    def __init__(self):
        """Initialize every AI subsystem."""

        # Persistent memory
        self.state = StateManager()

        # Dynamic modules
        self.parser = None
        self.world = None
        self.market = None
        self.strategy = None
        self.planner = None

        # Long-lived modules
        self.scheduler = Scheduler()
        self.economy = Economy()
        self.actions = ActionBuilder()

    # ---------------------------------------------------------
    # Update Environment
    # ---------------------------------------------------------

    def update(self, observation):
        """
        Parse the latest observation and
        update every subsystem.
        """

        self.parser = ObservationParser(observation)

        # Update persistent memory
        self.state.update(self.parser)

        # Build world model
        self.world = World(self.parser)

        # Market analysis
        self.market = Market(self.parser)

        # Economy tracking
        if hasattr(self.parser, "money"):
            self.economy.update(self.parser.money)

        # High-level strategy
        self.strategy = Strategy(self.parser)

        # Planner
        self.planner = Planner(
            parser=self.parser,
            world=self.world,
            market=self.market,
        )

    # ---------------------------------------------------------
    # Decision Engine
    # ---------------------------------------------------------

    def think(self):
        """
        Generate candidate tasks and allow
        the scheduler to choose the best one.
        """

        self.scheduler.clear()

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

        decision = self.scheduler.next()

        if decision is None:

            return {
                "task": "PASS",
                "target": None,
                "crop": None,
                "product": None,
                "amount": None,
            }

        return {
            "task": decision.action,
            "target": decision.target,
            "crop": decision.crop,
            "product": decision.product,
            "amount": decision.amount,
        }

    # ---------------------------------------------------------
    # Main API
    # ---------------------------------------------------------

    def act(self, observation):
        """
        Main entry point called by Kaggle.

        Parameters
        ----------
        observation : dict

        Returns
        -------
        dict
            Kaggle-compatible action dictionary.
        """

        # Update game state
        self.update(observation)

        # AI chooses next task
        task = self.think()

        # Convert planner task into
        # Kaggle action dictionary
        return self.actions.build(task)