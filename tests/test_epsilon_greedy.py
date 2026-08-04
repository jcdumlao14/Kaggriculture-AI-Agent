from src.epsilon_greedy import EpsilonGreedy
from src.q_table import QTable


def test_best_action():

    table = QTable()

    table.update("A", "MOVE", 10)
    table.update("A", "WAIT", 5)

    policy = EpsilonGreedy(epsilon=0)

    action = policy.choose(
        table,
        "A",
        ["MOVE", "WAIT"],
    )

    assert action == "MOVE"


def test_random_action():

    table = QTable()

    policy = EpsilonGreedy(epsilon=1)

    action = policy.choose(
        table,
        "A",
        ["MOVE", "WAIT"],
    )

    assert action in ["MOVE", "WAIT"]


def test_empty_actions():

    table = QTable()

    policy = EpsilonGreedy()

    assert policy.choose(table, "A", []) is None


def test_decay():

    policy = EpsilonGreedy(1.0)

    policy.decay(0.5)

    assert policy.epsilon == 0.5


def test_minimum_decay():

    policy = EpsilonGreedy(0.02)

    policy.decay(0.1)

    assert policy.epsilon == 0.01