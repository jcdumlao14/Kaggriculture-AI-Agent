from src.reward_shaping_engine import RewardShapingEngine


def test_reward():

    engine = RewardShapingEngine()

    value = engine.reward(
        profit=1000,
        harvested=2,
        watered=5,
        animals_cared=1,
    )

    assert value > 0


def test_penalty():

    engine = RewardShapingEngine()

    reward = engine.reward(
        penalties=20,
    )

    assert reward < 0


def test_normalized():

    engine = RewardShapingEngine()

    assert engine.normalized_reward(50) == 0.5


def test_positive():

    engine = RewardShapingEngine()

    assert engine.positive(10)


def test_negative():

    engine = RewardShapingEngine()

    assert not engine.positive(-5)