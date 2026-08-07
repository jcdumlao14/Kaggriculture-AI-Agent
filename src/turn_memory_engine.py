"""
turn_memory_engine.py

Turn Memory Engine for the Kaggriculture AI Agent.

Stores short-term memory between turns.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class TurnMemoryEngine:
    """
    Stores short-term turn memory.
    """

    def __init__(self):

        self.memory = {}

    # ---------------------------------------------------------

    def remember(
        self,
        key: str,
        value,
    ) -> None:
        """
        Store a value.
        """

        self.memory[key] = value

    # ---------------------------------------------------------

    def recall(
        self,
        key: str,
        default=None,
    ):
        """
        Recall a value.
        """

        return self.memory.get(
            key,
            default,
        )

    # ---------------------------------------------------------

    def forget(
        self,
        key: str,
    ) -> None:
        """
        Remove a memory.
        """

        self.memory.pop(
            key,
            None,
        )

    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clear all memory.
        """

        self.memory.clear()

    # ---------------------------------------------------------

    def keys(
        self,
    ) -> list[str]:
        """
        Return stored keys.
        """

        return sorted(
            self.memory.keys()
        )