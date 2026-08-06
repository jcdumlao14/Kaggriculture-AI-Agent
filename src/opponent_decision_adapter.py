"""
opponent_decision_adapter.py

Opponent Decision Adapter for the Kaggriculture AI Agent.

Adjusts action scores according to the inferred
opponent strategy.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class OpponentDecisionAdapter:
    """
    Modify scores based on opponent strategy.
    """

    STRATEGY_BONUS = {
        "UNKNOWN": 0.0,
        "BALANCED": 0.0,
        "ECONOMIC": 15.0,
        "AGGRESSIVE": 20.0,
        "EXPANSION": 10.0,
    }

    # ---------------------------------------------------------

    def adjustment(
        self,
        strategy: str,
    ) -> float:
        """
        Return adjustment for strategy.
        """

        return float(
            self.STRATEGY_BONUS.get(
                strategy.upper(),
                0.0,
            )
        )

    # ---------------------------------------------------------

    def apply(
        self,
        score: float,
        strategy: str,
    ) -> float:
        """
        Apply adjustment.
        """

        return float(
            score +
            self.adjustment(strategy)
        )

    # ---------------------------------------------------------

    def supported(
        self,
    ) -> list[str]:
        """
        Return supported strategies.
        """

        return sorted(
            self.STRATEGY_BONUS.keys()
        )