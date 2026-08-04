"""
workflow_orchestrator.py

Workflow Orchestrator for the Kaggriculture AI Agent.

Executes workflow steps in sequence.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class WorkflowOrchestrator:
    """
    Executes ordered workflow steps.
    """

    def __init__(self):
        self._steps = []
        self._completed = []

    # ---------------------------------------------------------

    def add_step(
        self,
        name: str,
        callback,
    ):
        """
        Register a workflow step.
        """
        self._steps.append(
            (
                name,
                callback,
            )
        )

    # ---------------------------------------------------------

    def run(self):
        """
        Execute every workflow step.
        """
        self._completed.clear()

        for name, callback in self._steps:
            callback()
            self._completed.append(name)

    # ---------------------------------------------------------

    def completed_steps(self):
        """
        Return completed workflow steps.
        """
        return list(self._completed)

    # ---------------------------------------------------------

    def total_steps(self) -> int:
        """
        Return total workflow steps.
        """
        return len(self._steps)

    # ---------------------------------------------------------

    def reset(self):
        """
        Clear execution history.
        """
        self._completed.clear()

    # ---------------------------------------------------------

    def status(self):
        """
        Return workflow status.
        """
        return {
            "total_steps": self.total_steps(),
            "completed_steps": len(self._completed),
            "finished": (
                len(self._completed)
                == len(self._steps)
                and self.total_steps() > 0
            ),
        }