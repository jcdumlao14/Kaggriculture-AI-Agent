"""
world.py

World analysis module.

This module inspects the current farm and provides helper methods for
finding plants, weeds, animals, empty tiles, and unlocked land.

The planner should use this module instead of manually scanning the map.
"""

from __future__ import annotations

from typing import Any

from src.parser import ObservationParser


class World:

    def __init__(self, parser: ObservationParser):

        self.parser = parser
        self.tiles = parser.tiles
        self.size = len(self.tiles)

    # ---------------------------------------------------------
    # Empty Tiles
    # ---------------------------------------------------------

    def empty_tiles(self):

        results = []

        for y in range(self.size):
            for x in range(self.size):

                tile = self.tiles[y][x]

                if tile is None:
                    results.append((x, y))

        return results

    # ---------------------------------------------------------
    # Locked Tiles
    # ---------------------------------------------------------

    def locked_tiles(self):

        results = []

        for y in range(self.size):
            for x in range(self.size):

                if self.tiles[y][x] == "LOCKED":
                    results.append((x, y))

        return results

    # ---------------------------------------------------------
    # Weeds
    # ---------------------------------------------------------

    def weeds(self):

        results = []

        for y in range(self.size):
            for x in range(self.size):

                tile = self.tiles[y][x]

                if isinstance(tile, dict):

                    if tile.get("kind") == "WEED":
                        results.append((x, y))

        return results

    # ---------------------------------------------------------
    # Plants
    # ---------------------------------------------------------

    def plants(self):

        results = []

        for y in range(self.size):
            for x in range(self.size):

                tile = self.tiles[y][x]

                if isinstance(tile, dict):

                    if tile.get("kind") == "PLANT":
                        results.append((x, y, tile))

        return results

    # ---------------------------------------------------------
    # Harvest Ready
    # ---------------------------------------------------------

    def harvestable_plants(self):

        results = []

        for x, y, tile in self.plants():

            if tile.get("yield_units", 0) > 0:
                results.append((x, y, tile))

        return results

    # ---------------------------------------------------------
    # Animals
    # ---------------------------------------------------------

    def animals(self):

        results = []

        for y in range(self.size):
            for x in range(self.size):

                tile = self.tiles[y][x]

                if isinstance(tile, dict):

                    if tile.get("kind") in ("COOP", "PASTURE"):

                        if tile.get("animal") is not None:
                            results.append((x, y, tile))

        return results

    # ---------------------------------------------------------
    # Structures
    # ---------------------------------------------------------

    def structures(self):

        results = []

        for y in range(self.size):
            for x in range(self.size):

                tile = self.tiles[y][x]

                if isinstance(tile, dict):

                    if tile.get("kind") in ("COOP", "PASTURE"):
                        results.append((x, y, tile))

        return results