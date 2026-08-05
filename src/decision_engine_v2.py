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
        

    # ---------------------------------------------------------

    def choose_action(
        self,
        observation: dict,
    ):
        """
        Return the best legal action.
        """

        # Parse and normalize the observation
        state = self.parser.parse(observation)
        game_state = self.adapter.adapt(observation)

        game_phase = self.phase.game_phase(
            day=game_state.get("day", 0),
            hour=game_state.get("hour", 0),
        )

        # Select the search algorithm (used in future phases)
        algorithm = self.search_controller.select_algorithm(
            turn=observation.get("turn", 0)
        )

        actions = self.filter.filter_actions(
            self.generator.generate(observation),
            observation,
        )

        algorithm = self.search_controller.select_algorithm(
            turn=observation.get("turn", 0)
        )

        selected = self.dispatcher.dispatch(
            algorithm,
            game_state,
        )
        
        if not actions:
            return None

        best_action = None
        best_score = float("-inf")

        for action in actions:

            score = self.scorer.score(
                action=action["action"],
            )

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

        # Parse and normalize the observation
        state = self.parser.parse(observation)
        game_state = self.adapter.adapt(observation)

        # Select the search algorithm (used in future phases)
        algorithm = self.search_controller.select_algorithm(
            turn=observation.get("turn", 0)
        )

        actions = self.filter.filter_actions(
            self.generator.generate(observation),
            observation,
        )

        return sorted(
            actions,
            key=lambda action: self.scorer.score(
                action=action["action"],
            ),
            reverse=True,
        )