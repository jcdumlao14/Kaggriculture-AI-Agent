from src.resource_aware_execution_history_manager import (
    ResourceAwareExecutionHistoryManager,
)


def test_initial_manager():

    manager = (
        ResourceAwareExecutionHistoryManager()
    )

    assert manager.count() == 0
    assert manager.get_all() == []


def test_record():

    manager = (
        ResourceAwareExecutionHistoryManager()
    )

    result = {
        "success": True,
    }

    assert manager.record(
        result=result,
    ) == result

    assert manager.count() == 1


def test_get_all():

    manager = (
        ResourceAwareExecutionHistoryManager()
    )

    first = {
        "success": True,
    }

    second = {
        "success": False,
    }

    manager.record(result=first)
    manager.record(result=second)

    assert manager.get_all() == [
        first,
        second,
    ]


def test_latest():

    manager = (
        ResourceAwareExecutionHistoryManager()
    )

    first = {
        "success": True,
    }

    second = {
        "success": False,
    }

    manager.record(result=first)
    manager.record(result=second)

    assert manager.latest() == second


def test_successful():

    manager = (
        ResourceAwareExecutionHistoryManager()
    )

    success = {
        "success": True,
    }

    failure = {
        "success": False,
    }

    manager.record(result=success)
    manager.record(result=failure)

    assert manager.successful() == [
        success,
    ]


def test_failed():

    manager = (
        ResourceAwareExecutionHistoryManager()
    )

    success = {
        "success": True,
    }

    failure = {
        "success": False,
    }

    manager.record(result=success)
    manager.record(result=failure)

    assert manager.failed() == [
        failure,
    ]


def test_success_rate():

    manager = (
        ResourceAwareExecutionHistoryManager()
    )

    manager.record(
        result={"success": True}
    )

    manager.record(
        result={"success": False}
    )

    assert manager.success_rate() == 0.5


def test_recent():

    manager = (
        ResourceAwareExecutionHistoryManager()
    )

    first = {"id": 1}
    second = {"id": 2}
    third = {"id": 3}

    manager.record(result=first)
    manager.record(result=second)
    manager.record(result=third)

    assert manager.recent(
        limit=2,
    ) == [
        second,
        third,
    ]


def test_recent_limit_larger_than_history():

    manager = (
        ResourceAwareExecutionHistoryManager()
    )

    first = {"id": 1}

    manager.record(result=first)

    assert manager.recent(
        limit=10,
    ) == [first]


def test_recent_zero():

    manager = (
        ResourceAwareExecutionHistoryManager()
    )

    manager.record(
        result={"id": 1}
    )

    assert manager.recent(
        limit=0,
    ) == []


def test_recent_negative():

    manager = (
        ResourceAwareExecutionHistoryManager()
    )

    manager.record(
        result={"id": 1}
    )

    assert manager.recent(
        limit=-1,
    ) == []


def test_clear():

    manager = (
        ResourceAwareExecutionHistoryManager()
    )

    manager.record(
        result={"success": True}
    )

    manager.clear()

    assert manager.count() == 0
    assert manager.latest() is None