from src.harvest_opportunity_analyzer import (
    HarvestOpportunityAnalyzer,
)


def test_count():

    analyzer = HarvestOpportunityAnalyzer()

    tiles = [
        {
            "kind": "PLANT",
            "yield_units": 2,
        },
        {
            "kind": "PLANT",
            "yield_units": 0,
        },
        {
            "kind": "PLANT",
            "yield_units": 5,
        },
    ]

    assert analyzer.count(tiles) == 2


def test_best():

    analyzer = HarvestOpportunityAnalyzer()

    tiles = [
        {
            "kind": "PLANT",
            "yield_units": 1,
        },
        {
            "kind": "PLANT",
            "yield_units": 7,
        },
    ]

    best = analyzer.best(tiles)

    assert best["yield_units"] == 7


def test_empty():

    analyzer = HarvestOpportunityAnalyzer()

    assert analyzer.best([]) is None


def test_harvestable():

    analyzer = HarvestOpportunityAnalyzer()

    tiles = [
        {
            "kind": "PLANT",
            "yield_units": 0,
        },
        {
            "kind": "PLANT",
            "yield_units": 3,
        },
    ]

    assert len(analyzer.harvestable(tiles)) == 1


def test_non_plant():

    analyzer = HarvestOpportunityAnalyzer()

    tiles = [
        {
            "kind": "WEED",
            "yield_units": 10,
        },
        {
            "kind": "PLANT",
            "yield_units": 4,
        },
    ]

    assert analyzer.count(tiles) == 1