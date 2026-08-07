from src.farm_route_planner import (
    FarmRoutePlanner,
)


def test_distance():

    planner = FarmRoutePlanner()

    assert (
        planner.distance(
            (0, 0),
            (3, 4),
        )
        == 7
    )


def test_nearest():

    planner = FarmRoutePlanner()

    target = planner.nearest(
        (0, 0),
        [
            (5, 5),
            (1, 2),
            (8, 8),
        ],
    )

    assert target == (1, 2)


def test_sort():

    planner = FarmRoutePlanner()

    ordered = planner.sort_by_distance(
        (0, 0),
        [
            (3, 3),
            (1, 1),
            (2, 2),
        ],
    )

    assert ordered[0] == (1, 1)


def test_total_distance():

    planner = FarmRoutePlanner()

    assert (
        planner.total_distance(
            [
                (0, 0),
                (1, 0),
                (1, 2),
            ]
        )
        == 3
    )


def test_reachable():

    planner = FarmRoutePlanner()

    assert planner.reachable(
        (0, 0),
        (2, 2),
        4,
    )