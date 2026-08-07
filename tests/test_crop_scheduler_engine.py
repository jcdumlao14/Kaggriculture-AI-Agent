from src.crop_scheduler_engine import (
    CropSchedulerEngine,
)


def test_plant():

    engine = CropSchedulerEngine()

    engine.plant(
        (2, 3),
        "WHEAT",
        1,
        2,
    )

    assert engine.crop_count() == 1


def test_ready():

    engine = CropSchedulerEngine()

    engine.plant(
        (0, 0),
        "CARROT",
        1,
        2,
    )

    assert engine.ready_to_harvest(
        (0, 0),
        3,
    )


def test_not_ready():

    engine = CropSchedulerEngine()

    engine.plant(
        (0, 0),
        "CARROT",
        1,
        3,
    )

    assert not engine.ready_to_harvest(
        (0, 0),
        2,
    )


def test_harvest():

    engine = CropSchedulerEngine()

    engine.plant(
        (1, 1),
        "TOMATO",
        2,
        4,
    )

    assert engine.harvest(
        (1, 1),
    )

    assert engine.crop_count() == 0


def test_watering():

    engine = CropSchedulerEngine()

    engine.plant(
        (4, 5),
        "MELON",
        1,
        6,
    )

    due = engine.watering_due(
        2,
    )

    assert (4, 5) in due