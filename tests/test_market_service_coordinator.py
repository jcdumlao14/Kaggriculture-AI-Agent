from src.market_service_coordinator import (
    MarketServiceCoordinator,
)


def test_prepare_features():

    service = MarketServiceCoordinator()

    features = service.prepare_features(
        state_id="a",
        game_state={
            "money": 500,
        },
    )

    assert features["money"] == 500


def test_normalized():

    service = MarketServiceCoordinator()

    features = service.prepare_features(
        state_id="b",
        game_state={
            "money": 50,
        },
        maximums={
            "money": 100,
        },
    )

    assert features["money"] == 0.5


def test_selected():

    service = MarketServiceCoordinator()

    features = service.prepare_features(
        state_id="c",
        game_state={
            "money": 100,
            "day": 2,
        },
        selected=["money"],
    )

    assert "money" in features
    assert "day" not in features


def test_should_sell():

    service = MarketServiceCoordinator()

    assert service.should_sell(
        current_price=20,
        average_price=10,
    )


def test_clear_cache():

    service = MarketServiceCoordinator()

    service.prepare_features(
        state_id="x",
        game_state={},
    )

    service.clear_cache()

    assert (
        service.feature_service.pipeline.cache.size()
        == 0
    )