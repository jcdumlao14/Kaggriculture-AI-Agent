"""
actions.py

Converts planner decisions into valid Kaggle actions.

Author: Jocelyn Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.constants import Action


class ActionBuilder:
    """
    Builds Kaggle-compatible action dictionaries.
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # Main Builder
    # ---------------------------------------------------------

    def build(self, task):

        if task is None:

            return self.pass_turn()

        action = task.get("task")

        # ---------------- Farmer ----------------

        if action == Action.PASS.value:
            farmer = ["PASS"]

        elif action == Action.WATER.value:
            farmer = ["WATER"]

        elif action == Action.HARVEST.value:
            farmer = ["HARVEST"]

        elif action == Action.FEED.value:
            farmer = ["FEED"]

        elif action == Action.CARE.value:
            farmer = ["CARE"]

        elif action == Action.FERTILIZE.value:
            farmer = ["FERTILIZE"]

        elif action == Action.COLLECT_FERTILIZER.value:
            farmer = ["COLLECT_FERTILIZER"]

        elif action == Action.DIG.value:
            farmer = ["DIG"]

        elif action == Action.PLANT.value:

            # Default crop for Version 1
            farmer = ["PLANT", "WHEAT"]

        else:

            farmer = ["PASS"]

        return {
            "farmer": farmer,
            "hands": [],
            "market": [],
        }

    # ---------------------------------------------------------

    def pass_turn(self):

        return {
            "farmer": ["PASS"],
            "hands": [],
            "market": [],
        }