from src.benchmark_suite import BenchmarkSuite


def test_add_result():

    suite = BenchmarkSuite()

    suite.add_result("Opening", 120)

    assert suite.score("Opening") == 120


def test_average_score():

    suite = BenchmarkSuite()

    suite.add_result("A", 100)
    suite.add_result("B", 200)
    suite.add_result("C", 300)

    assert suite.average_score() == 200


def test_best_scenario():

    suite = BenchmarkSuite()

    suite.add_result("Opening", 100)
    suite.add_result("Midgame", 220)
    suite.add_result("Endgame", 180)

    assert suite.best_scenario() == "Midgame"


def test_summary():

    suite = BenchmarkSuite()

    suite.add_result("Scenario1", 50)
    suite.add_result("Scenario2", 150)

    summary = suite.summary()

    assert summary["count"] == 2
    assert summary["average_score"] == 100
    assert summary["best_scenario"] == "Scenario2"


def test_reset():

    suite = BenchmarkSuite()

    suite.add_result("Scenario", 80)

    suite.reset()

    assert suite.summary()["count"] == 0