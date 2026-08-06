from src.opponent_decision_adapter import (
    OpponentDecisionAdapter,
)


def test_unknown():

    adapter = OpponentDecisionAdapter()

    assert (
        adapter.adjustment(
            "UNKNOWN",
        )
        == 0
    )


def test_economic():

    adapter = OpponentDecisionAdapter()

    assert (
        adapter.adjustment(
            "ECONOMIC",
        )
        == 15
    )


def test_aggressive():

    adapter = OpponentDecisionAdapter()

    assert (
        adapter.adjustment(
            "AGGRESSIVE",
        )
        == 20
    )


def test_apply():

    adapter = OpponentDecisionAdapter()

    assert (
        adapter.apply(
            100,
            "ECONOMIC",
        )
        == 115
    )


def test_supported():

    adapter = OpponentDecisionAdapter()

    assert (
        "BALANCED"
        in adapter.supported()
    )