"""
priority_task_scheduler.py

Priority Task Scheduler for the Kaggriculture AI Agent.

Executes higher-priority tasks before lower-priority tasks.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

import heapq


class PriorityTaskScheduler:
    """
    Priority-based task scheduler.
    """

    def __init__(self):
        self._queue = []
        self._counter = 0

    # ---------------------------------------------------------

    def add_task(self, task, priority: int = 0):
        """
        Add a task with a priority.

        Lower priority values execute first.
        """
        heapq.heappush(
            self._queue,
            (priority, self._counter, task),
        )
        self._counter += 1

    # ---------------------------------------------------------

    def run_next(self):
        """
        Execute the highest-priority task.
        """
        if not self._queue:
            return None

        _, _, task = heapq.heappop(self._queue)
        return task()

    # ---------------------------------------------------------

    def pending_tasks(self):
        """
        Return queued task count.
        """
        return len(self._queue)

    # ---------------------------------------------------------

    def has_tasks(self):
        """
        Return True if tasks remain.
        """
        return bool(self._queue)

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove every queued task.
        """
        self._queue.clear()