from src.price_history import PriceHistory
from src.market_trend_analyzer import MarketTrendAnalyzer


def make_history():

    history = PriceHistory()

    history.update("MELON", 200)
    history.update("MELON", 250)
    history.update("MELON", 300)

    return history


def test_latest_price():

    analyzer = MarketTrendAnalyzer(
        make_history(),
    )

    assert analyzer.latest_price("MELON") == 300


def test_average_price():

    analyzer = MarketTrendAnalyzer(
        make_history(),
    )

    assert analyzer.average_price("MELON") == 250


def test_trend():

    analyzer = MarketTrendAnalyzer(
        make_history(),
    )

    assert analyzer.trend("MELON") == "UP"


def test_rising():

    analyzer = MarketTrendAnalyzer(
        make_history(),
    )

    assert analyzer.is_price_rising("MELON")


def test_falling():

    history = PriceHistory()

    history.update("MELON", 300)
    history.update("MELON", 250)
    history.update("MELON", 200)

    analyzer = MarketTrendAnalyzer(history)

    assert analyzer.is_price_falling("MELON")


def test_good_time_to_sell():

    analyzer = MarketTrendAnalyzer(
        make_history(),
    )

    assert analyzer.is_good_time_to_sell("MELON")