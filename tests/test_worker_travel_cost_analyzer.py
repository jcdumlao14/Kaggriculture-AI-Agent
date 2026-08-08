from src.worker_travel_cost_analyzer import (
    WorkerTravelCostAnalyzer,
)


def test_distance():

    analyzer = WorkerTravelCostAnalyzer()

    result = analyzer.distance(
        start=(0, 0),
        target=(3, 4),
    )

    assert result == 7


def test_same_position():

    analyzer = WorkerTravelCostAnalyzer()

    result = analyzer.distance(
        start=(5, 5),
        target=(5, 5),
    )

    assert result == 0


def test_travel_cost():

    analyzer = WorkerTravelCostAnalyzer()

    result = analyzer.travel_cost(
        start=(0, 0),
        target=(3, 4),
        cost_per_step=2.0,
    )

    assert result == 14.0


def test_zero_cost():

    analyzer = WorkerTravelCostAnalyzer()

    result = analyzer.travel_cost(
        start=(0, 0),
        target=(3, 4),
        cost_per_step=0.0,
    )

    assert result == 0.0


def test_negative_cost():

    analyzer = WorkerTravelCostAnalyzer()

    try:
        analyzer.travel_cost(
            start=(0, 0),
            target=(1, 1),
            cost_per_step=-1.0,
        )

        assert False

    except ValueError:
        assert True


def test_closer_target():

    analyzer = WorkerTravelCostAnalyzer()

    result = analyzer.closer(
        start=(0, 0),
        first_target=(2, 2),
        second_target=(8, 8),
    )

    assert result == (2, 2)


def test_equal_distance():

    analyzer = WorkerTravelCostAnalyzer()

    result = analyzer.closer(
        start=(0, 0),
        first_target=(2, 0),
        second_target=(0, 2),
    )

    assert result == (2, 0)