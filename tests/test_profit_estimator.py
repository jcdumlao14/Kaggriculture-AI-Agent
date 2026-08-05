from src.profit_estimator import ProfitEstimator


def test_crop_profit():

    estimator = ProfitEstimator()

    assert estimator.crop_profit(
        sell_price=200,
        seed_cost=50,
        yield_units=2,
    ) == 350


def test_profit_per_day():

    estimator = ProfitEstimator()

    value = estimator.profit_per_day(
        sell_price=200,
        seed_cost=50,
        yield_units=2,
        grow_days=5,
    )

    assert value == 70


def test_zero_days():

    estimator = ProfitEstimator()

    value = estimator.profit_per_day(
        sell_price=100,
        seed_cost=20,
        yield_units=1,
        grow_days=0,
    )

    assert value == 80


def test_better_crop():

    estimator = ProfitEstimator()

    carrot = {
        "sell_price": 40,
        "seed_cost": 10,
        "yield_units": 3,
        "grow_days": 2,
    }

    melon = {
        "sell_price": 250,
        "seed_cost": 100,
        "yield_units": 3,
        "grow_days": 4,
    }

    assert estimator.better_crop(
        carrot,
        melon,
    ) == melon


def test_return_type():

    estimator = ProfitEstimator()

    assert isinstance(
        estimator.crop_profit(
            sell_price=100,
            seed_cost=10,
            yield_units=1,
        ),
        float,
    )