from src.strategy_coordinator import (
    StrategyCoordinator,
)


def make_obs(
    day=5,
    hour=10,
):
    return {
        "day": day,
        "hour": hour,
    }


def test_strategy():

    coordinator = StrategyCoordinator()

    strategy = coordinator.strategy(
        make_obs(),
    )

    assert "algorithm" in strategy


def test_phase():

    coordinator = StrategyCoordinator()

    assert (
        coordinator.turn_phase_name(
            make_obs(hour=22),
        )
        == "LATE"
    )


def test_algorithm():

    coordinator = StrategyCoordinator()

    assert isinstance(
        coordinator.search_algorithm(
            make_obs(),
        ),
        str,
    )


def test_late_game():

    coordinator = StrategyCoordinator()

    assert coordinator.is_late_game(
        make_obs(day=28),
    )


def test_end_day():

    coordinator = StrategyCoordinator()

    assert coordinator.is_end_of_day(
        make_obs(hour=21),
    )