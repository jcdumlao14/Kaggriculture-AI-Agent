from src.watering_priority_analyzer import (
    WateringPriorityAnalyzer,
)


def test_needs_water():

    analyzer = WateringPriorityAnalyzer()

    assert analyzer.needs_water(
        {
            "kind": "PLANT",
            "watered_today": False,
        }
    )


def test_not_needs_water():

    analyzer = WateringPriorityAnalyzer()

    assert not analyzer.needs_water(
        {
            "kind": "PLANT",
            "watered_today": True,
        }
    )


def test_candidates():

    analyzer = WateringPriorityAnalyzer()

    tiles = [
        {
            "kind": "PLANT",
            "watered_today": False,
        },
        {
            "kind": "PLANT",
            "watered_today": True,
        },
    ]

    assert len(analyzer.candidates(tiles)) == 1


def test_count():

    analyzer = WateringPriorityAnalyzer()

    tiles = [
        {
            "kind": "PLANT",
            "watered_today": False,
        },
        {
            "kind": "PLANT",
            "watered_today": False,
        },
    ]

    assert analyzer.count(tiles) == 2


def test_urgent():

    analyzer = WateringPriorityAnalyzer()

    tiles = [
        {
            "kind": "PLANT",
            "watered_today": False,
            "consecutive_unwatered": 1,
        },
        {
            "kind": "PLANT",
            "watered_today": False,
            "consecutive_unwatered": 2,
        },
    ]

    urgent = analyzer.urgent(tiles)

    assert urgent["consecutive_unwatered"] == 2