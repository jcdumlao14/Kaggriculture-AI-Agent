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

def test_worker_count():

    coordinator = StrategyCoordinator()

    state = {
        "farmer": [0, 0],
        "hands": [
            [1, 1],
            [2, 2],
        ],
    }

    assert coordinator.worker_count(state) == 3


def test_best_animal_action():

    coordinator = StrategyCoordinator()

    animal = {
        "harvest_ready": True,
    }

    assert (
        coordinator.best_animal_action(
            animal,
        )
        == "HARVEST"
    )


def test_should_expand():

    coordinator = StrategyCoordinator()

    assert coordinator.should_expand(
        money=12000,
        available_land=3,
    )