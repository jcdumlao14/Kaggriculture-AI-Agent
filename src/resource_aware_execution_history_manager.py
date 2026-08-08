"""
resource_aware_execution_history_manager.py

Resource-Aware Execution History Manager for the
Kaggriculture AI Agent.

Provides a higher-level interface for managing
resource-aware execution history.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.resource_aware_execution_history import (
    ResourceAwareExecutionHistory,
)


class ResourceAwareExecutionHistoryManager:
    """
    Manage resource-aware execution history.
    """

    def __init__(self):
        self.history = (
            ResourceAwareExecutionHistory()
        )

    # ---------------------------------------------------------

    def record(
        self,
        *,
        result: dict,
    ) -> dict:
        """
        Record an execution result.
        """

        return self.history.record(
            result=result,
        )

    # ---------------------------------------------------------

    def get_all(
        self,
    ) -> list[dict]:
        """
        Return all execution results.
        """

        return self.history.all()

    # ---------------------------------------------------------

    def latest(
        self,
    ) -> dict | None:
        """
        Return the latest execution result.
        """

        return self.history.latest()

    # ---------------------------------------------------------

    def count(
        self,
    ) -> int:
        """
        Return the number of execution results.
        """

        return self.history.count()

    # ---------------------------------------------------------

    def successful(
        self,
    ) -> list[dict]:
        """
        Return successful executions.
        """

        return self.history.successful()

    # ---------------------------------------------------------

    def failed(
        self,
    ) -> list[dict]:
        """
        Return failed executions.
        """

        return self.history.failed()

    # ---------------------------------------------------------

    def success_rate(
        self,
    ) -> float:
        """
        Return historical execution success rate.
        """

        return self.history.success_rate()

    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clear all execution history.
        """

        self.history.clear()

    # ---------------------------------------------------------

    def recent(
        self,
        *,
        limit: int = 5,
    ) -> list[dict]:
        """
        Return the most recent execution results.

        A non-positive limit returns an empty list.
        """

        if limit <= 0:
            return []

        return self.get_all()[-limit:]
    