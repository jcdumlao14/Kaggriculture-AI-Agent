"""
planner.py

High-level task planner for the Kaggriculture AI Agent.

The planner decides WHAT should happen next.

It generates a prioritized list of tasks while leaving
movement, pathfinding, and execution to other modules.

Author: Jocelyn Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.constants import Action, MarketAction
from src.crop_strategy import CropStrategy


class Planner:
    """
    High-level Planner.

    Responsible for deciding WHAT should happen next.

    It does not decide HOW to reach the target—that is
    handled by the movement/pathfinding system.
    """

    def __init__(self, parser, world, market):
        """
        Parameters
        ----------
        parser : ObservationParser
            Parsed Kaggriculture observation.

        world : World
            World state helper.

        market : Market
            Market intelligence module.
        """

        self.parser = parser
        self.world = world
        self.market = market

        # Crop intelligence
        self.crop_strategy = CropStrategy(parser)

    # ---------------------------------------------------------
    # Main Planner
    # ---------------------------------------------------------

    def plan(self):
        """
        Generate every possible task.

        Returns
        -------
        list[dict]
            Candidate tasks.
        """

        tasks = []

        # =====================================================
        # 1. Harvest Mature Crops (Highest Priority)
        # =====================================================

        for target in self.world.harvestable_plants():

            tasks.append(
                {
                    "priority": 1,
                    "task": Action.HARVEST.value,
                    "target": target,
                }
            )

        # =====================================================
        # 2. Sell Products
        # =====================================================

        for product, amount in self.parser.shed.items():

            if amount <= 0:
                continue

            if self.market.should_sell(product):

                tasks.append(
                    {
                        "priority": 2,
                        "task": MarketAction.SELL.value,
                        "product": product,
                        "amount": amount,
                        "target": None,
                    }
                )

        # =====================================================
        # 3. Water Plants
        # =====================================================

        for x, y, tile in self.world.plants():

            if not tile.get("watered_today", False):

                tasks.append(
                    {
                        "priority": 3,
                        "task": Action.WATER.value,
                        "target": (x, y),
                    }
                )

        # =====================================================
        # 4. Feed Animals
        # =====================================================

        for x, y, tile in self.world.animals():

            if not tile.get("fed_today", False):

                tasks.append(
                    {
                        "priority": 4,
                        "task": Action.FEED.value,
                        "target": (x, y),
                    }
                )

        # =====================================================
        # 5. Collect Fertilizer
        # =====================================================

        for x, y, tile in self.world.animals():

            if tile.get("fertilizer_available", False):

                tasks.append(
                    {
                        "priority": 5,
                        "task": Action.COLLECT_FERTILIZER.value,
                        "target": (x, y),
                    }
                )

        # =====================================================
        # 6. Plant Best Crop
        # =====================================================

        best_crop = self.crop_strategy.best_crop()

        for tile in self.world.empty_tiles():

            tasks.append(
                {
                    "priority": 6,
                    "task": Action.PLANT.value,
                    "crop": best_crop,
                    "target": tile,
                }
            )

        # =====================================================
        # 7. Buy Fertilizer
        # =====================================================

        if self.market.should_buy_fertilizer():

            tasks.append(
                {
                    "priority": 7,
                    "task": MarketAction.BUY_PRODUCT.value,
                    "product": "FERTILIZER",
                    "amount": 1,
                    "target": None,
                }
            )

        # =====================================================
        # 8. Buy Wheat Seeds
        # =====================================================

        if self.market.should_buy_wheat():

            tasks.append(
                {
                    "priority": 8,
                    "task": MarketAction.BUY_PRODUCT.value,
                    "product": "WHEAT",
                    "amount": 5,
                    "target": None,
                }
            )

        # =====================================================
        # 9. Pass Turn
        # =====================================================

        if not tasks:

            tasks.append(
                {
                    "priority": 999,
                    "task": Action.PASS.value,
                    "target": None,
                }
            )

        # =====================================================
        # Sort Tasks
        # =====================================================

        tasks.sort(key=lambda task: task["priority"])

        return tasks