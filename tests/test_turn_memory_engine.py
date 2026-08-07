from src.turn_memory_engine import (
    TurnMemoryEngine,
)


def test_remember():

    memory = TurnMemoryEngine()

    memory.remember(
        "last_action",
        "HARVEST",
    )

    assert (
        memory.recall(
            "last_action",
        )
        == "HARVEST"
    )


def test_default():

    memory = TurnMemoryEngine()

    assert (
        memory.recall(
            "missing",
            "NONE",
        )
        == "NONE"
    )


def test_forget():

    memory = TurnMemoryEngine()

    memory.remember(
        "crop",
        "WHEAT",
    )

    memory.forget(
        "crop",
    )

    assert (
        memory.recall(
            "crop",
        )
        is None
    )


def test_clear():

    memory = TurnMemoryEngine()

    memory.remember(
        "a",
        1,
    )

    memory.remember(
        "b",
        2,
    )

    memory.clear()

    assert (
        memory.keys()
        == []
    )


def test_keys():

    memory = TurnMemoryEngine()

    memory.remember(
        "b",
        1,
    )

    memory.remember(
        "a",
        2,
    )

    assert (
        memory.keys()
        == ["a", "b"]
    )