from src.farmer_action_generator import (
    FarmerActionGenerator,
)


def test_harvest():

    generator = FarmerActionGenerator()

    state = {
        "farmer": [0, 0],
        "tiles": [[{
            "kind": "PLANT",
            "yield_units": 3,
            "watered_today": True,
        }]],
        "seeds": {},
    }

    actions = generator.generate(state)

    assert ["HARVEST"] in actions


def test_water():

    generator = FarmerActionGenerator()

    state = {
        "farmer": [0, 0],
        "tiles": [[{
            "kind": "PLANT",
            "yield_units": 0,
            "watered_today": False,
        }]],
        "seeds": {},
    }

    actions = generator.generate(state)

    assert ["WATER"] in actions


def test_plant():

    generator = FarmerActionGenerator()

    state = {
        "farmer": [0, 0],
        "tiles": [[None]],
        "seeds": {
            "MELON": 1,
        },
    }

    actions = generator.generate(state)

    assert ["PLANT", "MELON"] in actions


def test_pass():

    generator = FarmerActionGenerator()

    actions = generator.generate({})

    assert ["PASS"] in actions


def test_return_type():

    generator = FarmerActionGenerator()

    assert isinstance(generator.generate({}), list)