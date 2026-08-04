"""
tournament_manager.py

Tournament Manager for the Kaggriculture AI Agent.

Tracks tournament results between multiple AI agents.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class TournamentManager:
    """
    Stores tournament standings.
    """

    def __init__(self):
        self._results = {}

    # ---------------------------------------------------------

    def register(self, agent: str):
        """
        Register an agent.
        """
        if agent not in self._results:
            self._results[agent] = {
                "wins": 0,
                "losses": 0,
            }

    # ---------------------------------------------------------

    def record_win(self, agent: str):
        """
        Record a win.
        """
        self.register(agent)
        self._results[agent]["wins"] += 1

    # ---------------------------------------------------------

    def record_loss(self, agent: str):
        """
        Record a loss.
        """
        self.register(agent)
        self._results[agent]["losses"] += 1

    # ---------------------------------------------------------

    def standings(self):
        """
        Return standings sorted by wins.
        """
        return sorted(
            self._results.items(),
            key=lambda item: (
                item[1]["wins"],
                -item[1]["losses"],
            ),
            reverse=True,
        )

    # ---------------------------------------------------------

    def stats(self, agent: str):
        """
        Return one agent's statistics.
        """
        return self._results.get(agent)

    # ---------------------------------------------------------

    def reset(self):
        """
        Clear tournament.
        """
        self._results.clear()