from src.tournament_manager import TournamentManager


def test_register():

    manager = TournamentManager()

    manager.register("AgentA")

    assert manager.stats("AgentA") == {
        "wins": 0,
        "losses": 0,
    }


def test_record_win():

    manager = TournamentManager()

    manager.record_win("AgentA")

    assert manager.stats("AgentA")["wins"] == 1


def test_record_loss():

    manager = TournamentManager()

    manager.record_loss("AgentA")

    assert manager.stats("AgentA")["losses"] == 1


def test_standings():

    manager = TournamentManager()

    manager.record_win("AgentA")
    manager.record_win("AgentA")

    manager.record_win("AgentB")

    standings = manager.standings()

    assert standings[0][0] == "AgentA"


def test_reset():

    manager = TournamentManager()

    manager.record_win("AgentA")

    manager.reset()

    assert manager.standings() == []