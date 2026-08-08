from src.resource_aware_execution_history import (
    ResourceAwareExecutionHistory,
)


def test_initial_history_is_empty():

    history = ResourceAwareExecutionHistory()

    assert history.all() == []
    assert history.count() == 0


def test_record():

    history = ResourceAwareExecutionHistory()

    result = {
        "success": True,
        "executed": True,
    }

    recorded = history.record(
        result=result,
    )

    assert recorded == result
    assert history.count() == 1


def test_all():

    history = ResourceAwareExecutionHistory()

    first = {
        "success": True,
    }

    second = {
        "success": False,
    }

    history.record(result=first)
    history.record(result=second)

    assert history.all() == [
        first,
        second,
    ]


def test_latest():

    history = ResourceAwareExecutionHistory()

    first = {
        "success": True,
    }

    second = {
        "success": False,
    }

    history.record(result=first)
    history.record(result=second)

    assert history.latest() == second


def test_latest_empty():

    history = ResourceAwareExecutionHistory()

    assert history.latest() is None


def test_successful():

    history = ResourceAwareExecutionHistory()

    success = {
        "success": True,
    }

    failure = {
        "success": False,
    }

    history.record(result=success)
    history.record(result=failure)

    assert history.successful() == [
        success,
    ]


def test_failed():

    history = ResourceAwareExecutionHistory()

    success = {
        "success": True,
    }

    failure = {
        "success": False,
    }

    history.record(result=success)
    history.record(result=failure)

    assert history.failed() == [
        failure,
    ]


def test_clear():

    history = ResourceAwareExecutionHistory()

    history.record(
        result={
            "success": True,
        }
    )

    history.clear()

    assert history.count() == 0
    assert history.all() == []


def test_success_rate():

    history = ResourceAwareExecutionHistory()

    history.record(
        result={"success": True}
    )

    history.record(
        result={"success": True}
    )

    history.record(
        result={"success": False}
    )

    assert history.success_rate() == 2 / 3


def test_empty_success_rate():

    history = ResourceAwareExecutionHistory()

    assert history.success_rate() == 0.0