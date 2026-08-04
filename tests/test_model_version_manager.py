from src.model_version_manager import ModelVersionManager


def test_register():

    manager = ModelVersionManager()

    manager.register(
        "Policy",
        "v1",
        100,
        "v1.json",
    )

    assert manager.get(
        "Policy",
        "v1",
    )["score"] == 100


def test_latest():

    manager = ModelVersionManager()

    manager.register(
        "Policy",
        "v1",
        100,
        "v1.json",
    )

    manager.register(
        "Policy",
        "v2",
        200,
        "v2.json",
    )

    assert manager.latest("Policy") == "v2"


def test_list_versions():

    manager = ModelVersionManager()

    manager.register(
        "Policy",
        "v2",
        2,
        "2.json",
    )

    manager.register(
        "Policy",
        "v1",
        1,
        "1.json",
    )

    assert manager.list_versions(
        "Policy"
    ) == [
        "v1",
        "v2",
    ]


def test_remove():

    manager = ModelVersionManager()

    manager.register(
        "Policy",
        "v1",
        1,
        "1.json",
    )

    manager.remove(
        "Policy",
        "v1",
    )

    assert manager.get(
        "Policy",
        "v1",
    ) is None


def test_count():

    manager = ModelVersionManager()

    manager.register(
        "Policy",
        "v1",
        1,
        "1.json",
    )

    manager.register(
        "Policy",
        "v2",
        2,
        "2.json",
    )

    assert manager.count(
        "Policy"
    ) == 2