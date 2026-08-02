from src.opponent_analyzer import OpponentAnalyzer


def test_record():

    analyzer = OpponentAnalyzer()

    analyzer.record("PLANT")

    assert analyzer.total_actions() == 1


def test_frequency():

    analyzer = OpponentAnalyzer()

    analyzer.record("PLANT")
    analyzer.record("PLANT")
    analyzer.record("HARVEST")

    assert analyzer.frequency("PLANT") == 2


def test_most_common():

    analyzer = OpponentAnalyzer()

    analyzer.record("BUY_LAND")
    analyzer.record("BUY_LAND")
    analyzer.record("HARVEST")

    assert analyzer.most_common() == "BUY_LAND"


def test_aggression():

    analyzer = OpponentAnalyzer()

    analyzer.record("BUY_LAND")
    analyzer.record("PLANT")
    analyzer.record("HARVEST")
    analyzer.record("PASS")

    assert analyzer.aggression_score() == 0.5


def test_reset():

    analyzer = OpponentAnalyzer()

    analyzer.record("PLANT")

    analyzer.reset()

    assert analyzer.total_actions() == 0