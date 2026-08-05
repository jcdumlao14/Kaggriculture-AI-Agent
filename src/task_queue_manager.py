"""
task_queue_manager.py

Task Queue Manager for the Kaggriculture AI Agent.

Maintains an ordered queue of tasks
to be executed by the decision engine.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class TaskQueueManager:
    """
    Manage queued tasks.
    """

    def __init__(self):
        self._tasks = []

    # ---------------------------------------------------------

    def add(
        self,
        task: dict,
    ):
        """
        Add a task.
        """

        self._tasks.append(task)

    # ---------------------------------------------------------

    def pop(self):
        """
        Remove the first task.
        """

        if not self._tasks:
            return None

        return self._tasks.pop(0)

    # ---------------------------------------------------------

    def peek(self):
        """
        Return the first task.
        """

        if not self._tasks:
            return None

        return self._tasks[0]

    # ---------------------------------------------------------

    def size(self) -> int:
        """
        Return queue size.
        """

        return len(self._tasks)

    # ---------------------------------------------------------

    def empty(self) -> bool:
        """
        Return True if queue is empty.
        """

        return len(self._tasks) == 0

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove every task.
        """

        self._tasks.clear()

    # ---------------------------------------------------------

    def tasks(self):
        """
        Return all queued tasks.
        """

        return list(self._tasks)