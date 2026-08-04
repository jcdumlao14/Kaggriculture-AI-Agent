import json

from src.training_dashboard import TrainingDashboard


def create_log(path):
    records = [
        {"episode": 1, "reward": 10, "steps": 5},
        {"episode": 2, "reward": 20, "steps": 6},
        {"episode": 3, "reward": 30, "steps": 7},
        {"episode": 4, "reward": 40, "steps": 8},
    ]

    with path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")


def test_load(tmp_path):

    file = tmp_path / "training.jsonl"

    create_log(file)

    dashboard = TrainingDashboard(file)

    assert len(dashboard.load()) == 4


def test_best_reward(tmp_path):

    file = tmp_path / "training.jsonl"

    create_log(file)

    dashboard = TrainingDashboard(file)

    assert dashboard.best_reward() == 40


def test_average_reward(tmp_path):

    file = tmp_path / "training.jsonl"

    create_log(file)

    dashboard = TrainingDashboard(file)

    assert dashboard.average_reward() == 25


def test_moving_average(tmp_path):

    file = tmp_path / "training.jsonl"

    create_log(file)

    dashboard = TrainingDashboard(file)

    assert dashboard.moving_average(window=2) == [15, 25, 35]


def test_summary(tmp_path):

    file = tmp_path / "training.jsonl"

    create_log(file)

    dashboard = TrainingDashboard(file)

    summary = dashboard.summary()

    assert summary["episodes"] == 4
    assert summary["best_reward"] == 40
    assert summary["average_reward"] == 25
    assert summary["latest_reward"] == 40