"""
test_actions.py

Unit tests for the ActionBuilder.
"""

from src.actions import ActionBuilder


def test_pass_action():
    builder = ActionBuilder()

    action = builder.build({"task": "PASS"})

    assert action["farmer"] == ["PASS"]


def test_water_action():
    builder = ActionBuilder()

    action = builder.build({"task": "WATER"})

    assert action["farmer"] == ["WATER"]


def test_harvest_action():
    builder = ActionBuilder()

    action = builder.build({"task": "HARVEST"})

    assert action["farmer"] == ["HARVEST"]


def test_move_action():
    builder = ActionBuilder()

    action = builder.build({"task": "NORTH"})

    assert action["farmer"] == ["NORTH"]


def test_plant_action():
    builder = ActionBuilder()

    action = builder.build(
        {
            "task": "PLANT",
            "crop": "WHEAT",
        }
    )

    assert action["farmer"] == ["PLANT", "WHEAT"]


def test_sell_action():
    builder = ActionBuilder()

    action = builder.build(
        {
            "task": "SELL",
            "product": "WHEAT",
            "amount": 5,
        }
    )

    assert action["market"] == [["SELL", "WHEAT", 5]]