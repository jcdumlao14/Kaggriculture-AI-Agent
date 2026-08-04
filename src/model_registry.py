"""
model_registry.py

Model Registry for the Kaggriculture AI Agent.

Stores and manages trained model versions.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ModelRegistry:
    """
    Registry of trained models.
    """

    def __init__(self):
        self._models = {}

    # ---------------------------------------------------------

    def register(
        self,
        name: str,
        score: float,
        checkpoint: str,
    ):
        """
        Register or update a model.
        """

        self._models[name] = {
            "score": score,
            "checkpoint": checkpoint,
        }

    # ---------------------------------------------------------

    def get(self, name: str):
        """
        Retrieve a registered model.
        """

        return self._models.get(name)

    # ---------------------------------------------------------

    def exists(self, name: str) -> bool:
        """
        Check whether a model exists.
        """

        return name in self._models

    # ---------------------------------------------------------

    def remove(self, name: str):
        """
        Remove a registered model.
        """

        self._models.pop(name, None)

    # ---------------------------------------------------------

    def best_model(self):
        """
        Return the highest-scoring model name.
        """

        if not self._models:
            return None

        return max(
            self._models.items(),
            key=lambda item: item[1]["score"],
        )[0]

    # ---------------------------------------------------------

    def list_models(self):
        """
        Return a copy of all registered models.
        """

        return dict(self._models)

    # ---------------------------------------------------------

    def count(self) -> int:
        """
        Return number of registered models.
        """

        return len(self._models)

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove every registered model.
        """

        self._models.clear()