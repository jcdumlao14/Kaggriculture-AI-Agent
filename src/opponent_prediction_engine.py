"""
opponent_prediction_engine.py

Opponent Prediction Engine for the Kaggriculture AI Agent.

Predicts the opponent's next likely action using
the learned opponent model.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from src.opponent_model import OpponentModel


class OpponentPredictionEngine:
    """
    Predict opponent behavior.
    """

    def __init__(
        self,
        model: OpponentModel,
    ):

        self.model = model

    # ---------------------------------------------------------

    def predict(self) -> str | None:
        """
        Return the most likely next action.
        """

        return self.model.most_common()

    # ---------------------------------------------------------

    def confidence(self) -> float:
        """
        Return confidence of the prediction.
        """

        total = self.model.total_actions()

        if total == 0:
            return 0.0

        action = self.model.most_common()

        return (
            self.model.frequency(action)
            / total
        )

    # ---------------------------------------------------------

    def has_prediction(self) -> bool:
        """
        Return True if a prediction exists.
        """

        return (
            self.model.most_common()
            is not None
        )