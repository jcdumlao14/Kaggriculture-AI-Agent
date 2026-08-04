"""
workflow_engine.py

Workflow Engine for the Kaggriculture AI Agent.

Registers and executes reusable workflows.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class WorkflowEngine:
    """
    Manages named workflows.
    """

    def __init__(self):
        self._workflows = {}

    # ---------------------------------------------------------

    def register(self, name: str, workflow):
        """
        Register a workflow.
        """
        self._workflows[name] = workflow

    # ---------------------------------------------------------

    def run(self, name: str, data):
        """
        Execute a workflow.
        """
        if name not in self._workflows:
            raise KeyError(f"Workflow '{name}' is not registered.")

        return self._workflows[name](data)

    # ---------------------------------------------------------

    def exists(self, name: str) -> bool:
        """
        Check whether a workflow exists.
        """
        return name in self._workflows

    # ---------------------------------------------------------

    def list_workflows(self):
        """
        Return workflow names.
        """
        return sorted(self._workflows.keys())

    # ---------------------------------------------------------

    def unregister(self, name: str):
        """
        Remove a workflow.
        """
        self._workflows.pop(name, None)

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove all workflows.
        """
        self._workflows.clear()