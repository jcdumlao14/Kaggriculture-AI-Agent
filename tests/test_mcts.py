from src.mcts import MCTSNode


def test_node_creation():

    node = MCTSNode()

    assert node.visits == 0
    assert node.reward == 0


def test_add_child():

    root = MCTSNode()

    child = root.add_child("PLANT")

    assert child.parent is root
    assert len(root.children) == 1


def test_update():

    node = MCTSNode()

    node.update(10)

    assert node.reward == 10
    assert node.visits == 1


def test_average_reward():

    node = MCTSNode()

    node.update(10)
    node.update(20)

    assert node.average_reward() == 15


def test_ucb_unvisited():

    node = MCTSNode()

    assert node.ucb1() == float("inf")