from src.experiment_manager import ExperimentManager


def test_create_experiment():

    experiment = ExperimentManager("baseline")

    assert experiment.name == "baseline"


def test_set_hyperparameter():

    experiment = ExperimentManager("baseline")

    experiment.set_hyperparameter("learning_rate", 0.1)

    assert experiment.get_hyperparameter("learning_rate") == 0.1


def test_log_metric():

    experiment = ExperimentManager("baseline")

    experiment.log_metric("reward", 125)

    assert experiment.get_metric("reward") == 125


def test_summary():

    experiment = ExperimentManager("baseline")

    experiment.set_hyperparameter("epsilon", 0.2)
    experiment.log_metric("reward", 500)

    summary = experiment.summary()

    assert summary["name"] == "baseline"
    assert summary["hyperparameters"]["epsilon"] == 0.2
    assert summary["metrics"]["reward"] == 500


def test_reset():

    experiment = ExperimentManager("baseline")

    experiment.set_hyperparameter("gamma", 0.95)
    experiment.log_metric("reward", 100)

    experiment.reset()

    assert experiment.hyperparameters == {}
    assert experiment.metrics == {}