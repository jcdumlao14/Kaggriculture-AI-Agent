from src.beam_search import BeamSearch


def test_select():

    beam = BeamSearch(beam_width=2)

    candidates = [
        ("A", 10),
        ("B", 30),
        ("C", 20),
    ]

    result = beam.select(candidates)

    assert len(result) == 2
    assert result[0][0] == "B"
    assert result[1][0] == "C"


def test_best():

    beam = BeamSearch()

    candidates = [
        ("A", 10),
        ("B", 50),
        ("C", 30),
    ]

    assert beam.best(candidates) == ("B", 50)


def test_empty():

    beam = BeamSearch()

    assert beam.best([]) is None


def test_update_width():

    beam = BeamSearch()

    beam.update_width(5)

    assert beam.beam_width == 5


def test_select_all():

    beam = BeamSearch(beam_width=10)

    candidates = [
        ("A", 5),
        ("B", 2),
    ]

    assert len(beam.select(candidates)) == 2