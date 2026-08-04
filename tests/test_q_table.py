from src.q_table import QTable


def test_default_value():

    table = QTable()

    assert table.get("A", "MOVE") == 0.0


def test_update():

    table = QTable()

    table.update("A", "MOVE", 5.0)

    assert table.get("A", "MOVE") == 5.0


def test_best_action():

    table = QTable()

    table.update("A", "MOVE", 2.0)
    table.update("A", "HARVEST", 8.0)

    assert table.best_action("A") == "HARVEST"


def test_size():

    table = QTable()

    table.update("A", "MOVE", 1)

    assert table.size() == 1


def test_clear():

    table = QTable()

    table.update("A", "MOVE", 3)

    table.clear()

    assert table.size() == 0
    