from src.latency_tracker import LatencyTracker


def test_record():

    tracker = LatencyTracker()

    tracker.record(12.5)

    assert tracker.count() == 1


def test_latest():

    tracker = LatencyTracker()

    tracker.record(10)
    tracker.record(20)

    assert tracker.latest() == 20


def test_minimum():

    tracker = LatencyTracker()

    tracker.record(12)
    tracker.record(5)
    tracker.record(8)

    assert tracker.minimum() == 5


def test_maximum():

    tracker = LatencyTracker()

    tracker.record(12)
    tracker.record(5)
    tracker.record(18)

    assert tracker.maximum() == 18


def test_average():

    tracker = LatencyTracker()

    tracker.record(10)
    tracker.record(20)
    tracker.record(30)

    assert tracker.average() == 20