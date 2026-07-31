"""
state.py

Persistent state for the Kaggriculture AI Agent.

Stores information across turns that is useful for
long-term decision making.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AgentState:
    """
    Stores persistent information across turns.
    """

    turn: int = 0
    day: int = 0

    money: float = 0.0

    previous_money: float = 0.0

    previous_prices: dict = field(default_factory=dict)

    harvested: int = 0

    planted: int = 0

    animals: int = 0

    fertilizer_used: int = 0

    land_owned: int = 1

    workers: int = 0


class StateManager:

    def __init__(self):

        self.state = AgentState()

    # --------------------------------------------------------

    def update(self, parser):

        """
        Update state from latest observation.
        """

        self.state.turn = parser.step

        self.state.day = parser.day

        self.state.previous_money = self.state.money

        self.state.money = parser.money

        self.state.previous_prices = parser.market_prices.copy()

    # --------------------------------------------------------

    def profit(self):

        return self.state.money - self.state.previous_money

    # --------------------------------------------------------

    def harvest(self):

        self.state.harvested += 1

    # --------------------------------------------------------

    def plant(self):

        self.state.planted += 1

    # --------------------------------------------------------

    def add_worker(self):

        self.state.workers += 1

    # --------------------------------------------------------

    def buy_land(self):

        self.state.land_owned += 1

    # --------------------------------------------------------

    def summary(self):

        return {

            "Turn": self.state.turn,

            "Day": self.state.day,

            "Money": self.state.money,

            "Profit": self.profit(),

            "Harvested": self.state.harvested,

            "Planted": self.state.planted,

            "Workers": self.state.workers,

            "Land": self.state.land_owned,

        }