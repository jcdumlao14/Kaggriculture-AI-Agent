"""
parser.py

Utility functions for extracting information from the Kaggriculture
observation dictionary.

This module keeps the rest of the AI independent of the raw observation
format provided by Kaggle.
"""

from __future__ import annotations

from typing import Any


class ObservationParser:
    """
    Helper class for reading the Kaggriculture observation.
    """

    def __init__(self, obs: dict[str, Any]):
        self.obs = obs
        self.player = obs["player"]
        self.farm = obs["farms"][self.player]
        self.private = obs["private"]
        self.market = obs["market"]
        self.town = obs["town"]

    # -------------------------------------------------------
    # Time
    # -------------------------------------------------------

    @property
    def day(self) -> int:
        return self.obs["day"]

    @property
    def hour(self) -> int:
        return self.obs["hour"]

    # -------------------------------------------------------
    # Money
    # -------------------------------------------------------

    @property
    def money(self) -> float:
        return self.farm["money"]

    # -------------------------------------------------------
    # Farmer Position
    # -------------------------------------------------------

    @property
    def farmer_position(self) -> tuple[int, int]:
        x, y = self.farm["farmer"]
        return x, y

    # -------------------------------------------------------
    # Tiles
    # -------------------------------------------------------

    @property
    def tiles(self):
        return self.farm["tiles"]

    def tile(self, x: int, y: int):
        return self.tiles[y][x]

    @property
    def current_tile(self):
        x, y = self.farmer_position
        return self.tile(x, y)

    # -------------------------------------------------------
    # Private Inventory
    # -------------------------------------------------------

    @property
    def shed(self):
        return self.private["shed"]

    @property
    def seeds(self):
        return self.private["seeds"]

    @property
    def inventories(self):
        return self.private["inventories"]

    # -------------------------------------------------------
    # Market
    # -------------------------------------------------------

    @property
    def prices(self):
        return self.market["prices"]

    @property
    def inventory(self):
        return self.market["inventory"]

    # -------------------------------------------------------
    # Town
    # -------------------------------------------------------

    @property
    def unlocked_shops(self):
        return self.town["unlocked_shops"]