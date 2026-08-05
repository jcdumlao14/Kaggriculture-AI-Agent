from src.dynamic_market_analyzer import (
    DynamicMarketAnalyzer,
)


def test_profit_margin():

    analyzer = DynamicMarketAnalyzer()

    assert analyzer.profit_margin(
        20,
        50,
    ) == 30


def test_profitable():

    analyzer = DynamicMarketAnalyzer()

    assert analyzer.is_profitable(
        10,
        30,
    )


def test_best_buy():

    analyzer = DynamicMarketAnalyzer()

    market = {
        "WHEAT": {
            "buy_price": 20,
            "sell_price": 35,
        },
        "CARROT": {
            "buy_price": 10,
            "sell_price": 25,
        },
    }

    assert analyzer.best_buy(
        market,
    ) == "CARROT"


def test_best_sell():

    analyzer = DynamicMarketAnalyzer()

    market = {
        "WHEAT": {
            "buy_price": 20,
            "sell_price": 35,
        },
        "MELON": {
            "buy_price": 80,
            "sell_price": 160,
        },
    }

    assert analyzer.best_sell(
        market,
    ) == "MELON"


def test_spread():

    analyzer = DynamicMarketAnalyzer()

    market = {
        "TOMATO": {
            "buy_price": 40,
            "sell_price": 75,
        }
    }

    assert analyzer.spread(
        market,
        "TOMATO",
    ) == 35