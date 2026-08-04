from src.priority_task_scheduler import PriorityTaskScheduler


def test_add_task():

    scheduler = PriorityTaskScheduler()

    scheduler.add_task(lambda: 1)

    assert scheduler.pending_tasks() == 1


def test_priority_execution():

    scheduler = PriorityTaskScheduler()

    scheduler.add_task(lambda: "low", priority=5)
    scheduler.add_task(lambda: "high", priority=1)

    assert scheduler.run_next() == "high"


def test_fifo_same_priority():

    scheduler = PriorityTaskScheduler()

    scheduler.add_task(lambda: 1, priority=2)
    scheduler.add_task(lambda: 2, priority=2)

    assert scheduler.run_next() == 1
    assert scheduler.run_next() == 2


def test_clear():

    scheduler = PriorityTaskScheduler()

    scheduler.add_task(lambda: None)

    scheduler.clear()

    assert scheduler.pending_tasks() == 0


def test_has_tasks():

    scheduler = PriorityTaskScheduler()

    assert not scheduler.has_tasks()

    scheduler.add_task(lambda: 5)

    assert scheduler.has_tasks()