"""
task_scheduler.py

Task Scheduler for the Kaggriculture AI Agent.

Queues and executes tasks in FIFO order.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from collections import deque


class TaskScheduler:
    """
    FIFO task scheduler.
    """

    def __init__(self):
        self._queue = deque()

    # ---------------------------------------------------------

    def add_task(self, task):
        """
        Add a callable task.
        """
        self._queue.append(task)

    # ---------------------------------------------------------

    def run_next(self):
        """
        Execute the next queued task.
        """
        if not self._queue:
            return None

        task = self._queue.popleft()
        return task()

    # ---------------------------------------------------------

    def pending_tasks(self) -> int:
        """
        Return number of queued tasks.
        """
        return len(self._queue)

    # ---------------------------------------------------------

    def has_tasks(self) -> bool:
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

        # ---------------------------------------------------------

    def peek(self):
        """
        Return the next task without removing it.
        """

        if not self._queue:
            return None

        return self._queue[0]

    # ---------------------------------------------------------

    def run_all(self):
        """
        Execute every queued task.
        """

        results = []

        while self.has_tasks():
            results.append(
                self.run_next()
            )

        return results