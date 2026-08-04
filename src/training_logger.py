"""
training_logger.py

Training Logger for the Kaggriculture AI Agent.

Stores training metrics for each episode.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

import json
from datetime import datetime, UTC
from pathlib import Path


class TrainingLogger:
    """
    Logs training episodes to a JSON Lines file.
    """

    def __init__(self, filename: str = "training_log.jsonl"):
        self.path = Path(filename)

    # ---------------------------------------------------------

    def log(
        self,
        episode: int,
        reward: float,
        steps: int,
    ):
        """
        Record one training episode.
        """

        record = {
            "episode": episode,
            "reward": reward,
            "steps": steps,
            "timestamp": datetime.now(UTC).isoformat(),
        }

        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    # ---------------------------------------------------------

    def exists(self) -> bool:
        return self.path.exists()

    # ---------------------------------------------------------

    def count(self) -> int:
        """
        Number of logged episodes.
        """

        if not self.exists():
            return 0

        with self.path.open("r", encoding="utf-8") as f:
            return sum(1 for _ in f)

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove the log file.
        """

        if self.exists():
            self.path.unlink()

    # ---------------------------------------------------------

    def size(self) -> int:
        """
        Size of the log file in bytes.
        """

        if not self.exists():
            return 0

        return self.path.stat().st_size