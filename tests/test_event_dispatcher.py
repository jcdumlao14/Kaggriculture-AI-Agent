from src.event_dispatcher import EventDispatcher


def test_dispatch():

    dispatcher = EventDispatcher()

    dispatcher.dispatch(
        "train",
        {"epoch": 1},
    )

    assert dispatcher.pending() == 1


def test_next_event():

    dispatcher = EventDispatcher()

    dispatcher.dispatch(
        "predict",
        5,
    )

    event = dispatcher.next_event()

    assert event == (
        "predict",
        5,
    )


def test_fifo_order():

    dispatcher = EventDispatcher()

    dispatcher.dispatch("a")
    dispatcher.dispatch("b")
    dispatcher.dispatch("c")

    assert dispatcher.next_event()[0] == "a"
    assert dispatcher.next_event()[0] == "b"
    assert dispatcher.next_event()[0] == "c"


def test_empty():

    dispatcher = EventDispatcher()

    assert dispatcher.empty()

    dispatcher.dispatch("x")

    assert not dispatcher.empty()


def test_clear():

    dispatcher = EventDispatcher()

    dispatcher.dispatch("x")
    dispatcher.dispatch("y")

    dispatcher.clear()

    assert dispatcher.pending() == 0