from src.action_utility_engine import (
    ActionUtilityEngine,
)


def test_utility():

    engine = ActionUtilityEngine()

    score = engine.utility(
        reward=100,
        probability=0.8,
        money_cost=10,
        energy_cost=5,
        time_cost=4,
    )

    assert score == 58.0


def test_worthwhile():

    engine = ActionUtilityEngine()

    assert engine.worthwhile(
        reward=100,
        probability=0.8,
        money_cost=10,
    )


def test_not_worthwhile():

    engine = ActionUtilityEngine()

    assert not engine.worthwhile(
        reward=10,
        probability=0.5,
        money_cost=20,
    )


def test_zero_cost():

    engine = ActionUtilityEngine()

    score = engine.utility(
        reward=50,
        probability=1.0,
    )

    assert score == 50.0


def test_zero_probability():

    engine = ActionUtilityEngine()

    score = engine.utility(
        reward=100,
        probability=0.0,
        money_cost=5,
    )

    assert score == -5.0