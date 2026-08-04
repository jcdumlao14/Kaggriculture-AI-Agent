from src.endgame_solver import EndgameSolver


def test_remaining_days():

    solver = EndgameSolver()

    assert solver.remaining_days(25) == 5


def test_is_endgame():

    solver = EndgameSolver()

    assert solver.is_endgame(26)


def test_sell_everything():

    solver = EndgameSolver()

    assert solver.should_sell_everything(29)


def test_should_not_plant():

    solver = EndgameSolver()

    assert not solver.should_plant(29, 4)


def test_should_plant():

    solver = EndgameSolver()

    assert solver.should_plant(25, 3)
    