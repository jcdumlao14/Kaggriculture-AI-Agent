from src.resource_aware_plan_validator import (
    ResourceAwarePlanValidator,
)


def test_valid_task():

    validator = ResourceAwarePlanValidator()

    assert validator.is_valid_task(
        task={
            "name": "WATER",
            "requirements": {
                "water": 1,
            },
        }
    )


def test_empty_task_invalid():

    validator = ResourceAwarePlanValidator()

    assert not validator.is_valid_task(
        task={}
    )


def test_non_dict_task_invalid():

    validator = ResourceAwarePlanValidator()

    assert not validator.is_valid_task(
        task="WATER"
    )


def test_negative_requirement_invalid():

    validator = ResourceAwarePlanValidator()

    assert not validator.is_valid_task(
        task={
            "name": "WATER",
            "requirements": {
                "water": -1,
            },
        }
    )


def test_invalid_requirement_type():

    validator = ResourceAwarePlanValidator()

    assert not validator.is_valid_task(
        task={
            "name": "WATER",
            "requirements": {
                "water": "one",
            },
        }
    )


def test_invalid_requirements_container():

    validator = ResourceAwarePlanValidator()

    assert not validator.is_valid_task(
        task={
            "name": "WATER",
            "requirements": [],
        }
    )


def test_validate_plan():

    validator = ResourceAwarePlanValidator()

    assert validator.validate(
        plan=[
            {
                "name": "WATER",
                "requirements": {
                    "water": 1,
                },
            },
            {
                "name": "FEED",
                "requirements": {
                    "wheat": 1,
                },
            },
        ]
    )


def test_validate_invalid_plan():

    validator = ResourceAwarePlanValidator()

    assert not validator.validate(
        plan=[
            {
                "name": "WATER",
                "requirements": {
                    "water": -1,
                },
            }
        ]
    )


def test_invalid_tasks():

    validator = ResourceAwarePlanValidator()

    invalid = {
        "name": "WATER",
        "requirements": {
            "water": -1,
        },
    }

    result = validator.invalid_tasks(
        plan=[
            {
                "name": "FEED",
                "requirements": {
                    "wheat": 1,
                },
            },
            invalid,
        ]
    )

    assert result == [invalid]


def test_task_count():

    validator = ResourceAwarePlanValidator()

    assert validator.task_count(
        plan=[
            {"name": "A"},
            {"name": "B"},
        ]
    ) == 2


def test_has_tasks():

    validator = ResourceAwarePlanValidator()

    assert validator.has_tasks(
        plan=[
            {"name": "A"},
        ]
    )


def test_empty_plan():

    validator = ResourceAwarePlanValidator()

    assert validator.validate(
        plan=[]
    )


def test_empty_plan_has_no_tasks():

    validator = ResourceAwarePlanValidator()

    assert not validator.has_tasks(
        plan=[]
    )