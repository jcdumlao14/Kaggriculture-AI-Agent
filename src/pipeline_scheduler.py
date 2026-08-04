"""
pipeline_scheduler.py

Pipeline Scheduler for the Kaggriculture AI Agent.

Queues and executes workflows.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from collections import deque


class PipelineScheduler:
    """
    Schedules workflow execution.
    """

    def __init__(self):
        self._queue = deque()

    # ---------------------------------------------------------

    def schedule(
        self,
        workflow,
    ):
        """
        Add a workflow to the queue.
        """
        self._queue.append(workflow)

    # ---------------------------------------------------------

    def run_next(self):
        """
        Execute the next scheduled workflow.
        """
        if not self._queue:
            return None

        workflow = self._queue.popleft()
        workflow.run()

        return workflow

    # ---------------------------------------------------------

    def pending(self):
        """
        Return number of queued workflows.
        """
        return len(self._queue)

    # ---------------------------------------------------------

    def is_empty(self):
        """
        Return True if no workflows remain.
        """
        return len(self._queue) == 0

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove all scheduled workflows.
        """
        self._queue.clear()