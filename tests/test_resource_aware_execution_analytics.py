from src.resource_aware_execution_analytics import (
    ResourceAwareExecutionAnalytics,
)


def test_success_count():

    analytics = (
        ResourceAwareExecutionAnalytics()
    )

    results = [
        {"success": True},
        {"success": False},
        {"success": True},
    ]

    assert analytics.success_count(
        results=results,
    ) == 2


def test_failure_count():

    analytics = (
        ResourceAwareExecutionAnalytics()
    )

    results = [
        {"success": True},
        {"success": False},
        {"success": False},
    ]

    assert analytics.failure_count(
        results=results,
    ) == 2


def test_success_rate():

    analytics = (
        ResourceAwareExecutionAnalytics()
    )

    results = [
        {"success": True},
        {"success": True},
        {"success": False},
        {"success": False},
    ]

    assert analytics.success_rate(
        results=results,
    ) == 0.5


def test_empty_success_rate():

    analytics = (
        ResourceAwareExecutionAnalytics()
    )

    assert analytics.success_rate(
        results=[],
    ) == 0.0


def test_average_task_count():

    analytics = (
        ResourceAwareExecutionAnalytics()
    )

    results = [
        {
            "plan": [
                {"name": "A"},
                {"name": "B"},
            ]
        },
        {
            "plan": [
                {"name": "C"},
                {"name": "D"},
                {"name": "E"},
                {"name": "F"},
            ]
        },
    ]

    assert analytics.average_task_count(
        results=results,
    ) == 3.0


def test_empty_average_task_count():

    analytics = (
        ResourceAwareExecutionAnalytics()
    )

    assert analytics.average_task_count(
        results=[],
    ) == 0.0


def test_total_tasks():

    analytics = (
        ResourceAwareExecutionAnalytics()
    )

    results = [
        {
            "plan": [
                {"name": "A"},
            ]
        },
        {
            "plan": [
                {"name": "B"},
                {"name": "C"},
            ]
        },
    ]

    assert analytics.total_tasks(
        results=results,
    ) == 3


def test_resource_consumption():

    analytics = (
        ResourceAwareExecutionAnalytics()
    )

    results = [
        {
            "resources": {
                "water": 5,
            },
            "remaining": {
                "water": 3,
            },
        },
        {
            "resources": {
                "water": 3,
                "wheat": 4,
            },
            "remaining": {
                "water": 2,
                "wheat": 2,
            },
        },
    ]

    assert analytics.resource_consumption(
        results=results,
    ) == {
        "water": 3,
        "wheat": 2,
    }


def test_rejection_reasons():

    analytics = (
        ResourceAwareExecutionAnalytics()
    )

    results = [
        {
            "success": False,
            "reason": "insufficient_resources",
        },
        {
            "success": False,
            "reason": "insufficient_resources",
        },
        {
            "success": False,
            "reason": "invalid_plan",
        },
        {
            "success": True,
            "reason": None,
        },
    ]

    assert analytics.rejection_reasons(
        results=results,
    ) == {
        "insufficient_resources": 2,
        "invalid_plan": 1,
    }


def test_successful_results_have_no_rejection_reason():

    analytics = (
        ResourceAwareExecutionAnalytics()
    )

    results = [
        {
            "success": True,
            "reason": "ignored",
        }
    ]

    assert analytics.rejection_reasons(
        results=results,
    ) == {}


def test_build():

    analytics = (
        ResourceAwareExecutionAnalytics()
    )

    results = [
        {
            "success": True,
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
        },
        {
            "success": False,
            "plan": [
                {"name": "FEED"},
                {"name": "HARVEST"},
            ],
            "resources": {
                "water": 1,
            },
            "remaining": {
                "water": 1,
            },
            "reason": "insufficient_resources",
        },
    ]

    output = analytics.build(
        results=results,
    )

    assert output == {
        "total_results": 2,
        "success_count": 1,
        "failure_count": 1,
        "success_rate": 0.5,
        "total_tasks": 3,
        "average_task_count": 1.5,
        "resource_consumption": {
            "water": 1,
        },
        "rejection_reasons": {
            "insufficient_resources": 1,
        },
    }