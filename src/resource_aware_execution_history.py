"""
resource_aware_execution_history.py

Resource-Aware Execution History for the
Kaggriculture AI Agent.

Stores and summarizes resource-aware execution results.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAwareExecutionHistory:
    """
    Maintain execution history.
    """

    def __init__(self):
        self._results: list[dict] = []

    # ---------------------------------------------------------

    def record(
        self,
        *,
        result: dict,
    ) -> dict:
        """
        Record an execution result and return it.
        """

        stored = dict(result)

        self._results.append(stored)

        return stored

    # ---------------------------------------------------------

    def all(
        self,
    ) -> list[dict]:
        """
        Return all recorded results.
        """

        return list(self._results)

    # ---------------------------------------------------------

    def latest(
        self,
    ) -> dict | None:
        """
        Return the most recent result.
        """

        if not self._results:
            return None

        return self._results[-1]

    # ---------------------------------------------------------

    def count(
        self,
    ) -> int:
        """
        Return the number of recorded results.
        """

        return len(self._results)

    # ---------------------------------------------------------

    def successful(
        self,
    ) -> list[dict]:
        """
        Return successful execution results.
        """

        return [
            result
            for result in self._results
            if result.get("success", False)
        ]

    # ---------------------------------------------------------

    def failed(
        self,
    ) -> list[dict]:
        """
        Return failed execution results.
        """

        return [
            result
            for result in self._results
            if not result.get("success", False)
        ]

    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clear all execution history.
        """

        self._results.clear()

    # ---------------------------------------------------------

    def success_rate(
        self,
    ) -> float:
        """
        Return the historical execution success rate.
        """

        if not self._results:
            return 0.0

        return len(
            self.successful()
        ) / len(self._results)