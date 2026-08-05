from src.task_scheduler import TaskScheduler


def test_add_task():

    scheduler = TaskScheduler()

    scheduler.add_task(lambda: 10)

    assert scheduler.pending_tasks() == 1


def test_run_next():

    scheduler = TaskScheduler()

    scheduler.add_task(lambda: 42)

    assert scheduler.run_next() == 42


def test_fifo_order():

    scheduler = TaskScheduler()

    scheduler.add_task(lambda: 1)
    scheduler.add_task(lambda: 2)

    assert scheduler.run_next() == 1
    assert scheduler.run_next() == 2


def test_clear():

    scheduler = TaskScheduler()

    scheduler.add_task(lambda: 1)

    scheduler.clear()

    assert scheduler.pending_tasks() == 0


def test_has_tasks():

    scheduler = TaskScheduler()

    assert not scheduler.has_tasks()

    scheduler.add_task(lambda: None)

    assert scheduler.has_tasks()

def test_peek():

    scheduler = TaskScheduler()

    scheduler.add_task(lambda: 99)

    task = scheduler.peek()

    assert callable(task)
    assert scheduler.pending_tasks() == 1


def test_run_all():

    scheduler = TaskScheduler()

    scheduler.add_task(lambda: 1)
    scheduler.add_task(lambda: 2)
    scheduler.add_task(lambda: 3)

    assert scheduler.run_all() == [1, 2, 3]
    assert scheduler.pending_tasks() == 0