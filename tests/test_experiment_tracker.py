from src.experiment_tracker import ExperimentTracker


def test_start():

    tracker = ExperimentTracker()

    tracker.start("exp1")

    assert tracker.get("exp1")["status"] == "running"


def test_log_parameter():

    tracker = ExperimentTracker()

    tracker.start("exp")

    tracker.log_parameter("exp", "learning_rate", 0.01)

    assert tracker.get("exp")["parameters"]["learning_rate"] == 0.01


def test_log_metric():

    tracker = ExperimentTracker()

    tracker.start("exp")

    tracker.log_metric("exp", "accuracy", 0.95)

    assert tracker.get("exp")["metrics"]["accuracy"] == 0.95


def test_finish():

    tracker = ExperimentTracker()

    tracker.start("exp")

    tracker.finish("exp")

    assert tracker.get("exp")["status"] == "completed"


def test_clear():

    tracker = ExperimentTracker()

    tracker.start("exp")

    tracker.clear()

    assert tracker.get("exp") is None