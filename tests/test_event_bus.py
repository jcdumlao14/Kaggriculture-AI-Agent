from src.event_bus import EventBus


def test_subscribe():

    bus = EventBus()

    def callback(data):
        pass

    bus.subscribe("train", callback)

    assert bus.listener_count("train") == 1


def test_publish():

    bus = EventBus()

    received = []

    def callback(data):
        received.append(data)

    bus.subscribe("reward", callback)

    bus.publish("reward", 125)

    assert received == [125]


def test_unsubscribe():

    bus = EventBus()

    def callback(data):
        pass

    bus.subscribe("episode", callback)
    bus.unsubscribe("episode", callback)

    assert bus.listener_count("episode") == 0


def test_multiple_listeners():

    bus = EventBus()

    values = []

    def a(data):
        values.append(data)

    def b(data):
        values.append(data * 2)

    bus.subscribe("score", a)
    bus.subscribe("score", b)

    bus.publish("score", 10)

    assert values == [10, 20]


def test_clear():

    bus = EventBus()

    def callback(data):
        pass

    bus.subscribe("x", callback)

    bus.clear()

    assert bus.listener_count("x") == 0