"""
rule_based_action_filter.py

Rule-Based Action Filter for the Kaggriculture AI Agent.

Filters candidate actions using simple game rules.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class RuleBasedActionFilter:
    """
    Removes invalid actions before scoring.
    """

    def filter_actions(
        self,
        actions,
        observation,
    ):
        """
        Return only valid actions.
        """

        money = observation.get("farm", {}).get("money", 0)

        filtered = []

        for action in actions:

            name = action["action"]

            if (
                name == "BUY"
                and money <= 0
            ):
                continue

            filtered.append(action)

        return filtered

    # ---------------------------------------------------------

    def count(
        self,
        actions,
        observation,
    ):
        """
        Number of remaining actions.
        """
        return len(
            self.filter_actions(
                actions,
                observation,
            )
        )

    # ---------------------------------------------------------

    def has_actions(
        self,
        actions,
        observation,
    ):
        """
        True if actions remain.
        """
        return (
            self.count(
                actions,
                observation,
            )
            > 0
        )