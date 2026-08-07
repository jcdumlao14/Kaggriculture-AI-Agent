from src.execution_plan_selector import (
    ExecutionPlanSelector,
)


def test_select():

    selector = ExecutionPlanSelector()

    plan = selector.select(
        [
            {
                "name": "A",
                "score": 10,
            },
            {
                "name": "B",
                "score": 30,
            },
            {
                "name": "C",
                "score": 20,
            },
        ]
    )

    assert plan["name"] == "B"


def test_rank():

    selector = ExecutionPlanSelector()

    ranked = selector.rank(
        [
            {
                "score": 5,
            },
            {
                "score": 25,
            },
            {
                "score": 10,
            },
        ]
    )

    assert ranked[0]["score"] == 25
    assert ranked[1]["score"] == 10
    assert ranked[2]["score"] == 5


def test_top_n():

    selector = ExecutionPlanSelector()

    plans = selector.top_n(
        [
            {"score": 10},
            {"score": 30},
            {"score": 20},
        ],
        limit=2,
    )

    assert len(plans) == 2
    assert plans[0]["score"] == 30
    assert plans[1]["score"] == 20


def test_empty():

    selector = ExecutionPlanSelector()

    assert selector.select([]) is None


def test_single():

    selector = ExecutionPlanSelector()

    plan = selector.select(
        [
            {
                "score": 50,
            }
        ]
    )

    assert plan["score"] == 50