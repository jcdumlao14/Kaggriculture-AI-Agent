from src.search_controller import SearchController


def test_early_game():

    controller = SearchController()

    assert (
        controller.select_algorithm(turn=50)
        == "BEAM_SEARCH"
    )


def test_mid_game():

    controller = SearchController()

    assert (
        controller.select_algorithm(turn=300)
        == "ALPHA_BETA"
    )


def test_late_game():

    controller = SearchController()

    assert (
        controller.select_algorithm(turn=650)
        == "MCTS"
    )


def test_flags():

    controller = SearchController()

    assert controller.is_early_game(10)
    assert controller.is_mid_game(350)
    assert controller.is_late_game(700)


def test_boundaries():

    controller = SearchController()

    assert (
        controller.select_algorithm(turn=238)
        == "ALPHA_BETA"
    )

    assert (
        controller.select_algorithm(turn=476)
        == "MCTS"
    )