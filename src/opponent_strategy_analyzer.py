"""
opponent_strategy_analyzer.py

Opponent Strategy Analyzer for the Kaggriculture AI Agent.

Infers the opponent's overall strategy from
their observed actions.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.opponent_model import OpponentModel


class OpponentStrategyAnalyzer:
    """
    Classify opponent strategy.
    """

    def __init__(
        self,
        model: OpponentModel,
    ):

        self.model = model

    # ---------------------------------------------------------

    def strategy(self) -> str:
        """
        Return inferred strategy.
        """

        if self.model.total_actions() == 0:
            return "UNKNOWN"

        sell = self.model.frequency("SELL")
        harvest = self.model.frequency("HARVEST")
        expand = self.model.frequency("EXPAND")
        plant = self.model.frequency("PLANT")

        if sell >= max(harvest, expand, plant):
            return "ECONOMIC"

        if expand >= max(sell, harvest, plant):
            return "EXPANSION"

        if harvest >= max(sell, expand, plant):
            return "AGGRESSIVE"

        return "BALANCED"

    # ---------------------------------------------------------

    def is_aggressive(
        self,
    ) -> bool:

        return (
            self.strategy()
            == "AGGRESSIVE"
        )

    # ---------------------------------------------------------

    def is_economic(
        self,
    ) -> bool:

        return (
            self.strategy()
            == "ECONOMIC"
        )

    # ---------------------------------------------------------

    def is_expansion(
        self,
    ) -> bool:

        return (
            self.strategy()
            == "EXPANSION"
        )