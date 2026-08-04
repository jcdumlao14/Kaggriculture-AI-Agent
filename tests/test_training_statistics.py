from src.training_statistics import TrainingStatistics


def test_add_episode():

    stats = TrainingStatistics()

    stats.add_episode(25)

    assert stats.total_episodes() == 1


def test_best_reward():

    stats = TrainingStatistics()

    stats.add_episode(10)
    stats.add_episode(50)
    stats.add_episode(30)

    assert stats.best_reward() == 50


def test_average_reward():

    stats = TrainingStatistics()

    stats.add_episode(10)
    stats.add_episode(20)
    stats.add_episode(30)

    assert stats.average_reward() == 20


def test_latest_reward():

    stats = TrainingStatistics()

    stats.add_episode(5)
    stats.add_episode(15)

    assert stats.latest_reward() == 15


def test_summary():

    stats = TrainingStatistics()

    stats.add_episode(10)
    stats.add_episode(20)

    summary = stats.summary()

    assert summary["episodes"] == 2
    assert summary["best"] == 20
    assert summary["worst"] == 10
    assert summary["average"] == 15
    assert summary["latest"] == 20