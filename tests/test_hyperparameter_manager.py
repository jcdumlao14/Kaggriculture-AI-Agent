from src.hyperparameter_manager import HyperparameterManager


def test_default_learning_rate():

    hp = HyperparameterManager()

    assert hp.get("learning_rate") == 0.10


def test_update_parameter():

    hp = HyperparameterManager()

    hp.set("learning_rate", 0.25)

    assert hp.get("learning_rate") == 0.25


def test_exists():

    hp = HyperparameterManager()

    assert hp.exists("epsilon")
    assert not hp.exists("unknown_parameter")


def test_all():

    hp = HyperparameterManager()

    params = hp.all()

    assert isinstance(params, dict)
    assert "batch_size" in params


def test_reset():

    hp = HyperparameterManager()

    hp.set("epsilon", 0.5)

    hp.reset()

    assert hp.get("epsilon") == 0.10