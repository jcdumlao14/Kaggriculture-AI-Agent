from src.decision_confidence_engine import (
    DecisionConfidenceEngine,
)


def test_empty():

    engine = DecisionConfidenceEngine()

    assert (
        engine.confidence([])
        == 0.0
    )


def test_single():

    engine = DecisionConfidenceEngine()

    assert (
        engine.confidence([10.0])
        == 1.0
    )


def test_gap():

    engine = DecisionConfidenceEngine()

    confidence = engine.confidence(
        [100.0, 60.0],
    )

    assert confidence == 0.4


def test_confident():

    engine = DecisionConfidenceEngine()

    assert engine.confident(
        [100.0, 20.0],
    )


def test_not_confident():

    engine = DecisionConfidenceEngine()

    assert not engine.confident(
        [100.0, 95.0],
    )