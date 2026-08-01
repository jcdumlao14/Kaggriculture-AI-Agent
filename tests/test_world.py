"""
test_world.py

Unit tests for the World module.
"""

from src.parser import ObservationParser
from src.world import World


def make_observation():
    # Create an empty 10x10 farm
    tiles = [[None for _ in range(10)] for _ in range(10)]

    # Harvestable wheat plant
    tiles[1][1] = {
        "kind": "PLANT",
        "crop": "WHEAT",
        "yield_units": 5,
        "watered_today": False,
    }

    # Growing carrot (not harvestable)
    tiles[2][2] = {
        "kind": "PLANT",
        "crop": "CARROT",
        "yield_units": 0,
        "watered_today": True,
    }

    # Weed
    tiles[3][3] = {
        "kind": "WEED",
    }

    # Coop with goose
    tiles[4][4] = {
        "kind": "COOP",
        "animal": "GOOSE",
        "fed_today": False,
    }

    # Locked tile
    tiles[5][5] = {
        "kind": "LOCKED",
    }

    return {
        "player": 0,
        "day": 1,
        "hour": 0,
        "farms": [
            {
                "money": 3000,
                "farmer": [0, 0],
                "tiles": tiles,
            }
        ],
        "private": {
            "shed": {},
            "seeds": {},
            "inventories": {},
        },
        "market": {
            "prices": {},
            "inventory": {},
        },
        "town": {
            "unlocked_shops": [],
        },
    }


def build_world():
    parser = ObservationParser(make_observation())
    return World(parser)


def test_empty_tiles():
    world = build_world()
    assert len(world.empty_tiles()) > 0


def test_plants():
    world = build_world()
    assert len(world.plants()) == 2


def test_harvestable_plants():
    world = build_world()
    assert len(world.harvestable_plants()) == 1


def test_weeds():
    world = build_world()
    assert len(world.weeds()) == 1


def test_animals():
    world = build_world()
    assert len(world.animals()) == 1


def test_locked_tiles():
    world = build_world()
    assert len(world.locked_tiles()) == 1


def test_walkable():
    world = build_world()

    assert world.is_walkable(0, 0) is True
    assert world.is_walkable(5, 5) is False