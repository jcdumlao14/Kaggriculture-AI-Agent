"""
task_scoring.py

Dynamic task scoring for the Kaggriculture AI Agent.

Assigns adaptive scores to planner tasks based on
game state and economic conditions.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class TaskScoring:
    """
    Score planner tasks.
    """

    def __init__(
        self,
        season_strategy,
        profitability,
        money_manager,
        inventory_strategy,
    ):
        self.season = season_strategy
        self.profit = profitability
        self.money = money_manager
        self.inventory = inventory_strategy

    # ---------------------------------------------------------
    # Harvest
    # ---------------------------------------------------------

    def harvest_score(self) -> float:

        score = 100.0

        if self.season.remaining_days() <= 2:
            score += 25

        return score

    # ---------------------------------------------------------
    # Plant
    # ---------------------------------------------------------

    def plant_score(self, crop: str) -> float:

        score = self.profit.profit(crop)

        if self.season.remaining_days() <= 3:
            score *= 0.25

        return score

    # ---------------------------------------------------------
    # Sell
    # ---------------------------------------------------------

    def sell_score(self, product: str) -> float:

        score = 50.0

        if self.inventory.should_sell(product):
            score += 25

        if self.money.should_save():
            score += 15

        return score

    # ---------------------------------------------------------
    # Buy
    # ---------------------------------------------------------

    def buy_score(self, cost: int) -> float:

        if not self.money.can_afford(cost):
            return 0.0

        return 40.0