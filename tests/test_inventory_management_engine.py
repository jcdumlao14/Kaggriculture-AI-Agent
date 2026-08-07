from src.inventory_management_engine import (
    InventoryManagementEngine,
)


def test_add():

    engine = InventoryManagementEngine()

    engine.add(
        "WHEAT",
        3,
    )

    assert engine.count(
        "WHEAT",
    ) == 3


def test_remove():

    engine = InventoryManagementEngine()

    engine.add(
        "WHEAT",
        5,
    )

    assert engine.remove(
        "WHEAT",
        2,
    )

    assert engine.count(
        "WHEAT",
    ) == 3


def test_has():

    engine = InventoryManagementEngine()

    engine.add(
        "CARROT",
        4,
    )

    assert engine.has(
        "CARROT",
        2,
    )


def test_remove_fail():

    engine = InventoryManagementEngine()

    assert not engine.remove(
        "MELON",
        1,
    )


def test_clear():

    engine = InventoryManagementEngine()

    engine.add(
        "WHEAT",
        10,
    )

    engine.clear()

    assert engine.count(
        "WHEAT",
    ) == 0