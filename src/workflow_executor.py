"""
workflow_executor.py

Workflow Executor for the Kaggriculture AI Agent.

Executes workflows and tracks execution status.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class WorkflowExecutor:
    """
    Executes workflows with status tracking.
    """

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

    def __init__(self):
        self.reset()

    # ---------------------------------------------------------

    def execute(self, workflow):
        """
        Execute a workflow.
        """
        self._status = self.RUNNING
        self._exception = None

        try:
            workflow.run()
            self._status = self.COMPLETED

        except Exception as exc:
            self._status = self.FAILED
            self._exception = exc

    # ---------------------------------------------------------

    def status(self):
        """
        Return current execution status.
        """
        return self._status

    # ---------------------------------------------------------

    def succeeded(self) -> bool:
        """
        Return True if execution completed successfully.
        """
        return self._status == self.COMPLETED

    # ---------------------------------------------------------

    def failed(self) -> bool:
        """
        Return True if execution failed.
        """
        return self._status == self.FAILED

    # ---------------------------------------------------------

    def exception(self):
        """
        Return the last captured exception.
        """
        return self._exception

    # ---------------------------------------------------------

    def reset(self):
        """
        Reset executor state.
        """
        self._status = self.PENDING
        self._exception = None