from src.request_rate_limiter import (
    RequestRateLimiter,
)


def test_allow():

    limiter = RequestRateLimiter(limit=2)

    assert limiter.allow("client1")
    assert limiter.allow("client1")


def test_limit():

    limiter = RequestRateLimiter(limit=2)

    limiter.allow("client1")
    limiter.allow("client1")

    assert not limiter.allow("client1")


def test_request_count():

    limiter = RequestRateLimiter(limit=5)

    limiter.allow("client1")
    limiter.allow("client1")

    assert limiter.request_count("client1") == 2


def test_reset():

    limiter = RequestRateLimiter(limit=1)

    limiter.allow("client1")

    limiter.reset("client1")

    assert limiter.allow("client1")


def test_remove():

    limiter = RequestRateLimiter(limit=5)

    limiter.allow("client1")

    limiter.remove("client1")

    assert not limiter.exists("client1")