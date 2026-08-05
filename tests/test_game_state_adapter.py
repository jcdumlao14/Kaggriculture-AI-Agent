from src.game_state_adapter import GameStateAdapter


def sample_observation():

    return {
        "player": 0,
        "day": 1,
        "hour": 5,
        "farms": [
            {
                "money": 500,
                "tiles": [[None]],
                "farmer": [0, 0],
                "hands": [[1, 0]],
                "unlocked_quadrants": ["NW"],
                "hires_today": 0,
            }
        ],
        "market": {
            "prices": {
                "WHEAT": 20,
            }
        },
        "town": {},
        "private": {
            "shed": {
                "WHEAT": 3,
            },
            "seeds": {},
            "inventories": [],
        },
    }


def test_adapt():

    adapter = GameStateAdapter()

    state = adapter.adapt(sample_observation())

    assert state["money"] == 500


def test_tile_count():

    adapter = GameStateAdapter()

    assert adapter.tile_count(sample_observation()) == 1


def test_inventory_size():

    adapter = GameStateAdapter()

    assert adapter.inventory_size(sample_observation()) == 1


def test_worker_count():

    adapter = GameStateAdapter()

    assert adapter.worker_count(sample_observation()) == 1


def test_defaults():

    adapter = GameStateAdapter()

    state = adapter.adapt({})

    assert state["money"] == 0