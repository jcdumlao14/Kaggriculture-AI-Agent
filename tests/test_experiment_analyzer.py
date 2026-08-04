from src.experiment_analyzer import ExperimentAnalyzer


def sample():

    return [
        {"accuracy": 0.90},
        {"accuracy": 0.95},
        {"accuracy": 0.85},
    ]


def test_best():

    analyzer = ExperimentAnalyzer()

    assert analyzer.best(
        sample(),
        "accuracy",
    ) == 0.95


def test_average():

    analyzer = ExperimentAnalyzer()

    assert analyzer.average(
        sample(),
        "accuracy",
    ) == 0.90


def test_worst():

    analyzer = ExperimentAnalyzer()

    assert analyzer.worst(
        sample(),
        "accuracy",
    ) == 0.85


def test_count():

    analyzer = ExperimentAnalyzer()

    assert analyzer.count(sample()) == 3


def test_summary():

    analyzer = ExperimentAnalyzer()

    summary = analyzer.summary(
        sample(),
        "accuracy",
    )

    assert summary["count"] == 3
    assert summary["best"] == 0.95