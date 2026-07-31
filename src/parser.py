"""
parser.py

Observation parser for the Kaggriculture AI Agent.

This module converts the raw Kaggle observation into a clean,
easy-to-use interface for the rest of the AI.

Author: Jocelyn Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from typing import Any


class ObservationParser:
    """
    Helper class for accessing the Kaggriculture observation.

    Instead of reading deeply nested dictionaries throughout the code,
    every module should use this parser.
    """

    def __init__(self, obs: dict[str, Any]):
        """
        Initialize the parser.

        Parameters
        ----------
        obs : dict
            Raw observation provided by Kaggle.
        """

        self.obs = obs

        # -----------------------------------------------------
        # Player Information
        # -----------------------------------------------------

        self.player = obs["player"]

        self.farm = obs["farms"][self.player]

        self.private = obs["private"]

        self.market = obs["market"]

        self.town = obs["town"]

        # -----------------------------------------------------
        # Frequently Used Shortcuts
        # -----------------------------------------------------

        self._tiles = self.farm["tiles"]

        self._farmer = tuple(self.farm["farmer"])

        self._money = self.farm["money"]

    # =========================================================
    # Time
    # =========================================================

    @property
    def day(self) -> int:
        """Current game day."""
        return self.obs["day"]

    @property
    def hour(self) -> int:
        """Current hour within the day."""
        return self.obs["hour"]

    @property
    def step(self) -> int:
        """
        Total turn number.
        """
        return self.day * 24 + self.hour

    # =========================================================
    # Farm
    # =========================================================

    @property
    def money(self) -> float:
        """Current player money."""
        return self._money

    @property
    def farmer(self) -> tuple[int, int]:
        """Farmer position."""
        return self._farmer

    @property
    def farmer_position(self) -> tuple[int, int]:
        """Alias for farmer position."""
        return self._farmer

    @property
    def hands(self):
        """Farm hand positions."""
        return self.farm.get("hands", [])

    @property
    def tiles(self):
        """Entire farm tile grid."""
        return self._tiles

    @property
    def unlocked_quadrants(self):
        """Purchased land."""
        return self.farm.get("unlocked_quadrants", [])

    @property
    def hires_today(self):
        """Number of workers hired today."""
        return self.farm.get("hires_today", 0)

    # =========================================================
    # Tile Helpers
    # =========================================================

    def tile(self, x: int, y: int):
        """Return a tile."""
        return self._tiles[y][x]

    @property
    def current_tile(self):
        """Tile underneath the farmer."""
        x, y = self._farmer
        return self.tile(x, y)

    # =========================================================
    # Private Inventory
    # =========================================================

    @property
    def shed(self):
        """Items stored inside the shed."""
        return self.private.get("shed", {})

    @property
    def seeds(self):
        """Available seeds."""
        return self.private.get("seeds", {})

    @property
    def inventories(self):
        """Inventories of farmer and farm hands."""
        return self.private.get("inventories", [])

    # =========================================================
    # Market
    # =========================================================

    @property
    def prices(self):
        """Current market prices."""
        return self.market.get("prices", {})

    @property
    def inventory(self):
        """Current market inventory."""
        return self.market.get("inventory", {})

    # =========================================================
    # Town
    # =========================================================

    @property
    def unlocked_shops(self):
        """Unlocked town shops."""
        return self.town.get("unlocked_shops", [])

    # =========================================================
    # Opponent Information
    # =========================================================

    @property
    def opponent(self):
        """Opponent's public farm."""
        return self.obs["farms"][1 - self.player]

    @property
    def opponent_money(self):
        """Opponent's current money."""
        return self.opponent["money"]

    @property
    def opponent_farmer(self):
        """Opponent farmer position."""
        return tuple(self.opponent["farmer"])

    # =========================================================
    # Utility Functions
    # =========================================================

    def has_seed(self, crop: str) -> bool:
        """Return True if the player owns at least one seed."""
        return self.seeds.get(crop, 0) > 0

    def shed_count(self, item: str) -> int:
        """Number of items in the shed."""
        return self.shed.get(item, 0)

    def market_price(self, product: str) -> int:
        """Current market price."""
        return self.prices.get(product, 0)

    def market_inventory(self, product: str) -> int:
        """Current market inventory."""
        return self.inventory.get(product, 0)

    # =========================================================
    # Debugging
    # =========================================================

    def summary(self) -> dict:
        """
        Return a quick summary of the current observation.
        """

        return {
            "day": self.day,
            "hour": self.hour,
            "money": self.money,
            "farmer": self.farmer,
            "hands": len(self.hands),
            "shops": self.unlocked_shops,
        }