from src.parser import ObservationParser
from src.world import World
from src.market import Market
from src.planner import Planner


def test_empty_world_returns_tasks():
    observation = {
        "player": 0,
        "day": 1,
        "hour": 0,
        "farms": [
            {
                "money": 3000,
                "farmer": [0, 0],
                "tiles": [[None] * 10 for _ in range(10)],
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

    planner = Planner(
        parser=parser,
        world=world,
        market=market,
    )

    tasks = planner.plan()

    assert isinstance(tasks, list)
    assert len(tasks) > 0

def test_empty_world_returns_tasks():
    ...

def test_harvest_task_exists():
    ...

def test_water_task_exists():
    ...

def test_feed_task_exists():
    ...

def test_sell_task_exists():
    ...