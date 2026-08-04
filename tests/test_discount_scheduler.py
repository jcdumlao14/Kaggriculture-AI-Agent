from src.discount_scheduler import DiscountScheduler


def test_initial_gamma():
    
    scheduler = DiscountScheduler()

    assert scheduler.current() == 0.80


def test_step():

    scheduler = DiscountScheduler(
        initial_gamma=0.50,
        increment=0.10,
    )

    scheduler.step()

    assert scheduler.current() == 0.60


def test_maximum():

    scheduler = DiscountScheduler(
        initial_gamma=0.95,
        maximum_gamma=0.99,
        increment=0.10,
    )

    scheduler.step()

    assert scheduler.current() == 0.99


def test_reset():

    scheduler = DiscountScheduler()

    scheduler.step()

    scheduler.reset()

    assert scheduler.current() == 0.80


def test_multiple_steps():

    scheduler = DiscountScheduler(
        initial_gamma=0.50,
        increment=0.05,
    )

    scheduler.step()
    scheduler.step()

    assert scheduler.current() == 0.60