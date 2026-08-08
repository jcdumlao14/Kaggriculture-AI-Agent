from src.resource_aware_task_scheduler import (
    ResourceAwareTaskScheduler,
)


def test_can_execute_water():

    scheduler = ResourceAwareTaskScheduler()

    assert scheduler.can_execute(
        task={"name": "WATER"},
        resources={"water": 2},
    )


def test_cannot_execute_water():

    scheduler = ResourceAwareTaskScheduler()

    assert not scheduler.can_execute(
        task={"name": "WATER"},
        resources={"water": 0},
    )


def test_feed_requires_wheat():

    scheduler = ResourceAwareTaskScheduler()

    assert scheduler.can_execute(
        task={"name": "FEED"},
        resources={"wheat": 1},
    )


def test_fertilize_requires_fertilizer():

    scheduler = ResourceAwareTaskScheduler()

    assert not scheduler.can_execute(
        task={"name": "FERTILIZE"},
        resources={"fertilizer": 0},
    )


def test_custom_requirements():

    scheduler = ResourceAwareTaskScheduler()

    task = {
        "name": "CUSTOM",
        "requirements": {
            "seeds": 3,
        },
    }

    assert scheduler.can_execute(
        task=task,
        resources={"seeds": 3},
    )


def test_filter_tasks():

    scheduler = ResourceAwareTaskScheduler()

    tasks = [
        {
            "name": "WATER",
            "priority": 50,
        },
        {
            "name": "FEED",
            "priority": 80,
        },
    ]

    result = scheduler.filter_tasks(
        tasks=tasks,
        resources={
            "water": 1,
            "wheat": 0,
        },
    )

    assert len(result) == 1
    assert result[0]["name"] == "WATER"


def test_schedule_priority():

    scheduler = ResourceAwareTaskScheduler()

    tasks = [
        {
            "name": "WATER",
            "priority": 50,
        },
        {
            "name": "FEED",
            "priority": 90,
        },
    ]

    result = scheduler.schedule(
        tasks=tasks,
        resources={
            "water": 1,
            "wheat": 1,
        },
    )

    assert result[0]["name"] == "FEED"


def test_next_task():

    scheduler = ResourceAwareTaskScheduler()

    task = scheduler.next_task(
        tasks=[
            {
                "name": "WATER",
                "priority": 50,
            },
            {
                "name": "FEED",
                "priority": 90,
            },
        ],
        resources={
            "water": 1,
            "wheat": 1,
        },
    )

    assert task["name"] == "FEED"


def test_no_executable_tasks():

    scheduler = ResourceAwareTaskScheduler()

    assert scheduler.next_task(
        tasks=[
            {
                "name": "WATER",
                "priority": 50,
            }
        ],
        resources={
            "water": 0,
        },
    ) is None