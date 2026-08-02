from src.learning import LearningModule


def test_record():

    learning = LearningModule()

    learning.record("BALANCED", 120)

    assert learning.total_games() == 1


def test_average():

    learning = LearningModule()

    learning.record("BALANCED", 100)
    learning.record("BALANCED", 200)

    assert learning.average_reward("BALANCED") == 150


def test_best_strategy():

    learning = LearningModule()

    learning.record("SAFE", 120)
    learning.record("EXPANSION", 300)
    learning.record("BALANCED", 200)

    assert learning.best_strategy() == "EXPANSION"


def test_reset():

    learning = LearningModule()

    learning.record("SAFE", 100)

    learning.reset()

    assert learning.total_games() == 0


def test_empty():

    learning = LearningModule()

    assert learning.best_strategy() is None