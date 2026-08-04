"""
model_version_manager.py

Model Version Manager for the Kaggriculture AI Agent.

Manages multiple versions of registered models.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ModelVersionManager:
    """
    Stores multiple versions of models.
    """

    def __init__(self):
        self._versions = {}

    # ---------------------------------------------------------

    def register(
        self,
        model_name: str,
        version: str,
        score: float,
        checkpoint: str,
    ):
        """
        Register a new model version.
        """

        self._versions.setdefault(model_name, {})

        self._versions[model_name][version] = {
            "score": score,
            "checkpoint": checkpoint,
        }

    # ---------------------------------------------------------

    def get(
        self,
        model_name: str,
        version: str,
    ):
        """
        Retrieve a model version.
        """

        return self._versions.get(
            model_name,
            {},
        ).get(version)

    # ---------------------------------------------------------

    def latest(
        self,
        model_name: str,
    ):
        """
        Return the latest registered version.
        """

        versions = self._versions.get(model_name)

        if not versions:
            return None

        return sorted(versions.keys())[-1]

    # ---------------------------------------------------------

    def list_versions(
        self,
        model_name: str,
    ):
        """
        Return all versions.
        """

        return sorted(
            self._versions.get(
                model_name,
                {},
            ).keys()
        )

    # ---------------------------------------------------------

    def remove(
        self,
        model_name: str,
        version: str,
    ):
        """
        Remove a version.
        """

        if model_name in self._versions:
            self._versions[model_name].pop(
                version,
                None,
            )

    # ---------------------------------------------------------

    def count(
        self,
        model_name: str,
    ):
        """
        Return number of versions.
        """

        return len(
            self._versions.get(
                model_name,
                {},
            )
        )