from src.action_history_analyzer import (
    ActionHistoryAnalyzer,
)


def test_record():

    analyzer = ActionHistoryAnalyzer()

    analyzer.record(
        "HARVEST",
    )

    assert (
        analyzer.total_actions()
        == 1
    )


def test_count():

    analyzer = ActionHistoryAnalyzer()

    analyzer.record("SELL")
    analyzer.record("SELL")
    analyzer.record("HARVEST")

    assert (
        analyzer.count("SELL")
        == 2
    )


def test_most_common():

    analyzer = ActionHistoryAnalyzer()

    analyzer.record("WATER")
    analyzer.record("PLANT")
    analyzer.record("WATER")

    assert (
        analyzer.most_common()
        == "WATER"
    )


def test_clear():

    analyzer = ActionHistoryAnalyzer()

    analyzer.record("WAIT")

    analyzer.clear()

    assert (
        analyzer.total_actions()
        == 0
    )


def test_empty():

    analyzer = ActionHistoryAnalyzer()

    assert (
        analyzer.most_common()
        is None
    )