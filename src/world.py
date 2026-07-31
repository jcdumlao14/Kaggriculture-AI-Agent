"""
world.py

World analysis module.

This module inspects the current farm and provides helper methods for
finding plants, weeds, animals, empty tiles, locked land, and
walkable locations.

The planner should use this module instead of manually scanning the map.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.parser import ObservationParser
from src.constants import BOARD_SIZE, TileKind


class World:
    """
    Represents the current farm world.

    Provides helper methods for querying the farm without exposing
    the raw observation structure.
    """

    def __init__(self, parser: ObservationParser):
        self.parser = parser
        self.tiles = parser.tiles
        self.size = len(self.tiles)

    # =========================================================
    # Basic Helpers
    # =========================================================

    def in_bounds(self, x: int, y: int) -> bool:
        """
        Return True if the coordinate is inside the farm.
        """

        return (
            0 <= x < BOARD_SIZE
            and
            0 <= y < BOARD_SIZE
        )

    # ---------------------------------------------------------

    def tile(self, x: int, y: int):
        """
        Return the tile located at (x, y).
        """

        return self.tiles[y][x]

    # ---------------------------------------------------------

    def is_walkable(self, x: int, y: int) -> bool:
        """
        Return True if the farmer can stand on the tile.
        """

        if not self.in_bounds(x, y):
            return False

        tile = self.tile(x, y)

        # Empty land
        if tile is None:
            return True

        # Locked land represented as a string
        if tile == "LOCKED":
            return False

        # Tile represented as a dictionary
        if isinstance(tile, dict):

            kind = tile.get("kind", "EMPTY")

            blocked = {
                TileKind.LOCKED.value,
                TileKind.COOP.value,
                TileKind.PASTURE.value,
            }

            return kind not in blocked

        return True

    # =========================================================
    # Empty Tiles
    # =========================================================

    def empty_tiles(self):
        """
        Return all empty farm tiles.
        """

        results = []

        for y in range(self.size):
            for x in range(self.size):

                tile = self.tiles[y][x]

                if tile is None:
                    results.append((x, y))

                elif (
                    isinstance(tile, dict)
                    and tile.get("kind") == "EMPTY"
                ):
                    results.append((x, y))

        return results

    # =========================================================
    # Locked Tiles
    # =========================================================

    def locked_tiles(self):
        """
        Return all locked tiles.
        """

        results = []

        for y in range(self.size):
            for x in range(self.size):

                tile = self.tiles[y][x]

                if tile == "LOCKED":
                    results.append((x, y))

                elif (
                    isinstance(tile, dict)
                    and tile.get("kind") == TileKind.LOCKED.value
                ):
                    results.append((x, y))

        return results

    # =========================================================
    # Weeds
    # =========================================================

    def weeds(self):
        """
        Return all weed tiles.
        """

        results = []

        for y in range(self.size):
            for x in range(self.size):

                tile = self.tiles[y][x]

                if (
                    isinstance(tile, dict)
                    and tile.get("kind") == TileKind.WEED.value
                ):
                    results.append((x, y))

        return results

    # =========================================================
    # Plants
    # =========================================================

    def plants(self):
        """
        Return every planted crop.
        """

        results = []

        for y in range(self.size):
            for x in range(self.size):

                tile = self.tiles[y][x]

                if (
                    isinstance(tile, dict)
                    and tile.get("kind") == TileKind.PLANT.value
                ):
                    results.append((x, y, tile))

        return results

    # =========================================================
    # Harvestable Plants
    # =========================================================

    def harvestable_plants(self):
        """
        Return mature crops ready for harvest.
        """

        results = []

        for x, y, tile in self.plants():

            if tile.get("yield_units", 0) > 0:
                results.append((x, y, tile))

        return results

    # =========================================================
    # Animals
    # =========================================================

    def animals(self):
        """
        Return all animal buildings containing animals.
        """

        results = []

        for y in range(self.size):
            for x in range(self.size):

                tile = self.tiles[y][x]

                if not isinstance(tile, dict):
                    continue

                if tile.get("kind") in (
                    TileKind.COOP.value,
                    TileKind.PASTURE.value,
                ):

                    if tile.get("animal") is not None:
                        results.append((x, y, tile))

        return results

    # =========================================================
    # Structures
    # =========================================================

    def structures(self):
        """
        Return all farm structures.
        """

        results = []

        for y in range(self.size):
            for x in range(self.size):

                tile = self.tiles[y][x]

                if not isinstance(tile, dict):
                    continue

                if tile.get("kind") in (
                    TileKind.COOP.value,
                    TileKind.PASTURE.value,
                ):
                    results.append((x, y, tile))

        return results