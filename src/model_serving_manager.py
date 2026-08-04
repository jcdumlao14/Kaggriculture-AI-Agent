"""
model_serving_manager.py

Model Serving Manager for the Kaggriculture AI Agent.

Simulates online model serving.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ModelServingManager:
    """
    Manages serving endpoints.
    """

    def __init__(self):
        self._endpoints = {}

    # ---------------------------------------------------------

    def register(
        self,
        endpoint: str,
        model_name: str,
        version: str,
    ):
        """
        Register a serving endpoint.
        """

        self._endpoints[endpoint] = {
            "model": model_name,
            "version": version,
            "enabled": True,
            "requests": 0,
        }

    # ---------------------------------------------------------

    def predict(
        self,
        endpoint: str,
        payload,
    ):
        """
        Simulate an inference request.
        """

        info = self._endpoints.get(endpoint)

        if info is None:
            return None

        if not info["enabled"]:
            return None

        info["requests"] += 1

        return {
            "prediction": payload,
            "model": info["model"],
            "version": info["version"],
        }

    # ---------------------------------------------------------

    def enable(
        self,
        endpoint: str,
    ):
        """
        Enable an endpoint.
        """

        if endpoint in self._endpoints:
            self._endpoints[endpoint]["enabled"] = True

    # ---------------------------------------------------------

    def disable(
        self,
        endpoint: str,
    ):
        """
        Disable an endpoint.
        """

        if endpoint in self._endpoints:
            self._endpoints[endpoint]["enabled"] = False

    # ---------------------------------------------------------

    def request_count(
        self,
        endpoint: str,
    ) -> int:
        """
        Return number of served requests.
        """

        endpoint_info = self._endpoints.get(endpoint)

        if endpoint_info is None:
            return 0

        return endpoint_info["requests"]

    # ---------------------------------------------------------

    def exists(
        self,
        endpoint: str,
    ) -> bool:
        """
        Return True if endpoint exists.
        """

        return endpoint in self._endpoints