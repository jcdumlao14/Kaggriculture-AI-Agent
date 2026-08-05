from src.crop_recommendation_engine import (
    CropRecommendationEngine,
)


def test_best_crop():

    engine = CropRecommendationEngine()

    crops = [
        {
            "name": "CARROT",
            "score": 80,
        },
        {
            "name": "MELON",
            "score": 210,
        },
        {
            "name": "TOMATO",
            "score": 130,
        },
    ]

    result = engine.recommend(crops)

    assert result["name"] == "MELON"


def test_name():

    engine = CropRecommendationEngine()

    crops = [
        {
            "name": "CARROT",
            "score": 100,
        }
    ]

    assert (
        engine.recommendation_name(crops)
        == "CARROT"
    )


def test_score():

    engine = CropRecommendationEngine()

    crops = [
        {
            "name": "CARROT",
            "score": 150,
        }
    ]

    assert (
        engine.recommendation_score(crops)
        == 150.0
    )


def test_empty():

    engine = CropRecommendationEngine()

    assert engine.recommend([]) is None


def test_empty_score():

    engine = CropRecommendationEngine()

    assert (
        engine.recommendation_score([])
        == 0.0
    )