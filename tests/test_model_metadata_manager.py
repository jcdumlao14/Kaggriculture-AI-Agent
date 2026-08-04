from src.model_metadata_manager import (
    ModelMetadataManager,
)


def test_register():

    manager = ModelMetadataManager()

    manager.register(
        "Policy",
        "v1",
        author="Jocelyn",
        algorithm="Q-Learning",
        dataset="Season1",
        trained_on="2026-08-04",
        tags=["baseline"],
    )

    assert manager.exists(
        "Policy",
        "v1",
    )


def test_get():

    manager = ModelMetadataManager()

    manager.register(
        "Policy",
        "v1",
        "Jocelyn",
        "DQN",
        "FarmSet",
        "2026-08-04",
        ["rl"],
    )

    metadata = manager.get(
        "Policy",
        "v1",
    )

    assert metadata["algorithm"] == "DQN"


def test_tags():

    manager = ModelMetadataManager()

    manager.register(
        "Policy",
        "v1",
        "JC",
        "PPO",
        "Dataset",
        "2026-08-04",
        ["best", "stable"],
    )

    metadata = manager.get(
        "Policy",
        "v1",
    )

    assert "stable" in metadata["tags"]


def test_remove():

    manager = ModelMetadataManager()

    manager.register(
        "Policy",
        "v1",
        "JC",
        "PPO",
        "Dataset",
        "2026-08-04",
    )

    manager.remove(
        "Policy",
        "v1",
    )

    assert not manager.exists(
        "Policy",
        "v1",
    )


def test_count():

    manager = ModelMetadataManager()

    manager.register(
        "Policy",
        "v1",
        "JC",
        "PPO",
        "Data",
        "2026-08-04",
    )

    manager.register(
        "Policy",
        "v2",
        "JC",
        "DQN",
        "Data",
        "2026-08-05",
    )

    assert manager.count("Policy") == 2