"""
reward_shaping_engine.py

Reward Shaping Engine for the Kaggriculture AI Agent.

Provides intermediate rewards that guide the
agent toward long-term success instead of only
using the final game score.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class RewardShapingEngine:
    """
    Compute shaped rewards.
    """

    def reward(
        self,
        *,
        profit: float = 0.0,
        harvested: int = 0,
        watered: int = 0,
        animals_cared: int = 0,
        penalties: float = 0.0,
    ) -> float:
        """
        Return a shaped reward.
        """

        reward = 0.0

        reward += profit * 0.01
        reward += harvested * 5.0
        reward += watered * 1.0
        reward += animals_cared * 2.0
        reward -= penalties

        return reward

    # ---------------------------------------------------------

    def normalized_reward(
        self,
        reward: float,
        *,
        scale: float = 100.0,
    ) -> float:
        """
        Normalize reward.
        """

        return reward / scale

    # ---------------------------------------------------------

    def positive(
        self,
        reward: float,
    ) -> bool:
        """
        Return True if reward is positive.
        """

        return reward > 0