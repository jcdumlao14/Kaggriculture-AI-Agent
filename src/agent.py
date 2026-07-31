"""
agent.py

Main AI Agent for Kaggriculture.

Coordinates all AI modules and returns valid
Kaggle actions for the current turn.

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
from src.scoring import CropScorer


class KaggricultureAgent:
    """
    Main AI Agent.

    Pipeline:

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
        Kaggle Action
    """

    def __init__(self):
        """Initialize all AI modules."""

        # Persistent memory
        self.state = StateManager()

        # Updated every turn
        self.parser = None
        self.world = None
        self.market = None
        self.strategy = None
        self.planner = None

        # Long-lived modules
        self.scheduler = Scheduler()
        self.economy = Economy()

        # Converts planner output into Kaggle actions
        self.actions = ActionBuilder()

    # ---------------------------------------------------------
    # Update Environment
    # ---------------------------------------------------------

    def update(self, observation):
        """
        Parse the latest observation and update all modules.
        """

        self.parser = ObservationParser(observation)

        # Update persistent memory
        self.state.update(self.parser)

        # Current world representation
        self.world = World(self.parser)

        # Market state
        self.market = Market(self.parser)

        # Crop Scorer
        self.scorer = CropScorer(self.parser)

        # Economy
        if hasattr(self.parser, "money"):
            self.economy.update(self.parser.money)

        # High-level strategy
        self.strategy = Strategy(self.parser)

        # Planner
        self.planner = Planner(
            self.parser,
            self.world,
        )

    # ---------------------------------------------------------
    # Decision Engine
    # ---------------------------------------------------------

    def think(self):
        """
        Generate candidate tasks and select
        the highest-priority one.
        """

        self.scheduler.clear()

        tasks = self.planner.plan()

        for task in tasks:

            self.scheduler.add(
                priority=task["priority"],
                action=task["task"],
                target=task["target"],
            )

        decision = self.scheduler.next()

        if decision is None:

            return {
                "task": "PASS",
                "target": None,
            }

        return {
            "task": decision.action,
            "target": decision.target,
        }

    # ---------------------------------------------------------
    # Main API
    # ---------------------------------------------------------

    def act(self, observation):
        """
        Main entry point.

        Parameters
        ----------
        observation : dict
            Kaggriculture observation.

        Returns
        -------
        dict
            Kaggle-compatible action dictionary.
        """

        # Update world
        self.update(observation)

        # AI decides the next task
        task = self.think()

        # Convert task into Kaggle action
        return self.actions.build(task)