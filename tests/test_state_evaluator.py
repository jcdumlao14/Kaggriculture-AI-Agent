from src.state_evaluator import StateEvaluator


def test_evaluate_returns_number():

    evaluator = StateEvaluator()

    score = evaluator.evaluate(
        money=3000,
        crops=8,
        animals=2,
        inventory=10,
    )

    assert isinstance(score, (int, float))


def test_better():

    evaluator = StateEvaluator()

    assert evaluator.better(200, 150)


def test_difference():

    evaluator = StateEvaluator()

    assert evaluator.difference(200, 150) == 50


def test_zero_state():

    evaluator = StateEvaluator()

    assert evaluator.evaluate(0, 0, 0, 0) == 0


def test_money_increases_score():

    evaluator = StateEvaluator()

    low = evaluator.evaluate(1000, 2, 1, 5)
    high = evaluator.evaluate(3000, 2, 1, 5)

    assert high > low