from src.decision_engine import DecisionEngine
from src.parser import ObservationParser


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

    parser = ObservationParser(observation)

    engine = DecisionEngine(parser)

    task = engine.next_task()

    assert task is not None