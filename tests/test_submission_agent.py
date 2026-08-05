from submission.agent import agent


def sample_state():

    return {
        "player": 0,
        "day": 1,
        "hour": 5,
        "farms": [
            {
                "money": 500,
                "farmer": [0, 0],
                "hands": [],
                "tiles": [
                    [
                        {
                            "kind": "PLANT",
                            "yield_units": 2,
                            "watered_today": True,
                        }
                    ]
                ],
            }
        ],
        "market": {
            "prices": {
                "MELON": 250,
            }
        },
        "private": {
            "shed": {
                "MELON": 4,
            },
            "seeds": {
                "MELON": 0,
            },
            "inventories": [],
        },
    }


def test_return_type():

    assert isinstance(
        agent(sample_state()),
        dict,
    )


def test_farmer_exists():

    action = agent(sample_state())

    assert "farmer" in action


def test_market_exists():

    action = agent(sample_state())

    assert "market" in action


def test_hands_exists():

    action = agent(sample_state())

    assert "hands" in action


def test_harvest():

    action = agent(sample_state())

    assert action["farmer"] == ["HARVEST"]