from src.feature_importance_engine import (
    FeatureImportanceEngine,
)


def test_update():

    engine = FeatureImportanceEngine()

    engine.update(
        "money",
        2.5,
    )

    assert engine.importance("money") == 2.5


def test_accumulate():

    engine = FeatureImportanceEngine()

    engine.update("money", 1.0)
    engine.update("money", 2.0)

    assert engine.importance("money") == 3.0


def test_ranking():

    engine = FeatureImportanceEngine()

    engine.update("money", 5.0)
    engine.update("day", 2.0)

    ranking = engine.ranking()

    assert ranking[0][0] == "money"


def test_unknown():

    engine = FeatureImportanceEngine()

    assert engine.importance("profit") == 0.0


def test_reset():

    engine = FeatureImportanceEngine()

    engine.update("money", 5.0)
    engine.reset()

    assert engine.ranking() == []