from src.opponent_tracker import OpponentTracker


def make_observation(money):

    return {
        "player": 0,
        "farms": [
            {"money": 3000},
            {"money": money},
        ],
    }


def test_money_change():

    tracker = OpponentTracker()

    tracker.update(make_observation(5000))
    tracker.update(make_observation(4200))

    assert tracker.money_change() == -800


def test_expanding():

    tracker = OpponentTracker()

    tracker.update(make_observation(5000))
    tracker.update(make_observation(3000))

    assert tracker.expanding()


def test_getting_richer():

    tracker = OpponentTracker()

    tracker.update(make_observation(2000))
    tracker.update(make_observation(3600))

    assert tracker.getting_richer()