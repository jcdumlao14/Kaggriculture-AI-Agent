from src.prediction_cache_manager import (
    PredictionCacheManager,
)


def test_put():

    cache = PredictionCacheManager()

    cache.put(
        "request1",
        {"action": "plant"},
    )

    assert cache.exists("request1")


def test_get():

    cache = PredictionCacheManager()

    cache.put(
        "request1",
        {"profit": 120},
    )

    result = cache.get("request1")

    assert result["profit"] == 120


def test_remove():

    cache = PredictionCacheManager()

    cache.put(
        "request1",
        {},
    )

    cache.remove("request1")

    assert not cache.exists("request1")


def test_clear():

    cache = PredictionCacheManager()

    cache.put("a", {})
    cache.put("b", {})

    cache.clear()

    assert cache.count() == 0


def test_count():

    cache = PredictionCacheManager()

    cache.put("a", {})
    cache.put("b", {})
    cache.put("c", {})

    assert cache.count() == 3