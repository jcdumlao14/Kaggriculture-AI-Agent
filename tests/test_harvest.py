from src.parser import ObservationParser
from src.world import World
from src.market import Market
from src.planner import Planner

def test_harvest_task_exists():
    observation = {
        "player": 0,
        "day": 1,
        "hour": 0,
        "farms": [
            {
                "money": 3000,
                "farmer": [0, 0],
                "tiles": [
                    [
                        {
                            "kind": "PLANT",
                            "yield_units": 5,
                            "watered_today": True,
                        }
                    ] + [None] * 9
                ] + [[None] * 10 for _ in range(9)],
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

    parser = ObservationParser(observation)
    world = World(parser)
    market = Market(parser)

    planner = Planner(parser, world, market)

    tasks = planner.plan()

    assert any(task["task"] == "HARVEST" for task in tasks)