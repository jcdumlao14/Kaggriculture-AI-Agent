"""
pipeline_engine.py

Pipeline Engine for the Kaggriculture AI Agent.

Executes configurable processing pipelines.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class PipelineEngine:
    """
    Executes a sequence of processing stages.
    """

    def __init__(self):
        self._stages = []

    # ---------------------------------------------------------

    def add_stage(self, stage):
        """
        Add a processing stage.

        A stage is any callable that accepts one argument
        and returns the transformed result.
        """
        self._stages.append(stage)

    # ---------------------------------------------------------

    def run(self, data):
        """
        Execute every stage in sequence.
        """
        result = data

        for stage in self._stages:
            result = stage(result)

        return result

    # ---------------------------------------------------------

    def stage_count(self) -> int:
        """
        Return the number of stages.
        """
        return len(self._stages)

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove all stages.
        """
        self._stages.clear()

    # ---------------------------------------------------------

    def stages(self):
        """
        Return a copy of the registered stages.
        """
        return list(self._stages)