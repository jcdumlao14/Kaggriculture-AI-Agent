from src.target_selector import TargetSelector


def test_harvest_priority():

    selector = TargetSelector()

    tiles = [[
        {
            "kind": "PLANT",
            "yield_units": 3,
            "watered_today": True,
        }
    ]]

    assert selector.select(tiles) == (0, 0)


def test_water_priority():

    selector = TargetSelector()

    tiles = [[
        {
            "kind": "PLANT",
            "yield_units": 0,
            "watered_today": False,
        }
    ]]

    assert selector.select(tiles) == (0, 0)


def test_harvest_over_water():

    selector = TargetSelector()

    tiles = [[
        {
            "kind": "PLANT",
            "yield_units": 0,
            "watered_today": False,
        },
        {
            "kind": "PLANT",
            "yield_units": 2,
            "watered_today": True,
        },
    ]]

    assert selector.select(tiles) == (1, 0)


def test_none():

    selector = TargetSelector()

    assert selector.select([[None]]) is None


def test_empty():

    selector = TargetSelector()

    assert selector.select([]) is None