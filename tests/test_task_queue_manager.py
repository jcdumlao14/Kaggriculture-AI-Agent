from src.task_queue_manager import (
    TaskQueueManager,
)


def test_add():

    queue = TaskQueueManager()

    queue.add({"action": "HARVEST"})

    assert queue.size() == 1


def test_pop():

    queue = TaskQueueManager()

    queue.add({"action": "WATER"})

    task = queue.pop()

    assert task["action"] == "WATER"


def test_peek():

    queue = TaskQueueManager()

    queue.add({"action": "PLANT"})

    assert queue.peek()["action"] == "PLANT"


def test_empty():

    queue = TaskQueueManager()

    assert queue.empty()


def test_clear():

    queue = TaskQueueManager()

    queue.add({"action": "SELL"})
    queue.clear()

    assert queue.empty()


def test_fifo():

    queue = TaskQueueManager()

    queue.add({"id": 1})
    queue.add({"id": 2})

    assert queue.pop()["id"] == 1
    assert queue.pop()["id"] == 2