from src.scoring import CropScorer
from src.crop_planner import CropPlanner


class DummyParser:
    """
    Minimal parser object required by CropScorer.
    """

    def __init__(self):
        self.day = 5
        self.money = 10000


def make_planner():

    parser = DummyParser()

    scorer = CropScorer(parser)

    return CropPlanner(scorer)


def test_choose_crop():

    planner = make_planner()

    assert planner.choose_crop() is not None


def test_can_plant():

    planner = make_planner()

    crop = planner.choose_crop()

    assert planner.can_plant(crop)


def test_affordable():

    planner = make_planner()

    crop = planner.choose_crop()

    assert planner.affordable(crop)


def test_score():

    planner = make_planner()

    crop = planner.choose_crop()

    assert isinstance(
        planner.score(crop),
        float,
    )


def test_return_type():

    planner = make_planner()

    assert isinstance(
        planner.choose_crop(),
        str,
    )