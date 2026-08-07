from src.execution_plan_evaluator import (
    ExecutionPlanEvaluator,
)


def test_score():

    evaluator = ExecutionPlanEvaluator()

    assert evaluator.score(
        reward=120,
        cost=40,
    ) == 80


def test_efficiency():

    evaluator = ExecutionPlanEvaluator()

    assert evaluator.efficiency(
        reward=120,
        cost=40,
    ) == 3.0


def test_zero_cost():

    evaluator = ExecutionPlanEvaluator()

    assert evaluator.efficiency(
        reward=50,
        cost=0,
    ) == 50


def test_worthwhile():

    evaluator = ExecutionPlanEvaluator()

    assert evaluator.worthwhile(
        reward=100,
        cost=20,
    )


def test_not_worthwhile():

    evaluator = ExecutionPlanEvaluator()

    assert not evaluator.worthwhile(
        reward=20,
        cost=40,
    )