from src.hybrid_search import HybridSearch


def test_rank():

    search = HybridSearch()

    states = [10, 20, 30]

    ranked = search.rank(states)

    assert len(ranked) == 3


def test_search():

    search = HybridSearch()

    state = search.search([10, 30, 20])

    assert state is not None


def test_evaluate():

    search = HybridSearch()

    score = search.evaluate(25)

    assert isinstance(score, (int, float))


def test_empty():

    search = HybridSearch()

    assert search.search([]) is None


def test_rank_order():

    search = HybridSearch()

    ranked = search.rank([1, 2])

    assert len(ranked) == 2