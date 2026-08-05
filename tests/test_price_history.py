from src.price_history import PriceHistory


def test_update():

    history = PriceHistory()

    history.update(
        "MELON",
        300,
    )

    assert history.latest(
        "MELON",
    ) == 300


def test_average():

    history = PriceHistory()

    history.update("MELON", 200)
    history.update("MELON", 300)

    assert history.average(
        "MELON",
    ) == 250


def test_trend_up():

    history = PriceHistory()

    history.update("MELON", 200)
    history.update("MELON", 250)
    history.update("MELON", 300)

    assert history.trend(
        "MELON",
    ) == "UP"


def test_trend_down():

    history = PriceHistory()

    history.update("MELON", 300)
    history.update("MELON", 250)
    history.update("MELON", 200)

    assert history.trend(
        "MELON",
    ) == "DOWN"


def test_trend_stable():

    history = PriceHistory()

    history.update("MELON", 200)
    history.update("MELON", 200)

    assert history.trend(
        "MELON",
    ) == "STABLE"


def test_clear():

    history = PriceHistory()

    history.update(
        "MELON",
        300,
    )

    history.clear()

    assert history.latest(
        "MELON",
    ) == 0.0