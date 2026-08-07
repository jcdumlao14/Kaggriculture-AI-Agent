from src.expected_reward_estimator import (
    ExpectedRewardEstimator,
)


def test_expected_reward():

    estimator = ExpectedRewardEstimator()

    result = estimator.expected_reward(
        reward=100,
        probability=0.5,
    )

    assert result == 50.0


def test_probability_clamped():

    estimator = ExpectedRewardEstimator()

    result = estimator.expected_reward(
        reward=80,
        probability=2.0,
    )

    assert result == 80.0


def test_expected_utility():

    estimator = ExpectedRewardEstimator()

    utility = estimator.expected_utility(
        reward=100,
        probability=0.8,
        cost=20,
    )

    assert utility == 60.0


def test_worthwhile():

    estimator = ExpectedRewardEstimator()

    assert estimator.worthwhile(
        reward=100,
        probability=0.8,
        cost=30,
    )


def test_not_worthwhile():

    estimator = ExpectedRewardEstimator()

    assert not estimator.worthwhile(
        reward=20,
        probability=0.5,
        cost=20,
    )