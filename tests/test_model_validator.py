from src.model_validator import ModelValidator


def sample_model():

    return {
        "score": 250,
        "checkpoint": "best.json",
    }


def sample_metadata():

    return {
        "author": "Jocelyn",
        "algorithm": "Q-Learning",
        "dataset": "Season1",
        "trained_on": "2026-08-04",
    }


def test_checkpoint():

    validator = ModelValidator()

    assert validator.has_checkpoint(
        sample_model()
    )


def test_threshold():

    validator = ModelValidator()

    assert validator.meets_threshold(
        sample_model(),
        200,
    )


def test_metadata():

    validator = ModelValidator()

    assert validator.metadata_complete(
        sample_metadata()
    )


def test_ready():

    validator = ModelValidator()

    assert validator.ready_for_deployment(
        sample_model(),
        sample_metadata(),
        200,
    )


def test_score():

    validator = ModelValidator()

    assert validator.has_score(
        sample_model()
    )