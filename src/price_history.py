"""
price_history.py

Price History Tracker for the Kaggriculture AI Agent.

Tracks historical market prices and provides
basic trend analysis.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from collections import defaultdict, deque


class PriceHistory:
    """
    Stores recent prices for every product.
    """

    def __init__(
        self,
        max_history: int = 10,
    ):
        self.max_history = max_history

        self.history = defaultdict(
            lambda: deque(maxlen=max_history)
        )

    # ---------------------------------------------------------

    def update(
        self,
        product: str,
        price: float,
    ) -> None:
        """
        Store the latest market price.
        """

        self.history[
            product.upper()
        ].append(float(price))

    # ---------------------------------------------------------

    def latest(
        self,
        product: str,
    ) -> float:

        prices = self.history.get(
            product.upper(),
        )

        if not prices:
            return 0.0

        return prices[-1]

    # ---------------------------------------------------------

    def average(
        self,
        product: str,
    ) -> float:

        prices = self.history.get(
            product.upper(),
        )

        if not prices:
            return 0.0

        return sum(prices) / len(prices)

    # ---------------------------------------------------------

    def trend(
        self,
        product: str,
    ) -> str:

        prices = self.history.get(
            product.upper(),
        )

        if prices is None or len(prices) < 2:
            return "STABLE"

        if prices[-1] > prices[0]:
            return "UP"

        if prices[-1] < prices[0]:
            return "DOWN"

        return "STABLE"

    # ---------------------------------------------------------

    def clear(self):

        self.history.clear()