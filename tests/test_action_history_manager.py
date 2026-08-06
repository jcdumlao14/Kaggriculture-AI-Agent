from src.action_history_manager import ActionHistoryManager


def test_record():

    manager = ActionHistoryManager()

    manager.record(
        {"action": "PLANT"}
    )

    assert manager.count() == 1


def test_last_action():

    manager = ActionHistoryManager()

    manager.record(
        {"action": "HARVEST"}
    )

    assert (
        manager.last_action()["action"]
        == "HARVEST"
    )


def test_history():

    manager = ActionHistoryManager()

    manager.record(
        {"action": "PLANT"}
    )

    manager.record(
        {"action": "WATER"}
    )

    assert len(
        manager.history()
    ) == 2


def test_clear():

    manager = ActionHistoryManager()

    manager.record(
        {"action": "SELL"}
    )

    manager.clear()

    assert manager.count() == 0


def test_empty():

    manager = ActionHistoryManager()

    assert manager.last_action() is None