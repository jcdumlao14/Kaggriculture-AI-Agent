from src.decision_engine import DecisionEngine
from src.parser import ObservationParser
from src.world import World
from src.market import Market


def test_engine_returns_task():

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
            "prices": {
                "WHEAT": 120,
            },
            "inventory": {},
        },
        "town": {
            "unlocked_shops": [],
        },
    }

    # Parse the observation
    parser = ObservationParser(observation)

    # Build helper modules
    world = World(parser)
    market = Market(parser)

    # Create the decision engine
    engine = DecisionEngine(
        parser,
        world,
        market,
    )

    # Get the next task
    task = engine.next_task()

    assert task is not None