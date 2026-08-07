from src.animal_scheduler_engine import (
    AnimalSchedulerEngine,
)


def test_add():

    engine = AnimalSchedulerEngine()

    engine.add_animal(
        (1, 1),
        "COW",
        1,
    )

    assert engine.animal_count() == 1


def test_feed_due():

    engine = AnimalSchedulerEngine()

    engine.add_animal(
        (0, 0),
        "SHEEP",
        1,
    )

    due = engine.feeding_due(2)

    assert (0, 0) in due


def test_feed():

    engine = AnimalSchedulerEngine()

    engine.add_animal(
        (2, 2),
        "GOOSE",
        1,
    )

    engine.feed(
        (2, 2),
        2,
    )

    assert engine.feeding_due(2) == []


def test_care_due():

    engine = AnimalSchedulerEngine()

    engine.add_animal(
        (3, 3),
        "COW",
        1,
    )

    assert (3, 3) in engine.care_due(2)


def test_care():

    engine = AnimalSchedulerEngine()

    engine.add_animal(
        (4, 4),
        "GOOSE",
        1,
    )

    engine.care(
        (4, 4),
        2,
    )

    assert engine.care_due(2) == []