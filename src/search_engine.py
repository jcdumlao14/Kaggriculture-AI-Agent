"""
search_engine.py

Search Engine for the Kaggriculture AI Agent.

Maintains candidate moves and selects the
highest-scoring option.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class SearchEngine:
    """
    Search candidate moves and select the best one.
    """

    def __init__(self):
        self.candidates = []

    # ---------------------------------------------------------

    def add_move(
        self,
        action: str,
        score: float,
    ):
        """
        Add a candidate move.
        """

        self.candidates.append(
            {
                "action": action,
                "score": score,
            }
        )

    # ---------------------------------------------------------

    def best_move(self):
        """
        Return the highest-scoring move.
        """

        if not self.candidates:
            return None

        return max(
            self.candidates,
            key=lambda move: move["score"],
        )

    # ---------------------------------------------------------

    def ranking(self):
        """
        Return moves sorted by score.
        """

        return sorted(
            self.candidates,
            key=lambda move: move["score"],
            reverse=True,
        )

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove all candidate moves.
        """

        self.candidates.clear()

    # ---------------------------------------------------------

    def __len__(self):
        return len(self.candidates)