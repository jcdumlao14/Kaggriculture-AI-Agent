"""
opening_book.py

Opening Book for the Kaggriculture AI Agent.

Provides predefined opening strategies for
the first days of the farming season.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class OpeningBook:
    """
    Opening strategy helper.
    """

    def __init__(self):
        self.book = {
            1: "PLANT_WHEAT",
            2: "EXPAND_FIELD",
            3: "PLANT_CARROT",
            4: "WATER",
            5: "BUY_SEEDS",
        }

    # ---------------------------------------------------------

    def has_move(self, day: int) -> bool:
        """
        Return True if an opening move exists.
        """
        return day in self.book

    # ---------------------------------------------------------

    def move(self, day: int):
        """
        Return the opening move for the given day.
        """
        return self.book.get(day)

    # ---------------------------------------------------------

    def add_move(self, day: int, action: str):
        """
        Add or update an opening move.
        """
        self.book[day] = action

    # ---------------------------------------------------------

    def remove_move(self, day: int):
        """
        Remove an opening move.
        """
        self.book.pop(day, None)

    # ---------------------------------------------------------

    def size(self) -> int:
        """
        Number of opening moves.
        """
        return len(self.book)