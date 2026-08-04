"""
training_loop.py

Training Loop for the Kaggriculture AI Agent.

Coordinates reinforcement learning episodes.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.episode_manager import EpisodeManager


class TrainingLoop:
    """
    Simple RL training loop.
    """

    def __init__(self):
        self.manager = EpisodeManager()

    # ---------------------------------------------------------

    def run_episode(self, rewards):
        """
        Execute one training episode.

        Parameters
        ----------
        rewards : iterable[float]
            Sequence of rewards received during the episode.
        """

        self.manager.start_episode()

        for reward in rewards:
            self.manager.step()
            self.manager.add_reward(reward)

        self.manager.finish()

        return self.manager.summary()

    # ---------------------------------------------------------

    def run(self, episodes):
        """
        Execute multiple episodes.

        Parameters
        ----------
        episodes : iterable
            Iterable containing reward sequences.

        Returns
        -------
        list[dict]
            Episode summaries.
        """

        history = []

        for rewards in episodes:
            history.append(
                self.run_episode(rewards)
            )

        return history