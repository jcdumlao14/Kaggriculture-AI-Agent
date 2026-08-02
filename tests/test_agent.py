from src.agent import Agent


def test_agent_returns_action():

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

    agent = Agent()

    action = agent.act(observation)

    assert isinstance(action, dict)

    assert "farmer" in action
    assert "hands" in action
    assert "market" in action
    