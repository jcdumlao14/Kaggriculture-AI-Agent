from src.animal_care_analyzer import (
    AnimalCareAnalyzer,
)


def test_needs_feed():

    analyzer = AnimalCareAnalyzer()

    tile = {
        "animal": "COW",
        "fed_today": False,
    }

    assert analyzer.needs_feed(tile)


def test_no_feed():

    analyzer = AnimalCareAnalyzer()

    tile = {
        "animal": "COW",
        "fed_today": True,
    }

    assert not analyzer.needs_feed(tile)


def test_needs_care():

    analyzer = AnimalCareAnalyzer()

    tile = {
        "animal": "GOOSE",
        "cared_today": False,
    }

    assert analyzer.needs_care(tile)


def test_feed_count():

    analyzer = AnimalCareAnalyzer()

    animals = [
        {
            "animal": "COW",
            "fed_today": False,
        },
        {
            "animal": "SHEEP",
            "fed_today": True,
        },
        {
            "animal": "GOOSE",
            "fed_today": False,
        },
    ]

    assert analyzer.feed_count(animals) == 2


def test_urgent():

    analyzer = AnimalCareAnalyzer()

    animals = [
        {
            "animal": "COW",
            "consecutive_unfed": 1,
        },
        {
            "animal": "GOOSE",
            "consecutive_unfed": 2,
        },
    ]

    urgent = analyzer.urgent(animals)

    assert urgent["animal"] == "GOOSE"