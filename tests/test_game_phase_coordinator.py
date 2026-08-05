from src.game_phase_coordinator import (
    GamePhaseCoordinator,
)


def test_early():

    manager = GamePhaseCoordinator()

    assert manager.season_phase(2) == "EARLY"


def test_mid():

    manager = GamePhaseCoordinator()

    assert manager.season_phase(15) == "MID"


def test_late():

    manager = GamePhaseCoordinator()

    assert manager.season_phase(24) == "LATE"


def test_end():

    manager = GamePhaseCoordinator()

    assert manager.is_endgame(29)


def test_force_sell():

    manager = GamePhaseCoordinator()

    assert manager.should_force_sell(29)


def test_expand():

    manager = GamePhaseCoordinator()

    assert manager.should_expand(10)