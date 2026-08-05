from src.planting_opportunity_analyzer import (
    PlantingOpportunityAnalyzer,
)


def test_empty_tiles():

    analyzer = PlantingOpportunityAnalyzer()

    tiles = [
        None,
        {"kind": "PLANT"},
        None,
    ]

    assert len(analyzer.empty_tiles(tiles)) == 2


def test_available_count():

    analyzer = PlantingOpportunityAnalyzer()

    tiles = [
        None,
        None,
    ]

    assert analyzer.available_count(tiles) == 2


def test_can_plant():

    analyzer = PlantingOpportunityAnalyzer()

    assert analyzer.can_plant(
        empty_tiles=2,
        seed_count=5,
    )


def test_cannot_plant_no_seed():

    analyzer = PlantingOpportunityAnalyzer()

    assert not analyzer.can_plant(
        empty_tiles=2,
        seed_count=0,
    )


def test_next_tile():

    analyzer = PlantingOpportunityAnalyzer()

    tiles = [
        {"kind": "PLANT"},
        None,
    ]

    assert analyzer.next_tile(tiles) is None