from src.reward_analyzer import RewardAnalyzer


def test_improving():

    analyzer = RewardAnalyzer([10, 20, 30])

    assert analyzer.improving()


def test_plateau():

    analyzer = RewardAnalyzer([15, 15, 15])

    assert analyzer.plateau()


def test_regression():

    analyzer = RewardAnalyzer([30, 20, 10])

    assert analyzer.regression()


def test_growth():

    analyzer = RewardAnalyzer([5, 10, 20])

    assert analyzer.growth() == 15


def test_best_jump():

    analyzer = RewardAnalyzer([10, 25, 30, 50])

    assert analyzer.best_jump() == 20