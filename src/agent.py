"""
agent.py

Main AI Agent for Kaggriculture.

Coordinates every AI subsystem and returns
valid Kaggle actions.

Author: Jocelyn C. Dumlao
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
from src.pathfinder import Pathfinder
from src.market_memory import MarketMemory


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
         Pathfinder
              ↓
        Action Builder
              ↓
        Kaggle Environment
    """

    def __init__(self):
        """Initialize every AI subsystem."""

        # -------------------------------------------------
        # Persistent memory
        # -------------------------------------------------

        self.state = StateManager()

        # -------------------------------------------------
        # Dynamic modules (rebuilt every turn)
        # -------------------------------------------------

        self.parser = None
        self.world = None
        self.market = None
        self.strategy = None
        self.planner = None
        self.pathfinder = None

        # -------------------------------------------------
        # Long-lived modules
        # -------------------------------------------------

        self.scheduler = Scheduler()
        self.economy = Economy()
        self.actions = ActionBuilder()

    # =====================================================
    # Update Environment
    # =====================================================

    def update(self, observation):
        """
        Parse the latest observation and update
        every subsystem.
        """

        # Parse observation
        self.parser = ObservationParser(observation)

        # Update persistent state
        self.state.update(self.parser)

        # Build world model
        self.world = World(self.parser)

        # Pathfinding
        self.pathfinder = Pathfinder(self.world)

        # Market
        self.market = Market(self.parser)

        self.market_memory.update(
            self.parser.prices
        )

        # Market Memory
        self.market_memory = MarketMemory()

        # Economy
        if hasattr(self.parser, "money"):
            self.economy.update(self.parser.money)

        # Strategy
        self.strategy = Strategy(self.parser)

        # Planner
        self.planner = Planner(
            parser=self.parser,
            world=self.world,
            market=self.market,
        )

    # =====================================================
    # Decision Engine
    # =====================================================

    def think(self):
        """
        Generate candidate tasks and select
        the highest-priority one.
        """

        # Reset scheduler
        self.scheduler.clear()

        # Planner generates tasks
        tasks = self.planner.plan()

        # Add every task
        for task in tasks:

            self.scheduler.add(
                priority=task["priority"],
                action=task["task"],
                target=task.get("target"),
                crop=task.get("crop"),
                product=task.get("product"),
                amount=task.get("amount"),
            )

        # Highest-priority task
        decision = self.scheduler.next()

        # Nothing to do
        if decision is None:
            return {
                "task": "PASS",
                "target": None,
            }

        target = decision.target

        # -------------------------------------------------
        # Tasks without movement
        # -------------------------------------------------

        if target is None:
            return {
                "task": decision.action,
                "target": None,
                "crop": decision.crop,
                "product": decision.product,
                "amount": decision.amount,
            }

        # -------------------------------------------------
        # Current farmer position
        # -------------------------------------------------

        current = self.parser.farmer_position

        # Already standing on destination
        if current == target:

            return {
                "task": decision.action,
                "target": target,
                "crop": decision.crop,
                "product": decision.product,
                "amount": decision.amount,
            }

        # -------------------------------------------------
        # Navigate toward destination
        # -------------------------------------------------

        path = self.pathfinder.find_path(
            current,
            target,
        )

        moves = self.pathfinder.directions(path)

        if moves:

            return {
                "task": moves[0],
                "target": None,
            }

        # No valid path
        return {
            "task": "PASS",
            "target": None,
        }

    # =====================================================
    # Main API
    # =====================================================

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

        # Convert to Kaggle action
        return self.actions.build(task)