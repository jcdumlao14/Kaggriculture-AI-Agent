"""
observation_parser.py

Production Observation Parser for the Kaggriculture AI Agent.

Parses the official Kaggriculture observation into a
normalized game state used throughout the AI pipeline.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ObservationParser:
    """
    Parses the Kaggriculture observation.
    """

    # ---------------------------------------------------------

    def parse(
        self,
        observation: dict,
    ) -> dict:
        """
        Convert the raw Kaggriculture observation into
        a normalized state dictionary.

        This parser supports both:

        1. Legacy unit-test observations
        2. Official Kaggriculture observations
        """

        # -----------------------------------------------------
        # Legacy test observation support
        # -----------------------------------------------------

        if "farm" in observation:

            farm = observation.get("farm", {})

            return {
                # Original API
                "money": farm.get("money", 0),
                "tiles": farm.get("tiles", []),
                "inventory": farm.get("inventory", {}),
                "workers": farm.get("workers", []),
                "market": observation.get("market", {}),
                "opponent": observation.get("opponent", {}),

                # New API defaults
                "player": 0,
                "day": observation.get("day", 0),
                "hour": observation.get("hour", 0),
                "farmer": farm.get("farmer", [0, 0]),
                "hands": farm.get("workers", []),
                "unlocked_quadrants": [],
                "hires_today": 0,
                "town": {},
                "shed": farm.get("inventory", {}),
                "seeds": {},
                "inventories": [],
            }

        # -----------------------------------------------------
        # Official Kaggriculture observation
        # -----------------------------------------------------

        player = observation.get("player", 0)

        farms = observation.get("farms", [])

        if player < len(farms):
            farm = farms[player]
        else:
            farm = {}

        private = observation.get("private", {}) or {}

        return {
            # =================================================
            # Original API (backward compatibility)
            # =================================================

            "money": farm.get("money", 0),

            "tiles": farm.get("tiles", []),

            "inventory": private.get(
                "shed",
                {},
            ),

            "workers": farm.get(
                "hands",
                [],
            ),

            "market": observation.get(
                "market",
                {},
            ),

            "opponent": {},

            # =================================================
            # New Kaggriculture API
            # =================================================

            "player": player,

            "day": observation.get(
                "day",
                0,
            ),

            "hour": observation.get(
                "hour",
                0,
            ),

            "farmer": farm.get(
                "farmer",
                [0, 0],
            ),

            "hands": farm.get(
                "hands",
                [],
            ),

            "unlocked_quadrants": farm.get(
                "unlocked_quadrants",
                [],
            ),

            "hires_today": farm.get(
                "hires_today",
                0,
            ),

            "town": observation.get(
                "town",
                {},
            ),

            "shed": private.get(
                "shed",
                {},
            ),

            "seeds": private.get(
                "seeds",
                {},
            ),

            "inventories": private.get(
                "inventories",
                [],
            ),
        }

    # ---------------------------------------------------------

    def player_id(
        self,
        observation: dict,
    ) -> int:
        """
        Return player id.
        """
        return self.parse(observation)["player"]

    # ---------------------------------------------------------

    def money(
        self,
        observation: dict,
    ) -> int:
        """
        Return player money.
        """
        return self.parse(observation)["money"]

    # ---------------------------------------------------------

    def current_day(
        self,
        observation: dict,
    ) -> int:
        """
        Return current day.
        """
        return self.parse(observation)["day"]

    # ---------------------------------------------------------

    def current_hour(
        self,
        observation: dict,
    ) -> int:
        """
        Return current hour.
        """
        return self.parse(observation)["hour"]

    # ---------------------------------------------------------

    def market_prices(
        self,
        observation: dict,
    ) -> dict:
        """
        Return market prices.
        """
        return (
            self.parse(observation)["market"]
            .get("prices", {})
        )