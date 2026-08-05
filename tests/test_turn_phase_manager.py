from src.turn_phase_manager import (
    TurnPhaseManager,
)


def test_early():

    manager = TurnPhaseManager()

    assert manager.phase(2) == "EARLY"


def test_mid():

    manager = TurnPhaseManager()

    assert manager.phase(12) == "MID"


def test_late():

    manager = TurnPhaseManager()

    assert manager.phase(20) == "LATE"


def test_remaining():

    manager = TurnPhaseManager()

    assert manager.remaining_turns(20) == 4


def test_final_turn():

    manager = TurnPhaseManager()

    assert manager.is_final_turn(23)


def test_progress():

    manager = TurnPhaseManager()

    assert manager.progress(12) == 0.5