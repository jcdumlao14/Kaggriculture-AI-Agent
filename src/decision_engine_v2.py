"""
decision_engine_v2.py

Decision Engine V2 for the Kaggriculture AI Agent.

Selects the best legal action using the
LegalActionGenerator and ActionScoringEngine.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.legal_action_generator import LegalActionGenerator
from src.action_scoring_engine import ActionScoringEngine
from src.rule_based_action_filter import RuleBasedActionFilter
from src.observation_parser import ObservationParser
from src.game_state_adapter import GameStateAdapter
from src.search_controller import SearchController
from src.search_dispatcher import SearchDispatcher
from src.game_phase_coordinator import GamePhaseCoordinator
from src.market_decision_engine import MarketDecisionEngine


class DecisionEngineV2:
    """
    Chooses the highest-scoring legal action.
    """

    def __init__(self):
        self.generator = LegalActionGenerator()
        self.scorer = ActionScoringEngine()
        self.filter = RuleBasedActionFilter()
        self.parser = ObservationParser()
        self.adapter = GameStateAdapter()
        self.search_controller = SearchController()
        self.dispatcher = SearchDispatcher()
        self.phase = GamePhaseCoordinator()
        self.market_engine = MarketDecisionEngine()

    # ---------------------------------------------------------

    def _market_score(
        self,
        game_state: dict,
    ) -> float:
        """
        Compute a market bonus based on current prices.
        """

        market = game_state.get(
            "market",
            {},
        )

        prices = market.get(
            "prices",
            {},
        )

        if not prices:
            return 0.0

        average_price = (
            sum(prices.values())
            / len(prices)
        )

        highest_price = max(
            prices.values()
        )

        if self.market_engine.should_sell(
            current_price=highest_price,
            average_price=average_price,
        ):
            return 20.0

        return 0.0

    # ---------------------------------------------------------

    def choose_action(
        self,
        observation: dict,
    ):
        """
        Return the best legal action.
        """

        # Normalize observation
        game_state = self.adapter.adapt(
            observation,
        )

        # Current game phase
        game_phase = self.phase.game_phase(
            day=game_state.get(
                "day",
                0,
            ),
            hour=game_state.get(
                "hour",
                0,
            ),
        )

        # Currently reserved for future phase-aware scoring
        _ = game_phase

        # Market evaluation
        market_score = self._market_score(
            game_state,
        )

        # Select search algorithm
        algorithm = self.search_controller.select_algorithm(
            turn=observation.get(
                "turn",
                0,
            ),
        )

        # Dispatch search (future integration)
        _ = self.dispatcher.dispatch(
            algorithm,
            game_state,
        )

        # Generate legal actions
        actions = self.filter.filter_actions(
            self.generator.generate(
                observation,
            ),
            observation,
        )

        if not actions:
            return None

        best_action = None
        best_score = float("-inf")

        for action in actions:

            score = self.scorer.score(
                action=action["action"],
                market_score=market_score,
                game_state=game_state,
            )

            #
            # Future:
            # Season-aware adjustments
            # Opponent-aware adjustments
            # Search evaluation bonus
            #

            if score > best_score:
                best_score = score
                best_action = action

        return best_action

    # ---------------------------------------------------------

    def choose_actions(
        self,
        observation: dict,
    ):
        """
        Return all legal actions sorted by score.
        """

        game_state = self.adapter.adapt(
            observation,
        )

        market_score = self._market_score(
            game_state,
        )

        actions = self.filter.filter_actions(
            self.generator.generate(
                observation,
            ),
            observation,
        )

        return sorted(
            actions,
            key=lambda action: self.scorer.score(
                action=action["action"],
                market_score=market_score,
                game_state=game_state,
            ),
            reverse=True,
        )