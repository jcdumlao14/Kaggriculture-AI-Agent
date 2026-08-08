from src.resource_aware_plan_comparator import (
    ResourceAwarePlanComparator,
)


def test_score():

    comparator = ResourceAwarePlanComparator()

    result = comparator.score(
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


def test_compare_first_better():

    comparator = ResourceAwarePlanComparator()

    first = [
        {
            "priority": 100,
            "requirements": {},
        }
    ]

    second = [
        {
            "priority": 50,
            "requirements": {},
        }
    ]

    assert comparator.compare(
        first=first,
        second=second,
    ) == 1


def test_compare_second_better():

    comparator = ResourceAwarePlanComparator()

    first = [
        {
            "priority": 40,
            "requirements": {},
        }
    ]

    second = [
        {
            "priority": 80,
            "requirements": {},
        }
    ]

    assert comparator.compare(
        first=first,
        second=second,
    ) == -1


def test_compare_equal():

    comparator = ResourceAwarePlanComparator()

    plan = [
        {
            "priority": 50,
            "requirements": {},
        }
    ]

    assert comparator.compare(
        first=plan,
        second=plan,
    ) == 0


def test_rank():

    comparator = ResourceAwarePlanComparator()

    low = [
        {
            "priority": 20,
            "requirements": {},
        }
    ]

    high = [
        {
            "priority": 100,
            "requirements": {},
        }
    ]

    result = comparator.rank(
        plans=[low, high],
    )

    assert result[0] == high
    assert result[1] == low


def test_best():

    comparator = ResourceAwarePlanComparator()

    first = [
        {
            "priority": 100,
            "requirements": {},
        }
    ]

    second = [
        {
            "priority": 20,
            "requirements": {},
        }
    ]

    assert comparator.best(
        plans=[first, second],
    ) == first


def test_empty_best():

    comparator = ResourceAwarePlanComparator()

    assert comparator.best(
        plans=[]
    ) == []


def test_scores():

    comparator = ResourceAwarePlanComparator()

    plans = [
        [
            {
                "priority": 100,
                "requirements": {},
            }
        ],
        [
            {
                "priority": 50,
                "requirements": {},
            }
        ],
    ]

    assert comparator.scores(
        plans=plans,
    ) == [100.0, 50.0]