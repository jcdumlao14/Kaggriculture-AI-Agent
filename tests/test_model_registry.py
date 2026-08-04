from src.model_registry import ModelRegistry


def test_register():

    registry = ModelRegistry()

    registry.register(
        "baseline",
        score=150,
        checkpoint="baseline.json",
    )

    assert registry.exists("baseline")


def test_get():

    registry = ModelRegistry()

    registry.register(
        "v1",
        score=100,
        checkpoint="v1.json",
    )

    model = registry.get("v1")

    assert model["score"] == 100
    assert model["checkpoint"] == "v1.json"


def test_best_model():

    registry = ModelRegistry()

    registry.register(
        "A",
        100,
        "a.json",
    )

    registry.register(
        "B",
        250,
        "b.json",
    )

    registry.register(
        "C",
        150,
        "c.json",
    )

    assert registry.best_model() == "B"


def test_remove():

    registry = ModelRegistry()

    registry.register(
        "temp",
        50,
        "temp.json",
    )

    registry.remove("temp")

    assert not registry.exists("temp")


def test_list_models():

    registry = ModelRegistry()

    registry.register(
        "A",
        1,
        "a.json",
    )

    registry.register(
        "B",
        2,
        "b.json",
    )

    models = registry.list_models()

    assert len(models) == 2
    assert "A" in models
    assert "B" in models


def test_count():

    registry = ModelRegistry()

    registry.register(
        "A",
        1,
        "a.json",
    )

    registry.register(
        "B",
        2,
        "b.json",
    )

    assert registry.count() == 2


def test_clear():

    registry = ModelRegistry()

    registry.register(
        "baseline",
        100,
        "baseline.json",
    )

    registry.clear()

    assert registry.count() == 0
    assert registry.list_models() == {}