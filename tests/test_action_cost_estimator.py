from src.action_cost_estimator import (
    ActionCostEstimator,
)


def test_estimate():

    estimator = ActionCostEstimator()

    cost = estimator.estimate(
        money=10,
        energy=5,
        time=4,
    )

    assert cost == 22.0


def test_affordable():

    estimator = ActionCostEstimator()

    assert estimator.affordable(
        available_money=100,
        estimated_cost=50,
    )


def test_not_affordable():

    estimator = ActionCostEstimator()

    assert not estimator.affordable(
        available_money=20,
        estimated_cost=30,
    )


def test_efficiency():

    estimator = ActionCostEstimator()

    score = estimator.efficiency(
        reward=100,
        cost=20,
    )

    assert score == 5.0


def test_zero_cost():

    estimator = ActionCostEstimator()

    score = estimator.efficiency(
        reward=15,
        cost=0,
    )

    assert score == 15