import time

from src.performance_profiler import PerformanceProfiler


def test_start_stop():

    profiler = PerformanceProfiler()

    profiler.start()
    time.sleep(0.001)
    elapsed = profiler.stop()

    assert elapsed > 0


def test_runs():

    profiler = PerformanceProfiler()

    profiler.start()
    profiler.stop()

    profiler.start()
    profiler.stop()

    assert profiler.runs() == 2


def test_average_time():

    profiler = PerformanceProfiler()

    profiler.start()
    profiler.stop()

    profiler.start()
    profiler.stop()

    assert profiler.average_time() >= 0


def test_summary():

    profiler = PerformanceProfiler()

    profiler.start()
    profiler.stop()

    summary = profiler.summary()

    assert summary["runs"] == 1
    assert "average_time" in summary
    assert "last_time" in summary


def test_reset():

    profiler = PerformanceProfiler()

    profiler.start()
    profiler.stop()

    profiler.reset()

    assert profiler.runs() == 0
    