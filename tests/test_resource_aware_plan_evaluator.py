from src.resource_aware_plan_evaluator import (
    ResourceAwarePlanEvaluator,
)


def test_total_priority():

    evaluator = ResourceAwarePlanEvaluator()

    result = evaluator.total_priority(
        plan=[
            {"priority": 100},
            {"priority": 50},
        ]
    )

    assert result == 150


def test_empty_priority():

    evaluator = ResourceAwarePlanEvaluator()

    assert evaluator.total_priority(
        plan=[]
    ) == 0


def test_resource_cost():

    evaluator = ResourceAwarePlanEvaluator()

    result = evaluator.resource_cost(
        plan=[
            {
                "requirements": {
                    "water": 2,
                    "wheat": 1,
                }
            }
        ]
    )

    assert result == 3


def test_empty_resource_cost():

    evaluator = ResourceAwarePlanEvaluator()

    assert evaluator.resource_cost(
        plan=[]
    ) == 0


def test_evaluate():

    evaluator = ResourceAwarePlanEvaluator()

    result = evaluator.evaluate(
        plan=[
            {
                "priority": 100,
                "requirements": {
                    "water": 2,
                },
            }
        ]
    )

    assert result == 98


def test_is_better():

    evaluator = ResourceAwarePlanEvaluator()

    first = [
        {
            "priority": 100,
            "requirements": {"water": 1},
        }
    ]

    second = [
        {
            "priority": 50,
            "requirements": {"water": 1},
        }
    ]

    assert evaluator.is_better(
        first=first,
        second=second,
    )


def test_best_plan():

    evaluator = ResourceAwarePlanEvaluator()

    plans = [
        [
            {
                "priority": 50,
                "requirements": {"water": 1},
            }
        ],
        [
            {
                "priority": 100,
                "requirements": {"water": 1},
            }
        ],
    ]

    result = evaluator.best_plan(
        plans=plans,
    )

    assert result == plans[1]


def test_best_plan_empty():

    evaluator = ResourceAwarePlanEvaluator()

    assert evaluator.best_plan(
        plans=[]
    ) == []