"""
prediction_cache_manager.py

Prediction Cache Manager for the Kaggriculture AI Agent.

Caches inference results for repeated requests.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class PredictionCacheManager:
    """
    Stores cached prediction results.
    """

    def __init__(self):
        self._cache = {}

    # ---------------------------------------------------------

    def put(
        self,
        key: str,
        prediction,
    ):
        """
        Store a prediction.
        """

        self._cache[key] = prediction

    # ---------------------------------------------------------

    def get(
        self,
        key: str,
    ):
        """
        Retrieve a cached prediction.
        """

        return self._cache.get(key)

    # ---------------------------------------------------------

    def exists(
        self,
        key: str,
    ) -> bool:
        """
        Return True if cache entry exists.
        """

        return key in self._cache

    # ---------------------------------------------------------

    def remove(
        self,
        key: str,
    ):
        """
        Remove a cache entry.
        """

        self._cache.pop(key, None)

    # ---------------------------------------------------------

    def clear(self):
        """
        Clear the cache.
        """

        self._cache.clear()

    # ---------------------------------------------------------

    def count(self) -> int:
        """
        Return number of cached entries.
        """

        return len(self._cache)