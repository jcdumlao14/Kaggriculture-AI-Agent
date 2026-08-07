"""
opponent_memory_engine.py

Opponent Memory Engine for the Kaggriculture AI Agent.

Stores information about previously encountered
opponents for long-term strategy adaptation.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class OpponentMemoryEngine:
    """
    Store long-term opponent information.
    """

    def __init__(self):

        self.memory = {}

    # ---------------------------------------------------------

    def record(
        self,
        opponent: str,
        strategy: str,
    ) -> None:
        """
        Record the opponent's latest strategy.
        """

        if opponent not in self.memory:

            self.memory[opponent] = {
                "games": 0,
                "strategy": strategy,
            }

        self.memory[opponent]["games"] += 1
        self.memory[opponent]["strategy"] = strategy

    # ---------------------------------------------------------

    def strategy(
        self,
        opponent: str,
    ) -> str:
        """
        Return the remembered strategy.
        """

        if opponent not in self.memory:
            return "UNKNOWN"

        return self.memory[opponent]["strategy"]

    # ---------------------------------------------------------

    def games(
        self,
        opponent: str,
    ) -> int:
        """
        Return games played.
        """

        if opponent not in self.memory:
            return 0

        return self.memory[opponent]["games"]

    # ---------------------------------------------------------

    def known(
        self,
        opponent: str,
    ) -> bool:
        """
        Return True if opponent is known.
        """

        return opponent in self.memory