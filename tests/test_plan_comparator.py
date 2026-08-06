from src.plan_comparator import PlanComparator


def plans():

    return [
        [
            {"action": "PLANT"},
            {"action": "WATER"},
        ],
        [
            {"action": "HARVEST"},
            {"action": "SELL"},
        ],
    ]


def test_best_plan():

    comparator = PlanComparator()

    best = comparator.best_plan(
        plans(),
    )

    assert isinstance(best, list)


def test_rank():

    comparator = PlanComparator()

    ranked = comparator.rank_plans(
        plans(),
    )

    assert len(ranked) == 2


def test_best_score():

    comparator = PlanComparator()

    score = comparator.best_score(
        plans(),
    )

    assert isinstance(score, float)


def test_has_plans():

    comparator = PlanComparator()

    assert comparator.has_plans(
        plans(),
    )


def test_empty():

    comparator = PlanComparator()

    assert not comparator.has_plans([])