"""
request_rate_limiter.py

Request Rate Limiter for the Kaggriculture AI Agent.

Tracks and limits client requests.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class RequestRateLimiter:
    """
    Simple request rate limiter.
    """

    def __init__(self, limit: int = 10):
        self.limit = limit
        self._requests = {}

    # ---------------------------------------------------------

    def allow(self, client: str) -> bool:
        """
        Check whether a request is allowed.
        """

        count = self._requests.get(client, 0)

        if count >= self.limit:
            return False

        self._requests[client] = count + 1

        return True

    # ---------------------------------------------------------

    def request_count(
        self,
        client: str,
    ) -> int:
        """
        Return number of requests.
        """

        return self._requests.get(client, 0)

    # ---------------------------------------------------------

    def reset(
        self,
        client: str,
    ):
        """
        Reset a client's request count.
        """

        self._requests[client] = 0

    # ---------------------------------------------------------

    def remove(
        self,
        client: str,
    ):
        """
        Remove a client.
        """

        self._requests.pop(client, None)

    # ---------------------------------------------------------

    def exists(
        self,
        client: str,
    ) -> bool:
        """
        Return True if client is tracked.
        """

        return client in self._requests