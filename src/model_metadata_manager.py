"""
model_metadata_manager.py

Model Metadata Manager for the Kaggriculture AI Agent.

Stores metadata associated with registered model versions.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ModelMetadataManager:
    """
    Stores metadata for model versions.
    """

    def __init__(self):
        self._metadata = {}

    # ---------------------------------------------------------

    def register(
        self,
        model_name: str,
        version: str,
        author: str,
        algorithm: str,
        dataset: str,
        trained_on: str,
        tags=None,
    ):
        """
        Register metadata.
        """

        if tags is None:
            tags = []

        self._metadata.setdefault(model_name, {})

        self._metadata[model_name][version] = {
            "author": author,
            "algorithm": algorithm,
            "dataset": dataset,
            "trained_on": trained_on,
            "tags": list(tags),
        }

    # ---------------------------------------------------------

    def get(
        self,
        model_name: str,
        version: str,
    ):
        """
        Retrieve metadata.
        """

        return (
            self._metadata
            .get(model_name, {})
            .get(version)
        )

    # ---------------------------------------------------------

    def exists(
        self,
        model_name: str,
        version: str,
    ) -> bool:
        """
        Check whether metadata exists.
        """

        return (
            version in
            self._metadata.get(model_name, {})
        )

    # ---------------------------------------------------------

    def remove(
        self,
        model_name: str,
        version: str,
    ):
        """
        Remove metadata.
        """

        if model_name in self._metadata:
            self._metadata[model_name].pop(
                version,
                None,
            )

    # ---------------------------------------------------------

    def count(
        self,
        model_name: str,
    ):
        """
        Return metadata count.
        """

        return len(
            self._metadata.get(
                model_name,
                {},
            )
        )