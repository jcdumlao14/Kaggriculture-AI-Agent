from src.learning_rate_scheduler import LearningRateScheduler


def test_initial_rate():

    scheduler = LearningRateScheduler()

    assert scheduler.current() == 0.10


def test_decay():

    scheduler = LearningRateScheduler(
        initial_rate=1.0,
        decay=0.5,
    )

    scheduler.step()

    assert scheduler.current() == 0.5


def test_multiple_steps():

    scheduler = LearningRateScheduler(
        initial_rate=1.0,
        decay=0.5,
    )

    scheduler.step()
    scheduler.step()

    assert scheduler.current() == 0.25


def test_minimum_rate():

    scheduler = LearningRateScheduler(
        initial_rate=0.02,
        decay=0.1,
        minimum_rate=0.01,
    )

    scheduler.step()

    assert scheduler.current() == 0.01


def test_reset():

    scheduler = LearningRateScheduler()

    scheduler.step()
    scheduler.reset()

    assert scheduler.current() == scheduler.initial_rate