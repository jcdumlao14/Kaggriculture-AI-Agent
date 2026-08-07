"""
resource_balance_analyzer.py

Resource Balance Analyzer for the Kaggriculture AI Agent.

Analyzes whether farm resources are balanced
for sustainable growth.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceBalanceAnalyzer:
    """
    Analyze farm resource balance.
    """

    # ---------------------------------------------------------

    def balance_score(
        self,
        *,
        money: float,
        crops: int,
        animals: int,
        fertilizer: int,
    ) -> float:
        """
        Compute an overall balance score.
        """

        score = 100.0

        score -= abs(crops - animals) * 5.0

        if money < 1000:
            score -= 20.0

        if fertilizer == 0 and crops > 0:
            score -= 15.0

        return max(
            0.0,
            score,
        )

    # ---------------------------------------------------------

    def balanced(
        self,
        *,
        money: float,
        crops: int,
        animals: int,
        fertilizer: int,
    ) -> bool:
        """
        Return True if the farm is balanced.
        """

        return (
            self.balance_score(
                money=money,
                crops=crops,
                animals=animals,
                fertilizer=fertilizer,
            )
            >= 70.0
        )

    # ---------------------------------------------------------

    def imbalance(
        self,
        *,
        money: float,
        crops: int,
        animals: int,
        fertilizer: int,
    ) -> float:
        """
        Return imbalance amount.
        """

        return (
            100.0
            - self.balance_score(
                money=money,
                crops=crops,
                animals=animals,
                fertilizer=fertilizer,
            )
        )