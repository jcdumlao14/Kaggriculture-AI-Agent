"""
planting_opportunity_analyzer.py

Planting Opportunity Analyzer for the Kaggriculture AI Agent.

Analyzes available planting opportunities
on the farm.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class PlantingOpportunityAnalyzer:
    """
    Analyze planting opportunities.
    """

    # ---------------------------------------------------------

    def empty_tiles(
        self,
        tiles: list,
    ) -> list:
        """
        Return empty tiles.
        """

        return [
            tile
            for tile in tiles
            if tile is None
        ]

    # ---------------------------------------------------------

    def available_count(
        self,
        tiles: list,
    ) -> int:
        """
        Return number of empty tiles.
        """

        return len(
            self.empty_tiles(tiles)
        )

    # ---------------------------------------------------------

    def can_plant(
        self,
        *,
        empty_tiles: int,
        seed_count: int,
    ) -> bool:
        """
        Return True if planting is possible.
        """

        return (
            empty_tiles > 0
            and seed_count > 0
        )

    # ---------------------------------------------------------

    def next_tile(
        self,
        tiles: list,
    ):
        """
        Return first available tile.
        """

        for tile in tiles:
            if tile is None:
                return tile

        return None