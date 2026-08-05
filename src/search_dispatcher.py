"""
search_dispatcher.py

Dispatches search requests to the appropriate search
algorithm.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class SearchDispatcher:
    """
    Dispatches search algorithms.

    This first version returns the selected algorithm.
    Later versions will invoke the real implementations.
    """

    def dispatch(
        self,
        algorithm: str,
        state: dict,
    ):
        """
        Dispatch search request.

        Returns the selected algorithm name.
        """

        return algorithm

    # ---------------------------------------------------------

    def supported_algorithms(self):
        """
        Return supported search algorithms.
        """

        return [
            "BEAM_SEARCH",
            "ALPHA_BETA",
            "MCTS",
            "MINIMAX",
        ]

    # ---------------------------------------------------------

    def supports(
        self,
        algorithm: str,
    ) -> bool:

        return (
            algorithm
            in self.supported_algorithms()
        )