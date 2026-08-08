from src.task_conflict_resolver import (
    TaskConflictResolver,
)


def test_resolve():

    resolver = TaskConflictResolver()

    result = resolver.resolve(
        assignments={
            "farmer": [
                {
                    "name": "Harvest",
                    "priority": 100,
                },
                {
                    "name": "Water",
                    "priority": 50,
                },
            ]
        }
    )

    assert result["farmer"]["name"] == "Harvest"


def test_highest_priority():

    resolver = TaskConflictResolver()

    result = resolver.resolve(
        assignments={
            "worker1": [
                {
                    "name": "Feed",
                    "priority": 30,
                },
                {
                    "name": "Harvest",
                    "priority": 90,
                },
                {
                    "name": "Water",
                    "priority": 60,
                },
            ]
        }
    )

    assert result["worker1"]["name"] == "Harvest"


def test_conflicts():

    resolver = TaskConflictResolver()

    result = resolver.conflicts(
        assignments={
            "farmer": [
                {"name": "Harvest"},
                {"name": "Water"},
            ],
            "worker1": [
                {"name": "Feed"},
            ],
        }
    )

    assert "farmer" in result
    assert "worker1" not in result


def test_has_conflicts():

    resolver = TaskConflictResolver()

    assert resolver.has_conflicts(
        assignments={
            "farmer": [
                {"name": "Harvest"},
                {"name": "Water"},
            ]
        }
    )


def test_no_conflicts():

    resolver = TaskConflictResolver()

    assert not resolver.has_conflicts(
        assignments={
            "farmer": [
                {"name": "Harvest"},
            ]
        }
    )


def test_empty():

    resolver = TaskConflictResolver()

    assert resolver.resolve(
        assignments={}
    ) == {}