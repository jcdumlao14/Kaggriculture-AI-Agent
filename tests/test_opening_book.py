from src.opening_book import OpeningBook


def test_has_move():

    book = OpeningBook()

    assert book.has_move(1)


def test_move():

    book = OpeningBook()

    assert book.move(1) == "PLANT_WHEAT"


def test_unknown_day():

    book = OpeningBook()

    assert book.move(20) is None


def test_add_move():

    book = OpeningBook()

    book.add_move(6, "BUY_ANIMAL")

    assert book.move(6) == "BUY_ANIMAL"


def test_remove_move():

    book = OpeningBook()

    book.remove_move(2)

    assert not book.has_move(2)