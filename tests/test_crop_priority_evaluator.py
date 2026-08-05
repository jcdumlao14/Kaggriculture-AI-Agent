from src.crop_priority_evaluator import CropPriorityEvaluator


def test_score():

    evaluator = CropPriorityEvaluator()

    score = evaluator.score(
        price=100,
        yield_units=4,
        grow_days=2,
    )

    assert score == 200


def test_best_crop():

    evaluator = CropPriorityEvaluator()

    crops = {
        "CARROT": {
            "price": 40,
            "yield_units": 3,
            "grow_days": 2,
        },
        "MELON": {
            "price": 250,
            "yield_units": 3,
            "grow_days": 4,
        },
    }

    assert evaluator.best_crop(crops) == "MELON"


def test_empty():

    evaluator = CropPriorityEvaluator()

    assert evaluator.best_crop({}) is None


def test_zero_days():

    evaluator = CropPriorityEvaluator()

    assert evaluator.score(
        price=50,
        yield_units=2,
        grow_days=0,
    ) == 100


def test_return_type():

    evaluator = CropPriorityEvaluator()

    assert isinstance(
        evaluator.score(
            price=10,
            yield_units=1,
            grow_days=1,
        ),
        float,
    )