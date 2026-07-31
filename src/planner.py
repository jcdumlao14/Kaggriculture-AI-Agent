"""
planner.py

High-level task planner for the Kaggriculture AI Agent.

The planner decides WHAT should happen next.

It does not worry about pathfinding or market optimization.
Those modules are handled separately.
"""

from __future__ import annotations

from src.constants import Action


class Planner:
    """
    High-level planner.

    Determines the next task based on the current game state.
    """

    def __init__(self, parser, world):

        self.parser = parser
        self.world = world

    # ---------------------------------------------------------
    # Main Planner
    # ---------------------------------------------------------

    def plan(self):
        """
        Returns the highest priority task.
        """

        # 1. Harvest crops

        crops = self.world.harvestable_plants()

        if crops:
            return {
                "task": "HARVEST",
                "target": crops[0],
            }

        # -----------------------------------------------------

        # 2. Water crops

        for x, y, tile in self.world.plants():

            if not tile.get("watered_today", False):

                return {
                    "task": "WATER",
                    "target": (x, y),
                }

        # -----------------------------------------------------

        # 3. Feed animals

        for x, y, tile in self.world.animals():

            if not tile.get("fed_today", False):

                return {
                    "task": "FEED",
                    "target": (x, y),
                }

        # -----------------------------------------------------

        # 4. Collect fertilizer

        for x, y, tile in self.world.animals():

            if tile.get("fertilizer_available", False):

                return {
                    "task": "COLLECT_FERTILIZER",
                    "target": (x, y),
                }

        # -----------------------------------------------------

        # 5. Plant

        empty = self.world.empty_tiles()

        if empty:

            return {
                "task": "PLANT",
                "target": empty[0],
            }

        # -----------------------------------------------------

        # Nothing to do

        return {
            "task": Action.PASS,
            "target": None,
        }