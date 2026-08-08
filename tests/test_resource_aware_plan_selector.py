from src.resource_aware_plan_selector import (
    ResourceAwarePlanSelector,
)


def test_score():

    selector = ResourceAwarePlanSelector()

    result = selector.score(
        plan=[
            {
                "priority": 100,
                "requirements": {},
            }
        ]
    )

    assert result == 100.0


def test_acceptable():

    selector = ResourceAwarePlanSelector(
        minimum_score=50,
    )

    assert selector.is_acceptable(
        plan=[
            {
                "priority": 100,
                "requirements": {},
            }
        ]
    )


def test_not_acceptable():

    selector = ResourceAwarePlanSelector(
        minimum_score=100,
    )

    assert not selector.is_acceptable(
        plan=[
            {
                "priority": 50,
                "requirements": {},
            }
        ]
    )


def test_select_best():

    selector = ResourceAwarePlanSelector(
        minimum_score=0,
    )

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

    result = selector.select(
        plans=[low, high],
    )

    assert result == high


def test_select_respects_minimum_score():

    selector = ResourceAwarePlanSelector(
        minimum_score=80,
    )

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

    result = selector.select(
        plans=[low, high],
    )

    assert result == high


def test_select_no_acceptable_plan():

    selector = ResourceAwarePlanSelector(
        minimum_score=200,
    )

    plans = [
        [
            {
                "priority": 100,
                "requirements": {},
            }
        ]
    ]

    assert selector.select(
        plans=plans,
    ) == []


def test_select_with_score():

    selector = ResourceAwarePlanSelector()

    plan = [
        {
            "priority": 75,
            "requirements": {},
        }
    ]

    result, score = selector.select_with_score(
        plans=[plan],
    )

    assert result == plan
    assert score == 75.0


def test_select_with_score_empty():

    selector = ResourceAwarePlanSelector(
        minimum_score=100,
    )

    plan = [
        {
            "priority": 50,
            "requirements": {},
        }
    ]

    result, score = selector.select_with_score(
        plans=[plan],
    )

    assert result == []
    assert score == 0.0


def test_accepted_plans():

    selector = ResourceAwarePlanSelector(
        minimum_score=50,
    )

    plans = [
        [
            {
                "priority": 20,
                "requirements": {},
            }
        ],
        [
            {
                "priority": 80,
                "requirements": {},
            }
        ],
    ]

    result = selector.accepted_plans(
        plans=plans,
    )

    assert result == [plans[1]]