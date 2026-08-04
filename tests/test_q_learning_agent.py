from src.q_learning_agent import QLearningAgent


def test_initial_value():

    agent = QLearningAgent()

    assert agent.value("A", "MOVE") == 0.0


def test_learning():

    agent = QLearningAgent()

    value = agent.learn(
        state="A",
        action="MOVE",
        reward=10,
        next_state="B",
        next_actions=[],
    )

    assert value > 0


def test_best_action():

    agent = QLearningAgent()

    agent.learn("A", "MOVE", 10, "B", [])
    agent.learn("A", "WAIT", 2, "B", [])

    assert agent.best_action("A") == "MOVE"


def test_reset():

    agent = QLearningAgent()

    agent.learn("A", "MOVE", 5, "B", [])

    agent.reset()

    assert agent.value("A", "MOVE") == 0.0


def test_future_reward():

    agent = QLearningAgent()

    agent.q.update("B", "HARVEST", 20)

    value = agent.learn(
        "A",
        "MOVE",
        reward=5,
        next_state="B",
        next_actions=["HARVEST"],
    )

    assert value > 5 * agent.alpha