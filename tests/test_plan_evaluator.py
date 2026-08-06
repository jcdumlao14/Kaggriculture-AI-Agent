from src.plan_evaluator import PlanEvaluator


def plan_a():

    return [
        {"action": "HARVEST"},
        {"action": "SELL"},
    ]


def plan_b():

    return [
        {"action": "PLANT"},
        {"action": "WATER"},
    ]


def test_evaluate():

    evaluator = PlanEvaluator()

    score = evaluator.evaluate(
        plan_a(),
    )

    assert isinstance(score, float)


def test_better_plan():

    evaluator = PlanEvaluator()

    best = evaluator.better_plan(
        plan_a(),
        plan_b(),
    )

    assert best == plan_a()


def test_average_score():

    evaluator = PlanEvaluator()

    average = evaluator.average_score(
        plan_a(),
    )

    assert isinstance(average, float)


def test_empty():

    evaluator = PlanEvaluator()

    assert evaluator.is_empty([])


def test_not_empty():

    evaluator = PlanEvaluator()

    assert not evaluator.is_empty(
        plan_a(),
    )