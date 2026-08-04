from src.elo_rating import EloRating


def test_register():

    elo = EloRating()

    elo.register("AgentA")

    assert elo.rating("AgentA") == 1000


def test_expected_score():

    elo = EloRating()

    score = elo.expected_score("A", "B")

    assert round(score, 2) == 0.50


def test_update():

    elo = EloRating()

    elo.update("A", "B")

    assert elo.rating("A") > 1000
    assert elo.rating("B") < 1000


def test_leaderboard():

    elo = EloRating()

    elo.update("A", "B")

    board = elo.leaderboard()

    assert board[0][0] == "A"


def test_reset():

    elo = EloRating()

    elo.update("A", "B")

    elo.reset()

    assert elo.leaderboard() == []