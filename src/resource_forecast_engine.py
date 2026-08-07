"""
resource_forecast_engine.py

Resource Forecast Engine for the Kaggriculture AI Agent.

Forecasts future resource levels based on
current state and expected consumption.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class ResourceForecastEngine:
    """
    Forecast future resource availability.
    """

    def forecast(
        self,
        *,
        current: float,
        production: float,
        consumption: float,
        turns: int,
    ) -> float:
        """
        Forecast future resource amount.
        """

        return current + (production - consumption) * turns

    # ---------------------------------------------------------

    def shortage(
        self,
        *,
        current: float,
        production: float,
        consumption: float,
        turns: int,
    ) -> bool:
        """
        Return True if the forecast becomes negative.
        """

        return (
            self.forecast(
                current=current,
                production=production,
                consumption=consumption,
                turns=turns,
            )
            < 0
        )

    # ---------------------------------------------------------

    def surplus(
        self,
        *,
        current: float,
        production: float,
        consumption: float,
        turns: int,
    ) -> bool:
        """
        Return True if resources increase.
        """

        return (
            self.forecast(
                current=current,
                production=production,
                consumption=consumption,
                turns=turns,
            )
            > current
        )