"""
planner.py

High-level task planner for the Kaggriculture AI Agent.

The planner decides WHAT should happen next.

It does not worry about movement, pathfinding,
or market optimization.
"""

from __future__ import annotations

from src.constants import Action
from src.scoring import CropScorer


class Planner:
    """
    High-level planner.

    Generates a prioritized list of tasks based on
    the current world state.
    """

    def __init__(self, parser, world):
        self.parser = parser
        self.world = world
        self.scorer = CropScorer(parser)

    # ---------------------------------------------------------
    # Main Planner
    # ---------------------------------------------------------

    def plan(self):
        """
        Generate all available tasks.

        Returns
        -------
        list
            List of task dictionaries sorted later
            by the Scheduler.
        """

        tasks = []

        # -----------------------------------------------------
        # Harvest mature crops (Highest Priority)
        # -----------------------------------------------------

        for target in self.world.harvestable_plants():
            tasks.append(
                {
                    "priority": 1,
                    "task": Action.HARVEST.value,
                    "target": target,
                }
            )

        # -----------------------------------------------------
        # Water crops
        # -----------------------------------------------------

        for x, y, tile in self.world.plants():

            if not tile.get("watered_today", False):

                tasks.append(
                    {
                        "priority": 2,
                        "task": Action.WATER.value,
                        "target": (x, y),
                    }
                )

        # -----------------------------------------------------
        # Feed animals
        # -----------------------------------------------------

        for x, y, tile in self.world.animals():

            if not tile.get("fed_today", False):

                tasks.append(
                    {
                        "priority": 3,
                        "task": Action.FEED.value,
                        "target": (x, y),
                    }
                )

        # -----------------------------------------------------
        # Collect fertilizer
        # -----------------------------------------------------

        for x, y, tile in self.world.animals():

            if tile.get("fertilizer_available", False):

                tasks.append(
                    {
                        "priority": 4,
                        "task": Action.COLLECT_FERTILIZER.value,
                        "target": (x, y),
                    }
                )

        # -----------------------------------------------------
        # Intelligent Planting Strategy
        # -----------------------------------------------------

        best_crop = self.scorer.best_crop()

        for tile in self.world.empty_tiles():

            tasks.append(
                {
                    "priority": 5,
                    "task": Action.PLANT.value,
                    "crop": best_crop,
                    "target": tile,
                }
            )

        # -----------------------------------------------------
        # Nothing to do
        # -----------------------------------------------------

        if not tasks:

            tasks.append(
                {
                    "priority": 999,
                    "task": Action.PASS.value,
                    "target": None,
                }
            )

        return tasks