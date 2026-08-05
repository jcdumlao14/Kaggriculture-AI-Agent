"""
watering_priority_analyzer.py

Watering Priority Analyzer for the Kaggriculture AI Agent.

Identifies crops that require watering and
prioritizes them.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class WateringPriorityAnalyzer:
    """
    Analyze watering priorities.
    """

    # ---------------------------------------------------------

    def needs_water(
        self,
        tile: dict,
    ) -> bool:
        """
        Return True if the crop needs watering.
        """

        return (
            tile.get("kind") == "PLANT"
            and not tile.get("watered_today", False)
        )

    # ---------------------------------------------------------

    def candidates(
        self,
        tiles: list[dict],
    ) -> list[dict]:
        """
        Return all crops needing water.
        """

        return [
            tile
            for tile in tiles
            if self.needs_water(tile)
        ]

    # ---------------------------------------------------------

    def count(
        self,
        tiles: list[dict],
    ) -> int:
        """
        Return number of crops needing water.
        """

        return len(self.candidates(tiles))

    # ---------------------------------------------------------

    def urgent(
        self,
        tiles: list[dict],
    ) -> dict | None:
        """
        Return the crop with the highest
        consecutive_unwatered value.
        """

        candidates = self.candidates(tiles)

        if not candidates:
            return None

        return max(
            candidates,
            key=lambda tile: tile.get(
                "consecutive_unwatered",
                0,
            ),
        )