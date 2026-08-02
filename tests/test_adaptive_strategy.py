from src.learning import LearningModule
from src.adaptive_strategy import AdaptiveStrategy


def test_default():

    learning = LearningModule()

    adaptive = AdaptiveStrategy(learning)

    assert adaptive.choose() == "BALANCED"


def test_choose_best():

    learning = LearningModule()

    learning.record("SAFE", 120)
    learning.record("EXPANSION", 250)
    learning.record("BALANCED", 150)

    adaptive = AdaptiveStrategy(learning)

    assert adaptive.choose() == "EXPANSION"


def test_recommend():

    learning = LearningModule()

    learning.record("SAFE", 200)

    adaptive = AdaptiveStrategy(learning)

    assert adaptive.recommend() == "SAFE"


def test_confidence_zero():

    learning = LearningModule()

    adaptive = AdaptiveStrategy(learning)

    assert adaptive.confidence() == 0.0


def test_confidence_positive():

    learning = LearningModule()

    for _ in range(10):
        learning.record("BALANCED", 100)

    adaptive = AdaptiveStrategy(learning)

    assert adaptive.confidence() > 0