from src.experiment_comparator import ExperimentComparator


def test_best():

    comparator = ExperimentComparator()

    experiments = {
        "A": {"accuracy": 0.91},
        "B": {"accuracy": 0.95},
    }

    assert comparator.best(experiments, "accuracy") == "B"


def test_compare():

    comparator = ExperimentComparator()

    a = {"score": 20}
    b = {"score": 15}

    assert comparator.compare(a, b, "score") == 5


def test_rank():

    comparator = ExperimentComparator()

    experiments = {
        "A": {"reward": 5},
        "B": {"reward": 8},
        "C": {"reward": 3},
    }

    assert comparator.rank(experiments, "reward") == [
        "B",
        "A",
        "C",
    ]


def test_better():

    comparator = ExperimentComparator()

    assert comparator.better(
        {"acc": 0.9},
        {"acc": 0.8},
        "acc",
    )


def test_equal():

    comparator = ExperimentComparator()

    assert comparator.equal(
        {"loss": 0.2},
        {"loss": 0.2},
        "loss",
    )