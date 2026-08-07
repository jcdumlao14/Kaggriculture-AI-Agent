from src.resource_allocation_engine import (
    ResourceAllocationEngine,
)


def test_set_resource():

    engine = ResourceAllocationEngine()

    engine.set_resource(
        "money",
        1000,
    )

    assert engine.available(
        "money",
    ) == 1000.0


def test_can_afford():

    engine = ResourceAllocationEngine()

    engine.set_resource(
        "money",
        500,
    )

    assert engine.can_afford(
        "money",
        200,
    )


def test_spend():

    engine = ResourceAllocationEngine()

    engine.set_resource(
        "money",
        500,
    )

    assert engine.spend(
        "money",
        300,
    )

    assert engine.available(
        "money",
    ) == 200.0


def test_add():

    engine = ResourceAllocationEngine()

    engine.add(
        "money",
        150,
    )

    assert engine.available(
        "money",
    ) == 150.0


def test_insufficient():

    engine = ResourceAllocationEngine()

    engine.set_resource(
        "money",
        100,
    )

    assert not engine.spend(
        "money",
        200,
    )