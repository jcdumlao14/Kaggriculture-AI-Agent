"""
decision_engine_v2.py

Decision Engine V2 for the Kaggriculture AI Agent.

Selects the best legal action using the
LegalActionGenerator and UnifiedActionEvaluator.

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
from src.multi_turn_planner import MultiTurnPlanner
from src.plan_evaluator import PlanEvaluator
from src.plan_comparator import PlanComparator
from src.plan_executor import PlanExecutor
from src.unified_action_evaluator import (
    UnifiedActionEvaluator,
)


class DecisionEngineV2:
    """
    Chooses the highest-scoring legal action.
    """

    def __init__(self):
        self.generator = LegalActionGenerator()
        self.scorer = ActionScoringEngine()      # Keep for backward compatibility
        self.filter = RuleBasedActionFilter()
        self.parser = ObservationParser()
        self.adapter = GameStateAdapter()
        self.search_controller = SearchController()
        self.dispatcher = SearchDispatcher()
        self.phase = GamePhaseCoordinator()
        self.market_engine = MarketDecisionEngine()

        self.multi_turn_planner = None
        self.plan_evaluator = PlanEvaluator()
        self.plan_comparator = PlanComparator()
        self.plan_executor = PlanExecutor()

        # New unified evaluator
        self.evaluator = UnifiedActionEvaluator()

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

        game_state = self.adapter.adapt(
            observation,
        )

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

        # Reserved for future phase-aware logic
        _ = game_phase

        market_score = self._market_score(
            game_state,
        )

        algorithm = self.search_controller.select_algorithm(
            turn=observation.get(
                "turn",
                0,
            ),
        )

        _ = self.dispatcher.dispatch(
            algorithm,
            game_state,
        )

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

            score = self.evaluator.evaluate(
                action["action"],
                game_state=game_state,
                market_score=market_score,
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
            key=lambda action: self.evaluator.evaluate(
                action["action"],
                game_state=game_state,
                market_score=market_score,
            ),
            reverse=True,
        )