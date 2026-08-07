from src.task_scheduling_advisor import (
    TaskSchedulingAdvisor,
)


def test_schedule():

    advisor = TaskSchedulingAdvisor()

    tasks = [
        {
            "name": "Plant",
            "priority": 30,
            "urgency": 1,
        },
        {
            "name": "Harvest",
            "priority": 100,
            "urgency": 5,
        },
        {
            "name": "Water",
            "priority": 70,
            "urgency": 4,
        },
    ]

    ranked = advisor.schedule(tasks)

    assert ranked[0]["name"] == "Harvest"
    assert ranked[1]["name"] == "Water"
    assert ranked[2]["name"] == "Plant"


def test_next_task():

    advisor = TaskSchedulingAdvisor()

    task = advisor.next_task(
        [
            {
                "name": "Feed",
                "priority": 90,
                "urgency": 2,
            },
            {
                "name": "Move",
                "priority": 10,
                "urgency": 1,
            },
        ]
    )

    assert task["name"] == "Feed"


def test_empty():

    advisor = TaskSchedulingAdvisor()

    assert advisor.next_task([]) is None


def test_top_tasks():

    advisor = TaskSchedulingAdvisor()

    tasks = [
        {"name": "A", "priority": 1},
        {"name": "B", "priority": 5},
        {"name": "C", "priority": 3},
    ]

    result = advisor.top_tasks(
        tasks,
        limit=2,
    )

    assert len(result) == 2
    assert result[0]["name"] == "B"
    assert result[1]["name"] == "C"


def test_limit_larger_than_tasks():

    advisor = TaskSchedulingAdvisor()

    tasks = [
        {
            "name": "Harvest",
            "priority": 100,
        }
    ]

    result = advisor.top_tasks(
        tasks,
        limit=5,
    )

    assert len(result) == 1