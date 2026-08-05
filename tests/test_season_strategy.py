from src.parser import ObservationParser
from src.season_strategy import SeasonStrategy


def make_parser(day):

    observation = {
        "player": 0,
        "day": day,
        "hour": 0,
        "farms": [
            {
                "money": 3000,
                "farmer": [0, 0],
                "tiles": [
                    [None] * 10
                    for _ in range(10)
                ],
            }
        ],
        "private": {
            "shed": {},
            "seeds": {},
            "inventories": {},
        },
        "market": {
            "prices": {},
            "inventory": {},
        },
        "town": {
            "unlocked_shops": [],
        },
    }

    return ObservationParser(observation)


# ---------------------------------------------------------


def test_early_phase():

    strategy = SeasonStrategy(
        make_parser(3),
    )

    assert strategy.phase() == "EARLY"


def test_mid_phase():

    strategy = SeasonStrategy(
        make_parser(15),
    )

    assert strategy.phase() == "MID"


def test_late_phase():

    strategy = SeasonStrategy(
        make_parser(24),
    )

    assert strategy.phase() == "LATE"


def test_end_phase():

    strategy = SeasonStrategy(
        make_parser(29),
    )

    assert strategy.phase() == "END"


def test_remaining_days():

    strategy = SeasonStrategy(
        make_parser(10),
    )

    assert strategy.remaining_days() == 20


def test_remaining_days_never_negative():

    strategy = SeasonStrategy(
        make_parser(35),
    )

    assert strategy.remaining_days() == 0


def test_can_plant_true():

    strategy = SeasonStrategy(
        make_parser(20),
    )

    assert strategy.can_plant(5)


def test_can_plant_false():

    strategy = SeasonStrategy(
        make_parser(29),
    )

    assert not strategy.can_plant(5)


def test_should_sell_all():

    strategy = SeasonStrategy(
        make_parser(29),
    )

    assert strategy.should_sell_all()


def test_should_invest():

    strategy = SeasonStrategy(
        make_parser(5),
    )

    assert strategy.should_invest()