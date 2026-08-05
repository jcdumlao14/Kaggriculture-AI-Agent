from src.path_planner import PathPlanner


def test_distance():

    planner = PathPlanner()

    assert planner.distance((0, 0), (3, 4)) == 7


def test_east():

    planner = PathPlanner()

    assert planner.next_step((0, 0), (1, 0)) == "EAST"


def test_west():

    planner = PathPlanner()

    assert planner.next_step((2, 0), (1, 0)) == "WEST"


def test_north():

    planner = PathPlanner()

    assert planner.next_step((0, 2), (0, 1)) == "NORTH"


def test_south():

    planner = PathPlanner()

    assert planner.next_step((0, 0), (0, 1)) == "SOUTH"