"""
performance_profiler.py

Performance Profiler for the Kaggriculture AI Agent.

Measures execution times for AI components.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

import time


class PerformanceProfiler:
    """
    Profiles execution time of code sections.
    """

    def __init__(self):
        self._times = []
        self._start = None

    # ---------------------------------------------------------

    def start(self):
        """
        Start timing.
        """
        self._start = time.perf_counter()

    # ---------------------------------------------------------

    def stop(self):
        """
        Stop timing and record elapsed time.
        """
        if self._start is None:
            return 0.0

        elapsed = time.perf_counter() - self._start

        self._times.append(elapsed)
        self._start = None

        return elapsed

    # ---------------------------------------------------------

    def runs(self):
        """
        Return the number of recorded runs.
        """
        return len(self._times)

    # ---------------------------------------------------------

    def average_time(self):
        """
        Return the average execution time.
        """
        if not self._times:
            return 0.0

        return sum(self._times) / len(self._times)

    # ---------------------------------------------------------

    def minimum_time(self):
        """
        Return the minimum execution time.
        """
        if not self._times:
            return 0.0

        return min(self._times)

    # ---------------------------------------------------------

    def maximum_time(self):
        """
        Return the maximum execution time.
        """
        if not self._times:
            return 0.0

        return max(self._times)

    # ---------------------------------------------------------

    def total_time(self):
        """
        Return the total execution time.
        """
        return sum(self._times)

    # ---------------------------------------------------------

    def last_time(self):
        """
        Return the most recent execution time.
        """
        if not self._times:
            return 0.0

        return self._times[-1]

    # ---------------------------------------------------------

    def summary(self):
        """
        Return profiling statistics.
        """
        return {
            "runs": self.runs(),
            "total_time": self.total_time(),
            "average_time": self.average_time(),
            "minimum_time": self.minimum_time(),
            "maximum_time": self.maximum_time(),
            "last_time": self.last_time(),
        }

    # ---------------------------------------------------------

    def reset(self):
        """
        Clear all recorded timings.
        """
        self._times.clear()
        self._start = None