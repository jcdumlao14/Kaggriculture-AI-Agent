"""
agent.py

Main AI Agent for Kaggriculture.

Coordinates all AI modules and returns the next
high-level action for the current turn.

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


class KaggricultureAgent:
    """
    Main AI Agent.

    This class coordinates every subsystem:
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
        Selected Action
    """

    def __init__(self):
        """Initialize all AI modules."""

        # Persistent state
        self.state = StateManager()

        # Dynamic modules (updated every turn)
        self.parser = None
        self.world = None
        self.market = None
        self.strategy = None
        self.planner = None

        # Static modules
        self.scheduler = Scheduler()
        self.economy = Economy()

    # ---------------------------------------------------------
    # Update Environment
    # ---------------------------------------------------------

    def update(self, observation):
        """
        Parse the latest observation and update every module.
        """

        self.parser = ObservationParser(observation)

        # Update persistent memory
        self.state.update(self.parser)

        # Rebuild world representation
        self.world = World(self.parser)

        # Market analysis
        self.market = Market(self.parser)

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
        Generate tasks and allow the scheduler
        to choose the highest priority task.
        """

        # Reset scheduler
        self.scheduler.clear()

        # Planner generates all tasks
        tasks = self.planner.plan()

        # Add tasks into scheduler
        for task in tasks:
            self.scheduler.add(
                priority=task["priority"],
                action=task["task"],
                target=task["target"],
            )

        # Select highest priority task
        decision = self.scheduler.next()

        # Nothing to do
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
            High-level task selected by the AI.
        """

        self.update(observation)

        return self.think()