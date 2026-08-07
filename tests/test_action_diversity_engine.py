from src.action_diversity_engine import (
    ActionDiversityEngine,
)


def test_record():

    engine = ActionDiversityEngine()

    engine.record(
        "HARVEST",
    )

    assert (
        engine.frequency(
            "HARVEST",
        )
        == 1
    )


def test_bonus():

    engine = ActionDiversityEngine()

    assert (
        engine.diversity_bonus(
            "MOVE",
        )
        == 1.0
    )


def test_penalty():

    engine = ActionDiversityEngine()

    engine.record("MOVE")
    engine.record("MOVE")

    assert (
        engine.diversity_bonus(
            "MOVE",
        )
        < 1.0
    )


def test_window():

    engine = ActionDiversityEngine(
        window=2,
    )

    engine.record("A")
    engine.record("B")
    engine.record("C")

    assert (
        engine.frequency("A")
        == 0
    )


def test_clear():

    engine = ActionDiversityEngine()

    engine.record(
        "SELL",
    )

    engine.clear()

    assert (
        engine.frequency(
            "SELL",
        )
        == 0
    )