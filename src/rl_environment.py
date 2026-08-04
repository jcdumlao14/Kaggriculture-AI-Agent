"""
rl_environment.py

Reinforcement Learning Environment for the
Kaggriculture AI Agent.

Provides a lightweight environment interface
compatible with future RL algorithms.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class RLEnvironment:
    """
    Simple reinforcement learning environment.
    """

    def __init__(self, max_steps: int = 30):
        self.max_steps = max_steps
        self.current_step = 0
        self.total_reward = 0.0

    # ---------------------------------------------------------

    def reset(self):
        """
        Reset the environment.
        """
        self.current_step = 0
        self.total_reward = 0.0

        return self.state()

    # ---------------------------------------------------------

    def step(self, action):
        """
        Execute one action.

        Returns:
            next_state, reward, done
        """

        self.current_step += 1

        # Placeholder reward logic
        reward = 1.0

        self.total_reward += reward

        done = self.current_step >= self.max_steps

        return self.state(), reward, done

    # ---------------------------------------------------------

    def state(self):
        """
        Return current environment state.
        """

        return {
            "step": self.current_step,
            "reward": self.total_reward,
        }

    # ---------------------------------------------------------

    def is_done(self):
        """
        Check if episode finished.
        """

        return self.current_step >= self.max_steps