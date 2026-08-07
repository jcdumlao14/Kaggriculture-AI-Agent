"""
unified_action_evaluator.py

Unified Action Evaluator for the Kaggriculture AI Agent.

Combines action scoring, opportunity assessment,
risk assessment, decision learning, adaptive strategy,
and decision fusion into one evaluation pipeline.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.action_scoring_engine import ActionScoringEngine
from src.decision_fusion_engine import DecisionFusionEngine
from src.opportunity_assessment_engine import (
    OpportunityAssessmentEngine,
)
from src.risk_assessment_engine import (
    RiskAssessmentEngine,
)
from src.decision_learning_engine import (
    DecisionLearningEngine,
)
from src.adaptive_strategy_engine import (
    AdaptiveStrategyEngine,
)
from src.action_priority_engine import (
    ActionPriorityEngine,
)


class UnifiedActionEvaluator:
    """
    Evaluate candidate actions using multiple
    decision signals.
    """

    def __init__(self):

        self.action_scorer = ActionScoringEngine()
        self.opportunity = OpportunityAssessmentEngine()
        self.risk = RiskAssessmentEngine()
        self.fusion = DecisionFusionEngine()
        self.learning = DecisionLearningEngine()
        self.strategy = AdaptiveStrategyEngine()
        self.priority = ActionPriorityEngine()

    # ---------------------------------------------------------

    def evaluate(
        self,
        action: str,
        *,
        game_state: dict | None = None,
        farm_score: float = 0.0,
        crop_profit: float = 0.0,
        animal_profit: float = 0.0,
        market_score: float = 0.0,
        strategy_score: float = 0.0,
        opponent_strategy: str = "UNKNOWN",
    ) -> float:
        """
        Return the final fused score for an action.
        """

        action_score = self.action_scorer.score(
            action=action,
            farm_score=farm_score,
            crop_profit=crop_profit,
            animal_profit=animal_profit,
            market_score=0.0,
            game_state=game_state,
        )

        opportunity_score = self.opportunity.value(
            action,
        )

        risk_score = self.risk.risk(
            action,
        )

        learning_bonus = self.learning.adjustment(
            action,
        )

        adaptive_bonus = self.strategy.adjustment(
            action,
            opponent_strategy,
        )

        final_score = self.fusion.fuse(
            action_score=action_score,
            opportunity_score=opportunity_score,
            market_score=market_score,
            strategy_score=strategy_score,
            risk_score=risk_score,
        )

        return float(
            final_score
            + learning_bonus
            + adaptive_bonus
        )

    # ---------------------------------------------------------

    def evaluate_details(
        self,
        action: str,
        *,
        game_state: dict | None = None,
        market_score: float = 0.0,
        strategy_score: float = 0.0,
        opponent_strategy: str = "UNKNOWN",
    ) -> dict:
        """
        Return the individual scoring components.
        """

        action_score = self.action_scorer.score(
            action=action,
            game_state=game_state,
        )

        opportunity_score = self.opportunity.value(
            action,
        )

        risk_score = self.risk.risk(
            action,
        )

        learning_bonus = self.learning.adjustment(
            action,
        )

        adaptive_bonus = self.strategy.adjustment(
            action,
            opponent_strategy,
        )

        final_score = (
            self.fusion.fuse(
                action_score=action_score,
                opportunity_score=opportunity_score,
                market_score=market_score,
                strategy_score=strategy_score,
                risk_score=risk_score,
            )
            + learning_bonus
            + adaptive_bonus
        )

        return {
            "action": action.upper(),
            "action_score": float(action_score),
            "opportunity_score": float(opportunity_score),
            "risk_score": float(risk_score),
            "market_score": float(market_score),
            "strategy_score": float(strategy_score),
            "learning_bonus": float(learning_bonus),
            "adaptive_bonus": float(adaptive_bonus),
            "final_score": float(final_score),
        }

    # ---------------------------------------------------------

    def rank_actions(
        self,
        actions: list[str],
        *,
        game_state: dict | None = None,
        market_score: float = 0.0,
        strategy_score: float = 0.0,
        opponent_strategy: str = "UNKNOWN",
    ) -> list[tuple[str, float]]:
        """
        Rank actions from highest to lowest score.
        """

        scores = {
            action: self.evaluate(
                action,
                game_state=game_state,
                market_score=market_score,
                strategy_score=strategy_score,
                opponent_strategy=opponent_strategy,
            )
            for action in actions
        }

        return self.fusion.rank(
            scores,
        )

    # ---------------------------------------------------------

    def best_action(
        self,
        actions: list[str],
        *,
        game_state: dict | None = None,
        market_score: float = 0.0,
        strategy_score: float = 0.0,
        opponent_strategy: str = "UNKNOWN",
    ) -> str | None:
        """
        Return the highest-scoring action.
        """

        if not actions:
            return None

        ranking = self.rank_actions(
            actions,
            game_state=game_state,
            market_score=market_score,
            strategy_score=strategy_score,
            opponent_strategy=opponent_strategy,
        )

        return ranking[0][0]

    # ---------------------------------------------------------

    def record_outcome(
        self,
        action: str,
        reward: float,
    ) -> None:
        """
        Store the observed reward for an action.
        """

        self.learning.record(
            action,
            reward,
        )

    # ---------------------------------------------------------

    def learned_reward(
        self,
        action: str,
    ) -> float:
        """
        Return the learned average reward.
        """

        return self.learning.average_reward(
            action,
        )