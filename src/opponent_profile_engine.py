"""
opponent_profile_engine.py

Opponent Profile Engine for the Kaggriculture AI Agent.

Profiles opponent behavior over multiple games.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class OpponentProfileEngine:
    """
    Build long-term opponent profiles.
    """

    def __init__(self):

        self.history = {}

    # ---------------------------------------------------------

    def record(
        self,
        opponent: str,
        strategy: str,
    ) -> None:
        """
        Record an observed strategy.
        """

        strategy = strategy.upper()

        if opponent not in self.history:

            self.history[opponent] = {}

        self.history[opponent][strategy] = (
            self.history[opponent].get(strategy, 0)
            + 1
        )

    # ---------------------------------------------------------

    def dominant_strategy(
        self,
        opponent: str,
    ) -> str:
        """
        Return the most frequently observed strategy.
        """

        if opponent not in self.history:
            return "UNKNOWN"

        return max(
            self.history[opponent],
            key=self.history[opponent].get,
        )

    # ---------------------------------------------------------

    def strategy_count(
        self,
        opponent: str,
        strategy: str,
    ) -> int:
        """
        Return how often a strategy was observed.
        """

        if opponent not in self.history:
            return 0

        return self.history[opponent].get(
            strategy.upper(),
            0,
        )

    # ---------------------------------------------------------

    def known(
        self,
        opponent: str,
    ) -> bool:
        """
        Return True if opponent exists.
        """

        return opponent in self.history