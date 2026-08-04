"""
resource_pool.py

Resource Pool for the Kaggriculture AI Agent.

Provides reusable resource allocation.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from collections import deque


class ResourcePool:
    """
    Manages reusable resources.
    """

    def __init__(self):
        self._resources = deque()

    # ---------------------------------------------------------

    def add(self, resource):
        """
        Add a resource to the pool.
        """
        self._resources.append(resource)

    # ---------------------------------------------------------

    def acquire(self):
        """
        Acquire the next available resource.
        """
        if not self._resources:
            return None

        return self._resources.popleft()

    # ---------------------------------------------------------

    def release(self, resource):
        """
        Return a resource to the pool.
        """
        self._resources.append(resource)

    # ---------------------------------------------------------

    def available(self):
        """
        Return the number of available resources.
        """
        return len(self._resources)

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove every resource.
        """
        self._resources.clear()