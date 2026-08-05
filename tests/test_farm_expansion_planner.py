from src.farm_expansion_planner import (
    FarmExpansionPlanner,
)


def test_can_expand():

    planner = FarmExpansionPlanner()

    assert planner.can_expand(
        money=5000,
        expansion_cost=2000,
    )


def test_cannot_expand():

    planner = FarmExpansionPlanner()

    assert not planner.can_expand(
        money=1000,
        expansion_cost=2000,
    )


def test_remaining():

    planner = FarmExpansionPlanner()

    assert (
        planner.remaining_quadrants(
            ["NW"]
        )
        == 3
    )


def test_fully_expanded():

    planner = FarmExpansionPlanner()

    assert planner.fully_expanded(
        [
            "NW",
            "NE",
            "SW",
            "SE",
        ]
    )


def test_next_priority():

    planner = FarmExpansionPlanner()

    assert (
        planner.next_priority(
            ["NW"]
        )
        == "NE"
    )


def test_score():

    planner = FarmExpansionPlanner()

    assert (
        planner.expansion_score(
            money=3000,
            expansion_cost=1500,
        )
        == 2.0
    )