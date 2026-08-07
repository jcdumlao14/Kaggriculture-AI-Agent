"""
state_encoding_engine.py

State Encoding Engine for the Kaggriculture AI Agent.

Encodes game states into deterministic
representations for caching, search,
learning, and replay.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

import json
from hashlib import sha256


class StateEncodingEngine:
    """
    Encode game states.
    """

    def encode(
        self,
        game_state: dict,
    ) -> str:
        """
        Return a deterministic JSON encoding.
        """

        return json.dumps(
            game_state,
            sort_keys=True,
            separators=(",", ":"),
        )

    # ---------------------------------------------------------

    def hash(
        self,
        game_state: dict,
    ) -> str:
        """
        Return a SHA-256 hash of the state.
        """

        encoded = self.encode(game_state)

        return sha256(
            encoded.encode("utf-8")
        ).hexdigest()

    # ---------------------------------------------------------

    def identical(
        self,
        state_a: dict,
        state_b: dict,
    ) -> bool:
        """
        Compare two states.
        """

        return (
            self.hash(state_a)
            == self.hash(state_b)
        )