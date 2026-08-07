from src.feature_extraction_engine import FeatureExtractionEngine


def test_extract():

    engine = FeatureExtractionEngine()

    state = {
        "money": 5000,
        "day": 4,
        "hour": 10,
        "inventory": {"wheat": 5},
        "market": {"prices": {"wheat": 20}},
        "crops": [1, 2],
        "animals": [1],
    }

    features = engine.extract(state)

    assert features["money"] == 5000
    assert features["crop_count"] == 2
    assert features["animal_count"] == 1


def test_vector():

    engine = FeatureExtractionEngine()

    vector = engine.vector({})

    assert len(vector) == 7


def test_feature_names():

    engine = FeatureExtractionEngine()

    names = engine.feature_names()

    assert "money" in names


def test_empty_state():

    engine = FeatureExtractionEngine()

    features = engine.extract({})

    assert features["money"] == 0


def test_inventory_size():

    engine = FeatureExtractionEngine()

    features = engine.extract(
        {
            "inventory": {
                "wheat": 5,
                "carrot": 2,
            }
        }
    )

    assert features["inventory_size"] == 2