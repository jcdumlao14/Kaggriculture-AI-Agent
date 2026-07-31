"""
constants.py

Global constants and enumerations for the Kaggriculture AI Agent.

These values describe the game environment and should never
contain decision-making logic.

Author: Jocelyn Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from enum import Enum


# ============================================================
# Game Configuration
# ============================================================

BOARD_SIZE = 10
QUADRANT_SIZE = 5

TURNS_PER_DAY = 24
TOTAL_DAYS = 30
TOTAL_TURNS = 720

STARTING_MONEY = 3000

SHED_CAPACITY = 100

MAX_MARKET_ORDERS = 10


# ============================================================
# Directions
# ============================================================

class Direction(str, Enum):
    """Movement directions."""

    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"


DIRECTION_VECTOR = {
    Direction.NORTH: (0, -1),
    Direction.SOUTH: (0, 1),
    Direction.EAST: (1, 0),
    Direction.WEST: (-1, 0),
}


# ============================================================
# Farmer Actions
# ============================================================

class Action(str, Enum):

    PASS = "PASS"

    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"

    PLANT = "PLANT"
    WATER = "WATER"
    HARVEST = "HARVEST"
    DIG = "DIG"

    FERTILIZE = "FERTILIZE"

    FEED = "FEED"
    CARE = "CARE"

    COLLECT_FERTILIZER = "COLLECT_FERTILIZER"

    PICKUP = "PICKUP"
    PLACE = "PLACE"
    DROP = "DROP"

    BUILD_COOP = "BUILD_COOP"
    BUILD_PASTURE = "BUILD_PASTURE"

# ============================================================
# Crops
# ============================================================

class Crop(str, Enum):
    WHEAT = "WHEAT"
    CARROT = "CARROT"
    TOMATO = "TOMATO"
    STRAWBERRY = "STRAWBERRY"
    MELON = "MELON"


# ============================================================
# Animals
# ============================================================

class Animal(str, Enum):
    GOOSE = "GOOSE"
    COW = "COW"
    SHEEP = "SHEEP"


# ============================================================
# Buildings
# ============================================================

class Building(str, Enum):
    COOP = "COOP"
    PASTURE = "PASTURE"


# ============================================================
# Products
# ============================================================

class Product(str, Enum):
    WHEAT = "WHEAT"
    CARROT = "CARROT"
    TOMATO = "TOMATO"
    STRAWBERRY = "STRAWBERRY"
    MELON = "MELON"

    EGG = "EGG"
    MILK = "MILK"
    WOOL = "WOOL"

    FERTILIZER = "FERTILIZER"


# ============================================================
# Tile Types
# ============================================================

class TileKind(str, Enum):
    PLANT = "PLANT"
    WEED = "WEED"
    COOP = "COOP"
    PASTURE = "PASTURE"
    LOCKED = "LOCKED"

# ============================================================
# Farm Quadrants
# ============================================================

class Quadrant(str, Enum):
    NW = "NW"
    NE = "NE"
    SW = "SW"
    SE = "SE"


# ============================================================
# Town Shops
# ============================================================

class Shop(str, Enum):
    BAKERY = "BAKERY"
    PIZZA_SHOP = "PIZZA_SHOP"
    BRUNCH_SPOT = "BRUNCH_SPOT"
    YARN_STORE = "YARN_STORE"
    ICE_CREAM_SHOP = "ICE_CREAM_SHOP"
    PET_CAFE = "PET_CAFE"
    SMOOTHIE_SHOP = "SMOOTHIE_SHOP"
    FARMERS_MARKET = "FARMERS_MARKET"

# ============================================================
# Useful Collections
# ============================================================

ALL_CROPS = tuple(Crop)

ALL_ANIMALS = tuple(Animal)

ALL_PRODUCTS = tuple(Product)

ALL_SHOPS = tuple(Shop)