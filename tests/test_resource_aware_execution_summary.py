from src.resource_aware_execution_summary import (
    ResourceAwareExecutionSummary,
)


def test_task_count():

    summary = ResourceAwareExecutionSummary()

    result = {
        "plan": [
            {"name": "WATER"},
            {"name": "FEED"},
        ]
    }

    assert summary.task_count(
        result=result,
    ) == 2


def test_empty_task_count():

    summary = ResourceAwareExecutionSummary()

    assert summary.task_count(
        result={}
    ) == 0


def test_resource_change():

    summary = ResourceAwareExecutionSummary()

    result = {
        "resources": {
            "water": 5,
            "wheat": 3,
        },
        "remaining": {
            "water": 3,
            "wheat": 2,
        },
    }

    assert summary.resource_change(
        result=result,
    ) == {
        "water": 2,
        "wheat": 1,
    }


def test_resource_change_new_remaining_resource():

    summary = ResourceAwareExecutionSummary()

    result = {
        "resources": {
            "water": 5,
        },
        "remaining": {
            "water": 3,
            "wheat": 2,
        },
    }

    assert summary.resource_change(
        result=result,
    ) == {
        "water": 2,
        "wheat": -2,
    }


def test_success():

    summary = ResourceAwareExecutionSummary()

    assert summary.success(
        result={
            "success": True,
        }
    )


def test_failure():

    summary = ResourceAwareExecutionSummary()

    assert not summary.success(
        result={
            "success": False,
        }
    )


def test_reason():

    summary = ResourceAwareExecutionSummary()

    assert summary.reason(
        result={
            "reason": "insufficient_resources",
        }
    ) == "insufficient_resources"


def test_build():

    summary = ResourceAwareExecutionSummary()

    result = {
        "success": True,
        "executed": True,
        "plan": [
            {"name": "WATER"},
        ],
        "resources": {
            "water": 5,
        },
        "remaining": {
            "water": 4,
        },
        "reason": None,
    }

    output = summary.build(
        result=result,
    )

    assert output == {
        "success": True,
        "executed": True,
        "task_count": 1,
        "resource_change": {
            "water": 1,
        },
        "reason": None,
    }


def test_build_failure():

    summary = ResourceAwareExecutionSummary()

    result = {
        "success": False,
        "executed": False,
        "plan": [],
        "resources": {
            "water": 0,
        },
        "remaining": {
            "water": 0,
        },
        "reason": "insufficient_resources",
    }

    output = summary.build(
        result=result,
    )

    assert output["success"] is False
    assert output["executed"] is False
    assert output["task_count"] == 0
    assert output["reason"] == (
        "insufficient_resources"
    )


def test_non_list_plan():

    summary = ResourceAwareExecutionSummary()

    assert summary.task_count(
        result={
            "plan": None,
        }
    ) == 0