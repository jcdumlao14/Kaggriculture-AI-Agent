"""
strategy_memory.py

Strategy Memory for the Kaggriculture AI Agent.

Tracks recently used strategies.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from collections import deque


class StrategyMemory:
    """
    Stores recent strategies.
    """

    def __init__(
        self,
        max_size: int = 20,
    ):
        self._memory = deque(maxlen=max_size)

    # ---------------------------------------------------------

    def record(
        self,
        strategy: str,
    ) -> None:
        """
        Record a strategy.
        """

        self._memory.append(strategy)

    # ---------------------------------------------------------

    def last(
        self,
    ) -> str | None:
        """
        Return the most recent strategy.
        """

        if not self._memory:
            return None

        return self._memory[-1]

    # ---------------------------------------------------------

    def history(
        self,
    ) -> list[str]:
        """
        Return all recorded strategies.
        """

        return list(self._memory)

    # ---------------------------------------------------------

    def count(
        self,
    ) -> int:
        """
        Return number of stored strategies.
        """

        return len(self._memory)

    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clear strategy history.
        """

        self._memory.clear()