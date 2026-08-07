from src.state_encoding_engine import (
    StateEncodingEngine,
)


def test_encode():

    engine = StateEncodingEngine()

    encoded = engine.encode(
        {"money": 100}
    )

    assert isinstance(encoded, str)


def test_hash():

    engine = StateEncodingEngine()

    value = engine.hash(
        {"money": 100}
    )

    assert len(value) == 64


def test_identical():

    engine = StateEncodingEngine()

    assert engine.identical(
        {"a": 1},
        {"a": 1},
    )


def test_different():

    engine = StateEncodingEngine()

    assert not engine.identical(
        {"a": 1},
        {"a": 2},
    )


def test_sorted_keys():

    engine = StateEncodingEngine()

    first = engine.hash(
        {"a": 1, "b": 2}
    )

    second = engine.hash(
        {"b": 2, "a": 1}
    )

    assert first == second