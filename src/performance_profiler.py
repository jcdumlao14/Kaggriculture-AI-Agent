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

    def average_time(self):
        """
        Return average execution time.
        """
        if not self._times:
            return 0.0

        return sum(self._times) / len(self._times)

    # ---------------------------------------------------------

    def runs(self):
        """
        Return the number of recorded runs.
        """
        return len(self._times)

    # ---------------------------------------------------------

    def summary(self):
        """
        Return profiling statistics.
        """
        return {
            "runs": self.runs(),
            "average_time": self.average_time(),
            "last_time": self._times[-1] if self._times else 0.0,
        }

    # ---------------------------------------------------------

    def reset(self):
        """
        Clear all recorded timings.
        """
        self._times.clear()
        self._start = None