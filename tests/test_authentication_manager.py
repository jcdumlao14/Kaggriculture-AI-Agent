from src.authentication_manager import (
    AuthenticationManager,
)


def test_register():

    manager = AuthenticationManager()

    manager.register(
        "client1",
        "abc123",
    )

    assert manager.authorized("client1")


def test_authenticate():

    manager = AuthenticationManager()

    manager.register(
        "client1",
        "secret",
    )

    assert manager.authenticate(
        "client1",
        "secret",
    )


def test_revoke():

    manager = AuthenticationManager()

    manager.register(
        "client1",
        "secret",
    )

    manager.revoke("client1")

    assert not manager.authorized("client1")


def test_list_clients():

    manager = AuthenticationManager()

    manager.register("A", "1")
    manager.register("B", "2")

    assert manager.list_clients() == [
        "A",
        "B",
    ]


def test_count():

    manager = AuthenticationManager()

    manager.register("A", "1")
    manager.register("B", "2")

    assert manager.count() == 2