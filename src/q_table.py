"""
q_table.py

Q-Table implementation for the Kaggriculture AI Agent.

Stores action-value estimates for reinforcement learning.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class QTable:
    """
    Simple Q-table.
    """

    def __init__(self):
        self.table = {}

    # ---------------------------------------------------------

    def get(self, state, action):
        """
        Return the Q-value for a state-action pair.
        """
        return self.table.get((state, action), 0.0)

    # ---------------------------------------------------------

    def update(self, state, action, value):
        """
        Set the Q-value.
        """
        self.table[(state, action)] = value

    # ---------------------------------------------------------

    def best_action(self, state):
        """
        Return the action with the highest Q-value.
        """
        actions = [
            (a, v)
            for (s, a), v in self.table.items()
            if s == state
        ]

        if not actions:
            return None

        return max(actions, key=lambda item: item[1])[0]

    # ---------------------------------------------------------

    def size(self):
        """
        Number of learned entries.
        """
        return len(self.table)

    # ---------------------------------------------------------

    def clear(self):
        """
        Reset the Q-table.
        """
        self.table.clear()