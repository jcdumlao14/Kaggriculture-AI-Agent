from src.mcts_search import MCTSSearch


def test_expand():

    search = MCTSSearch()

    search.expand(["A", "B", "C"])

    assert len(search.root.children) == 3


def test_run():

    search = MCTSSearch()

    node = search.run(["A", "B"])

    assert node is not None


def test_best_action():

    search = MCTSSearch()

    search.run(["A", "B", "C"])

    best = search.best_action()

    assert best is not None


def test_empty():

    search = MCTSSearch()

    assert search.best_action() is None


def test_backpropagation():

    search = MCTSSearch()

    search.expand(["MOVE"])

    node = search.root.children[0]

    search.backpropagate(node, 50)

    assert node.reward == 50