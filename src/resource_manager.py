"""
resource_manager.py

Resource Manager for the Kaggriculture AI Agent.

Tracks allocation and release of shared resources.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceManager:
    """
    Manages named resources and their allocation state.
    """

    def __init__(self):
        self._resources = {}

    # ---------------------------------------------------------

    def register(self, name: str, resource):
        """
        Register a resource.
        """
        self._resources[name] = {
            "resource": resource,
            "allocated": False,
        }

    # ---------------------------------------------------------

    def allocate(self, name: str):
        """
        Allocate a resource.

        Returns None if unavailable.
        """
        item = self._resources.get(name)

        if item is None:
            return None

        if item["allocated"]:
            return None

        item["allocated"] = True

        return item["resource"]

    # ---------------------------------------------------------

    def release(self, name: str):
        """
        Release a resource.
        """
        if name in self._resources:
            self._resources[name]["allocated"] = False

    # ---------------------------------------------------------

    def is_allocated(self, name: str) -> bool:
        """
        Return allocation status.
        """
        if name not in self._resources:
            return False

        return self._resources[name]["allocated"]

    # ---------------------------------------------------------

    def remove(self, name: str):
        """
        Remove a resource.
        """
        self._resources.pop(name, None)

    # ---------------------------------------------------------

    def count(self) -> int:
        """
        Return registered resource count.
        """
        return len(self._resources)

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove every resource.
        """
        self._resources.clear()