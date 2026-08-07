from src.execution_plan_validator import (
    ExecutionPlanValidator,
)


def test_validate():

    validator = ExecutionPlanValidator()

    plan = [
        {
            "worker": "farmer",
            "task": "Harvest",
        },
        {
            "worker": "worker1",
            "task": "Water",
        },
    ]

    assert validator.validate(
        plan=plan,
    )


def test_invalid():

    validator = ExecutionPlanValidator()

    plan = [
        {
            "worker": "farmer",
        }
    ]

    assert not validator.validate(
        plan=plan,
    )


def test_invalid_steps():

    validator = ExecutionPlanValidator()

    plan = [
        {
            "worker": "farmer",
            "task": "Harvest",
        },
        {
            "worker": "worker1",
        },
    ]

    invalid = validator.invalid_steps(
        plan=plan,
    )

    assert len(invalid) == 1


def test_executable():

    validator = ExecutionPlanValidator()

    assert validator.executable(
        plan=[
            {
                "worker": "farmer",
                "task": "Harvest",
            }
        ],
    )


def test_empty():

    validator = ExecutionPlanValidator()

    assert not validator.executable(
        plan=[],
    )