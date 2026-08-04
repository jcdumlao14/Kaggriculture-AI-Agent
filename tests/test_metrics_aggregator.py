from src.metrics_aggregator import MetricsAggregator


def test_mean():

    metrics = MetricsAggregator()

    metrics.add("reward", 10)
    metrics.add("reward", 20)

    assert metrics.mean("reward") == 15


def test_minimum():

    metrics = MetricsAggregator()

    metrics.add("loss", 5)
    metrics.add("loss", 2)

    assert metrics.minimum("loss") == 2


def test_maximum():

    metrics = MetricsAggregator()

    metrics.add("score", 7)
    metrics.add("score", 12)

    assert metrics.maximum("score") == 12


def test_total():

    metrics = MetricsAggregator()

    metrics.add("episodes", 3)
    metrics.add("episodes", 7)

    assert metrics.total("episodes") == 10


def test_reset():

    metrics = MetricsAggregator()

    metrics.add("reward", 1)

    metrics.reset()

    assert metrics.mean("reward") is None