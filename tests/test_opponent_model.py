from src.opponent_model import (
    OpponentModel,
)


def test_record():

    model = OpponentModel()

    model.record("HARVEST")

    assert model.frequency("HARVEST") == 1


def test_multiple_records():

    model = OpponentModel()

    model.record("SELL")
    model.record("SELL")
    model.record("PLANT")

    assert model.frequency("SELL") == 2


def test_most_common():

    model = OpponentModel()

    model.record("SELL")
    model.record("SELL")
    model.record("HARVEST")

    assert model.most_common() == "SELL"


def test_total():

    model = OpponentModel()

    model.record("PLANT")
    model.record("SELL")

    assert model.total_actions() == 2


def test_reset():

    model = OpponentModel()

    model.record("HARVEST")

    model.reset()

    assert model.total_actions() == 0