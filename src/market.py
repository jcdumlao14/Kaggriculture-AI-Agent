"""
market.py

Market analysis module.

Responsible for analyzing dynamic prices and deciding
when products should be sold.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MarketItem:
    name: str
    inventory: int
    price: int
    base_price: int


class Market:

    def __init__(self, parser):

        self.parser = parser

        self.base_prices = {

            "WHEAT": 25,
            "CARROT": 35,
            "TOMATO": 60,
            "STRAWBERRY": 120,
            "MELON": 250,

            "EGG": 50,
            "MILK": 160,
            "WOOL": 200,

            "FERTILIZER": 100,
        }

    # ---------------------------------------------------------

    def items(self):

        inventory = self.parser.market_inventory
        prices = self.parser.market_prices

        results = []

        for product, price in prices.items():

            results.append(

                MarketItem(
                    name=product,
                    inventory=inventory.get(product, 0),
                    price=price,
                    base_price=self.base_prices.get(product, price),
                )

            )

        return results

    # ---------------------------------------------------------

    def best_price(self):

        """
        Highest market price right now.
        """

        return max(
            self.items(),
            key=lambda x: x.price,
        )

    # ---------------------------------------------------------

    def cheapest(self):

        """
        Lowest market price.
        """

        return min(
            self.items(),
            key=lambda x: x.price,
        )

    # ---------------------------------------------------------

    def overpriced(self):

        """
        Products above their base value.
        """

        return [

            item

            for item in self.items()

            if item.price > item.base_price

        ]

    # ---------------------------------------------------------

    def underpriced(self):

        """
        Products below base value.
        """

        return [

            item

            for item in self.items()

            if item.price < item.base_price

        ]

    # ---------------------------------------------------------

    def should_sell(self, product):

        """
        Decide if current price is good enough.
        """

        price = self.parser.market_prices.get(product)

        base = self.base_prices.get(product)

        if price is None:
            return False

        return price >= base

    # ---------------------------------------------------------

    def summary(self):

        report = {}

        for item in self.items():

            report[item.name] = {

                "Price": item.price,
                "Inventory": item.inventory,
                "Above Base": item.price > item.base_price,

            }

        return report