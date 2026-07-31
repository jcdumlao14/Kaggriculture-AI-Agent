"""
main.py

Kaggle submission entry point for the
Kaggriculture AI Agent.

Author: Jocelyn Dumlao
Project: Kaggriculture-AI-Agent
"""

from src.agent import KaggricultureAgent

# -----------------------------------------------------
# Create one persistent agent instance
# -----------------------------------------------------

agent_instance = KaggricultureAgent()


# -----------------------------------------------------
# Kaggle entry point
# -----------------------------------------------------

def agent(observation):
    """
    Kaggle calls this function once every turn.

    Parameters
    ----------
    observation : dict
        Current game observation.

    Returns
    -------
    dict
        Action dictionary for the current turn.
    """

    return agent_instance.act(observation)