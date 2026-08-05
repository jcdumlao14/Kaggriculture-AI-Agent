"""
search_controller.py

Search Controller for the Kaggriculture AI Agent.

Selects the appropriate search strategy for the
current game state.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class SearchController:
    """
    Chooses a search strategy.
    """

    def select_algorithm(
        self,
        *,
        turn: int,
        max_turns: int = 720,
    ) -> str:
        """
        Return the preferred search algorithm.
        """

        progress = turn / max_turns

        if progress < 0.33:
            return "BEAM_SEARCH"

        if progress < 0.66:
            return "ALPHA_BETA"

        return "MCTS"

    # ---------------------------------------------------------

    def is_early_game(
        self,
        turn: int,
        max_turns: int = 720,
    ) -> bool:

        return turn / max_turns < 0.33

    # ---------------------------------------------------------

    def is_mid_game(
        self,
        turn: int,
        max_turns: int = 720,
    ) -> bool:

        progress = turn / max_turns

        return 0.33 <= progress < 0.66

    # ---------------------------------------------------------

    def is_late_game(
        self,
        turn: int,
        max_turns: int = 720,
    ) -> bool:

        return turn / max_turns >= 0.66