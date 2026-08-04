from src.transposition_table import TranspositionTable


def test_store():

    table = TranspositionTable()

    table.store("state1", 50)

    assert table.lookup("state1") == 50


def test_contains():

    table = TranspositionTable()

    table.store("abc", 10)

    assert table.contains("abc")


def test_missing():

    table = TranspositionTable()

    assert table.lookup("missing") is None


def test_clear():

    table = TranspositionTable()

    table.store("A", 1)

    table.clear()

    assert table.size() == 0


def test_size():

    table = TranspositionTable()

    table.store("A", 10)
    table.store("B", 20)

    assert table.size() == 2