"""
model_validator.py

Model Validator for the Kaggriculture AI Agent.

Validates models before deployment.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ModelValidator:
    """
    Validates registered models.
    """

    # ---------------------------------------------------------

    def has_checkpoint(self, model: dict) -> bool:
        """
        Check whether a checkpoint exists.
        """

        return bool(model.get("checkpoint"))

    # ---------------------------------------------------------

    def has_score(self, model: dict) -> bool:
        """
        Check whether a score exists.
        """

        return "score" in model

    # ---------------------------------------------------------

    def meets_threshold(
        self,
        model: dict,
        minimum_score: float,
    ) -> bool:
        """
        Check whether score satisfies threshold.
        """

        return (
            model.get("score", float("-inf"))
            >= minimum_score
        )

    # ---------------------------------------------------------

    def metadata_complete(
        self,
        metadata: dict,
    ) -> bool:
        """
        Check required metadata fields.
        """

        required = (
            "author",
            "algorithm",
            "dataset",
            "trained_on",
        )

        return all(
            metadata.get(field)
            for field in required
        )

    # ---------------------------------------------------------

    def ready_for_deployment(
        self,
        model: dict,
        metadata: dict,
        minimum_score: float,
    ) -> bool:
        """
        Determine deployment readiness.
        """

        return (
            self.has_checkpoint(model)
            and self.has_score(model)
            and self.meets_threshold(
                model,
                minimum_score,
            )
            and self.metadata_complete(
                metadata,
            )
        )