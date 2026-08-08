"""
resource_aware_snapshot_trend_analyzer.py

Resource-Aware Snapshot Trend Analyzer for the
Kaggriculture AI Agent.

Classifies execution trends from snapshot comparisons.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceAwareSnapshotTrendAnalyzer:
    """
    Analyze execution snapshot trends.
    """

    # ---------------------------------------------------------

    def success_rate_trend(
        self,
        *,
        change: float,
    ) -> str:
        """
        Classify success-rate movement.
        """

        if change > 0:
            return "improving"

        if change < 0:
            return "declining"

        return "stable"

    # ---------------------------------------------------------

    def task_trend(
        self,
        *,
        change: int,
    ) -> str:
        """
        Classify task-count movement.
        """

        if change > 0:
            return "increasing"

        if change < 0:
            return "decreasing"

        return "stable"

    # ---------------------------------------------------------

    def result_trend(
        self,
        *,
        change: int,
    ) -> str:
        """
        Classify result-count movement.
        """

        if change > 0:
            return "increasing"

        if change < 0:
            return "decreasing"

        return "stable"

    # ---------------------------------------------------------

    def performance_trend(
        self,
        *,
        performance: str,
    ) -> str:
        """
        Normalize the performance classification.
        """

        if performance == "improved":
            return "positive"

        if performance == "declined":
            return "negative"

        if performance == "unchanged":
            return "neutral"

        return "unknown"

    # ---------------------------------------------------------

    def build(
        self,
        *,
        comparison: dict,
    ) -> dict:
        """
        Build a normalized trend report.
        """

        success_change = float(
            comparison.get(
                "success_rate_change",
                0.0,
            )
        )

        task_change = int(
            comparison.get(
                "task_count_change",
                0,
            )
        )

        result_change = int(
            comparison.get(
                "result_count_change",
                0,
            )
        )

        performance = comparison.get(
            "performance",
            "unknown",
        )

        return {
            "success_rate_trend": (
                self.success_rate_trend(
                    change=success_change,
                )
            ),
            "task_trend": self.task_trend(
                change=task_change,
            ),
            "result_trend": self.result_trend(
                change=result_change,
            ),
            "performance_trend": (
                self.performance_trend(
                    performance=performance,
                )
            ),
        }