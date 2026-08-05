from src.crop_lifecycle_analyzer import (
    CropLifecycleAnalyzer,
)


def test_age():

    analyzer = CropLifecycleAnalyzer()

    assert analyzer.age(
        current_day=8,
        planted_day=5,
    ) == 3


def test_ready():

    analyzer = CropLifecycleAnalyzer()

    assert analyzer.ready_to_harvest(
        current_day=10,
        planted_day=5,
        mature_day=5,
    )


def test_not_ready():

    analyzer = CropLifecycleAnalyzer()

    assert not analyzer.ready_to_harvest(
        current_day=7,
        planted_day=5,
        mature_day=5,
    )


def test_needs_water():

    analyzer = CropLifecycleAnalyzer()

    assert analyzer.needs_water(
        {
            "watered_today": False,
        }
    )


def test_days_until():

    analyzer = CropLifecycleAnalyzer()

    assert analyzer.days_until_harvest(
        current_day=6,
        planted_day=5,
        mature_day=5,
    ) == 4


def test_status_water():

    analyzer = CropLifecycleAnalyzer()

    assert (
        analyzer.status(
            current_day=6,
            planted_day=5,
            mature_day=5,
            watered_today=False,
        )
        == "WATER"
    )


def test_status_growing():

    analyzer = CropLifecycleAnalyzer()

    assert (
        analyzer.status(
            current_day=6,
            planted_day=5,
            mature_day=10,
            watered_today=True,
        )
        == "GROWING"
    )


def test_status_harvest():

    analyzer = CropLifecycleAnalyzer()

    assert (
        analyzer.status(
            current_day=12,
            planted_day=5,
            mature_day=7,
            watered_today=True,
        )
        == "HARVEST"
    )