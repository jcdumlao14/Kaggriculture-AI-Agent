from src.authorization_manager import (
    AuthorizationManager,
)


def test_assign_role():

    manager = AuthorizationManager()

    manager.assign_role(
        "alice",
        "admin",
    )

    assert manager.role("alice") == "admin"


def test_grant_permission():

    manager = AuthorizationManager()

    manager.assign_role(
        "alice",
        "admin",
    )

    manager.grant_permission(
        "admin",
        "deploy",
    )

    assert manager.has_permission(
        "alice",
        "deploy",
    )


def test_revoke_role():

    manager = AuthorizationManager()

    manager.assign_role(
        "alice",
        "admin",
    )

    manager.revoke_role("alice")

    assert manager.role("alice") is None


def test_list_roles():

    manager = AuthorizationManager()

    manager.assign_role("alice", "admin")
    manager.assign_role("bob", "viewer")

    assert manager.list_roles() == [
        "admin",
        "viewer",
    ]


def test_user_count():

    manager = AuthorizationManager()

    manager.assign_role("alice", "admin")
    manager.assign_role("bob", "viewer")

    assert manager.user_count() == 2