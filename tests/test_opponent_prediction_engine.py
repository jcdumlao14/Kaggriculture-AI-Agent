from src.opponent_model import (
    OpponentModel,
)

from src.opponent_prediction_engine import (
    OpponentPredictionEngine,
)


def test_prediction():

    model = OpponentModel()

    model.record("SELL")
    model.record("SELL")
    model.record("PLANT")

    engine = OpponentPredictionEngine(
        model,
    )

    assert engine.predict() == "SELL"


def test_confidence():

    model = OpponentModel()

    model.record("SELL")
    model.record("SELL")
    model.record("PLANT")

    engine = OpponentPredictionEngine(
        model,
    )

    assert (
        engine.confidence()
        == 2 / 3
    )


def test_empty():

    model = OpponentModel()

    engine = OpponentPredictionEngine(
        model,
    )

    assert engine.predict() is None


def test_has_prediction():

    model = OpponentModel()

    model.record("HARVEST")

    engine = OpponentPredictionEngine(
        model,
    )

    assert engine.has_prediction()


def test_no_prediction():

    model = OpponentModel()

    engine = OpponentPredictionEngine(
        model,
    )

    assert not engine.has_prediction()