from src.metrics_collector import MetricsCollector


def test_record():

    collector = MetricsCollector()

    collector.record("reward", 10)

    assert collector.count("reward") == 1


def test_average():

    collector = MetricsCollector()

    collector.record("reward", 10)
    collector.record("reward", 20)
    collector.record("reward", 30)

    assert collector.average("reward") == 20


def test_history():

    collector = MetricsCollector()

    collector.record("loss", 1.0)
    collector.record("loss", 0.8)

    assert collector.history("loss") == [1.0, 0.8]


def test_reset():

    collector = MetricsCollector()

    collector.record("reward", 5)

    collector.reset()

    assert collector.history("reward") == []


def test_missing_metric():

    collector = MetricsCollector()

    assert collector.average("unknown") is None

def test_latest():

    collector = MetricsCollector()

    collector.record("reward", 5)
    collector.record("reward", 12)

    assert collector.latest("reward") == 12


def test_minimum():

    collector = MetricsCollector()

    collector.record("reward", 9)
    collector.record("reward", 2)
    collector.record("reward", 7)

    assert collector.minimum("reward") == 2


def test_maximum():

    collector = MetricsCollector()

    collector.record("reward", 9)
    collector.record("reward", 2)
    collector.record("reward", 15)

    assert collector.maximum("reward") == 15


def test_metric_names():

    collector = MetricsCollector()

    collector.record("reward", 1)
    collector.record("loss", 0.2)

    assert collector.metric_names() == [
        "loss",
        "reward",
    ]