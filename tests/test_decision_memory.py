from src.decision_memory import DecisionMemory


def test_add():

    memory = DecisionMemory()

    memory.add(
        {"action": "PLANT"},
        25,
    )

    assert len(memory.decisions()) == 1


def test_last():

    memory = DecisionMemory()

    memory.add(
        {"action": "SELL"},
        80,
    )

    assert (
        memory.last()["action"]["action"]
        == "SELL"
    )


def test_average():

    memory = DecisionMemory()

    memory.add(
        {"action": "PLANT"},
        10,
    )

    memory.add(
        {"action": "HARVEST"},
        30,
    )

    assert memory.average_score() == 20.0


def test_clear():

    memory = DecisionMemory()

    memory.add(
        {"action": "BUY"},
        5,
    )

    memory.clear()

    assert len(memory.decisions()) == 0


def test_empty_average():

    memory = DecisionMemory()

    assert memory.average_score() == 0.0