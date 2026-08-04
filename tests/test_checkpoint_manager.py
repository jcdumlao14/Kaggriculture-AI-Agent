from pathlib import Path

from src.checkpoint_manager import CheckpointManager


def test_save_and_exists(tmp_path):

    file = tmp_path / "checkpoint.json"

    manager = CheckpointManager(file)

    manager.save({"A": {"MOVE": 5}})

    assert manager.exists()


def test_load(tmp_path):

    file = tmp_path / "checkpoint.json"

    manager = CheckpointManager(file)

    manager.save({"A": {"MOVE": 10}})

    data = manager.load()

    assert data["A"]["MOVE"] == 10


def test_delete(tmp_path):

    file = tmp_path / "checkpoint.json"

    manager = CheckpointManager(file)

    manager.save({"x": 1})

    manager.delete()

    assert not manager.exists()


def test_missing_file(tmp_path):

    file = tmp_path / "missing.json"

    manager = CheckpointManager(file)

    assert manager.load() == {}


def test_size(tmp_path):

    file = tmp_path / "checkpoint.json"

    manager = CheckpointManager(file)

    manager.save({"A": 1})

    assert manager.size() > 0