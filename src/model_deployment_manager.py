"""
model_deployment_manager.py

Model Deployment Manager for the Kaggriculture AI Agent.

Manages model deployment lifecycle.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ModelDeploymentManager:
    """
    Manages deployed models.
    """

    def __init__(self):
        self._deployments = {}

    # ---------------------------------------------------------

    def deploy(
        self,
        model_name: str,
        version: str,
    ):
        """
        Deploy a model version.
        """

        self._deployments[model_name] = {
            "version": version,
            "status": "deployed",
        }

    # ---------------------------------------------------------

    def get(
        self,
        model_name: str,
    ):
        """
        Return deployment information.
        """

        return self._deployments.get(model_name)

    # ---------------------------------------------------------

    def status(
        self,
        model_name: str,
    ):
        """
        Return deployment status.
        """

        deployment = self.get(model_name)

        if deployment is None:
            return None

        return deployment["status"]

    # ---------------------------------------------------------

    def rollback(
        self,
        model_name: str,
        version: str,
    ):
        """
        Roll back to a previous version.
        """

        if model_name in self._deployments:
            self._deployments[model_name]["version"] = version

    # ---------------------------------------------------------

    def undeploy(
        self,
        model_name: str,
    ):
        """
        Remove a deployment.
        """

        self._deployments.pop(model_name, None)

    # ---------------------------------------------------------

    def is_deployed(
        self,
        model_name: str,
    ) -> bool:
        """
        Return True if model is deployed.
        """

        return model_name in self._deployments