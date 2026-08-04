from src.model_serving_manager import (
    ModelServingManager,
)


def test_register():

    manager = ModelServingManager()

    manager.register(
        "/predict",
        "Policy",
        "v1",
    )

    assert manager.exists("/predict")


def test_predict():

    manager = ModelServingManager()

    manager.register(
        "/predict",
        "Policy",
        "v1",
    )

    result = manager.predict(
        "/predict",
        {"money": 100},
    )

    assert result["model"] == "Policy"


def test_request_counter():

    manager = ModelServingManager()

    manager.register(
        "/predict",
        "Policy",
        "v1",
    )

    manager.predict("/predict", {})

    manager.predict("/predict", {})

    assert manager.request_count("/predict") == 2


def test_disable():

    manager = ModelServingManager()

    manager.register(
        "/predict",
        "Policy",
        "v1",
    )

    manager.disable("/predict")

    assert (
        manager.predict("/predict", {})
        is None
    )


def test_enable():

    manager = ModelServingManager()

    manager.register(
        "/predict",
        "Policy",
        "v1",
    )

    manager.disable("/predict")

    manager.enable("/predict")

    assert (
        manager.predict("/predict", {})
        is not None
    )