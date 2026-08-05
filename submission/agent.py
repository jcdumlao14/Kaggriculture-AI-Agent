"""
submission/agent.py

Production Kaggriculture competition agent.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.observation_parser import ObservationParser
from src.game_state_adapter import GameStateAdapter
from src.farmer_action_generator import FarmerActionGenerator
from src.market_action_generator import MarketActionGenerator
from src.action_composer import ActionComposer


class CompetitionAgent:
    """
    Main competition agent.
    """

    def __init__(self):

        self.parser = ObservationParser()
        self.adapter = GameStateAdapter()

        self.farmer_generator = FarmerActionGenerator()
        self.market_generator = MarketActionGenerator()

        self.composer = ActionComposer()

    # ---------------------------------------------------------

    def act(
        self,
        observation: dict,
    ) -> dict:
        """
        Produce a Kaggriculture action.
        """

        # Normalize state

        state = self.adapter.adapt(observation)

        # Generate actions

        farmer_actions = self.farmer_generator.generate(
            state,
        )

        market_actions = self.market_generator.generate(
            state,
        )

        # Compose

        return self.composer.compose(
            farmer_actions=farmer_actions,
            market_actions=market_actions,
        )


_AGENT = CompetitionAgent()


def agent(observation: dict):
    """
    Kaggle entry point.
    """

    return _AGENT.act(observation)