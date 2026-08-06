"""
opponent_model.py

Opponent Modeling for the Kaggriculture AI Agent.

Tracks opponent behavior and predicts their
preferred actions.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from collections import Counter


class OpponentModel:
    """
    Learns opponent action frequencies.
    """

    def __init__(self):

        self._actions = Counter()

    # ---------------------------------------------------------

    def record(
        self,
        action: str,
    ) -> None:
        """
        Record an observed opponent action.
        """

        self._actions[action.upper()] += 1

    # ---------------------------------------------------------

    def frequency(
        self,
        action: str,
    ) -> int:
        """
        Return how many times an action occurred.
        """

        return self._actions[action.upper()]

    # ---------------------------------------------------------

    def most_common(
        self,
    ) -> str | None:
        """
        Return the opponent's most common action.
        """

        if not self._actions:
            return None

        return self._actions.most_common(1)[0][0]

    # ---------------------------------------------------------

    def total_actions(
        self,
    ) -> int:
        """
        Return total observed actions.
        """

        return sum(self._actions.values())

    # ---------------------------------------------------------

    def reset(
        self,
    ) -> None:
        """
        Clear all learned observations.
        """

        self._actions.clear()