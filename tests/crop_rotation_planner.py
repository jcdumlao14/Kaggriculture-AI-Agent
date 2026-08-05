from src.crop_rotation_planner import (
    CropRotationPlanner,
)


def test_record():

    planner = CropRotationPlanner()

    planner.record("CARROT")

    assert planner.history() == ["CARROT"]


def test_last_crop():

    planner = CropRotationPlanner()

    planner.record("CARROT")
    planner.record("MELON")

    assert planner.last_crop() == "MELON"


def test_should_rotate_true():

    planner = CropRotationPlanner()

    planner.record("CARROT")

    assert planner.should_rotate("CARROT")


def test_should_rotate_false():

    planner = CropRotationPlanner()

    planner.record("CARROT")

    assert not planner.should_rotate("MELON")


def test_reset():

    planner = CropRotationPlanner()

    planner.record("CARROT")

    planner.reset()

    assert planner.history() == []