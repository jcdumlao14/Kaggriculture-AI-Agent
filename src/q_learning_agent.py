"""
q_learning_agent.py

Q-Learning Agent for the Kaggriculture AI Agent.

Learns optimal action values using the Bellman equation.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.q_table import QTable


class QLearningAgent:
    """
    Basic Q-learning implementation.
    """

    def __init__(
        self,
        learning_rate: float = 0.1,
        discount: float = 0.9,
    ):
        self.alpha = learning_rate
        self.gamma = discount
        self.q = QTable()

    # ---------------------------------------------------------

    def value(self, state, action):
        """
        Return Q-value.
        """
        return self.q.get(state, action)

    # ---------------------------------------------------------

    def best_action(self, state):
        """
        Return the best learned action.
        """
        return self.q.best_action(state)

    # ---------------------------------------------------------

    def learn(
        self,
        state,
        action,
        reward,
        next_state,
        next_actions,
    ):
        """
        Apply the Bellman update.
        """

        current = self.q.get(state, action)

        if next_actions:
            future = max(
                self.q.get(next_state, a)
                for a in next_actions
            )
        else:
            future = 0.0

        updated = current + self.alpha * (
            reward + self.gamma * future - current
        )

        self.q.update(
            state,
            action,
            updated,
        )

        return updated

    # ---------------------------------------------------------

    def reset(self):
        """
        Clear learned knowledge.
        """
        self.q.clear()