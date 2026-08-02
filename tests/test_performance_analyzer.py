from src.performance_analyzer import PerformanceAnalyzer


def test_turn_counter():

    analyzer = PerformanceAnalyzer()

    analyzer.record_turn()

    assert analyzer.turns == 1


def test_profit():

    analyzer = PerformanceAnalyzer()

    analyzer.add_profit(250)

    assert analyzer.total_profit == 250


def test_average_utility():

    analyzer = PerformanceAnalyzer()

    analyzer.add_utility(80)
    analyzer.add_utility(100)

    assert analyzer.average_utility() == 90


def test_summary():

    analyzer = PerformanceAnalyzer()

    analyzer.record_turn()
    analyzer.record_plant()

    summary = analyzer.summary()

    assert summary["turns"] == 1
    assert summary["plants"] == 1


def test_reset():

    analyzer = PerformanceAnalyzer()

    analyzer.record_turn()
    analyzer.add_profit(500)

    analyzer.reset()

    assert analyzer.turns == 0
    assert analyzer.total_profit == 0