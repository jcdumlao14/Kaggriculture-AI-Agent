"""
target_selector.py

Target Selector for the Kaggriculture AI Agent.

Chooses the highest-priority target tile.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class TargetSelector:
    """
    Selects the next target tile.
    """

    def select(
        self,
        tiles,
    ):
        """
        Return the highest-priority tile.

        Priority:

        Harvest
        Water
        Empty
        """

        best = None
        best_priority = 999

        for y, row in enumerate(tiles):

            for x, tile in enumerate(row):

                if not isinstance(tile, dict):
                    continue

                priority = None

                if (
                    tile.get("kind") == "PLANT"
                    and tile.get("yield_units", 0) > 0
                ):
                    priority = 0

                elif (
                    tile.get("kind") == "PLANT"
                    and not tile.get(
                        "watered_today",
                        False,
                    )
                ):
                    priority = 1

                if priority is None:
                    continue

                if priority < best_priority:

                    best_priority = priority
                    best = (x, y)

        return best