"""
transposition_table.py

Transposition Table for the Kaggriculture AI Agent.

Caches evaluated game states to avoid repeated computation.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class TranspositionTable:
    """
    Cache evaluated game states.
    """

    def __init__(self):
        self.table = {}

    # ---------------------------------------------------------

    def store(self, state, value):
        """
        Store an evaluated state.
        """
        self.table[state] = value

    # ---------------------------------------------------------

    def lookup(self, state):
        """
        Return the cached value for a state.
        """
        return self.table.get(state)

    # ---------------------------------------------------------

    def contains(self, state):
        """
        Check whether a state exists.
        """
        return state in self.table

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove all cached states.
        """
        self.table.clear()

    # ---------------------------------------------------------

    def size(self):
        """
        Number of cached states.
        """
        return len(self.table)