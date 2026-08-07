from src.episode_learning_engine import (
    EpisodeLearningEngine,
)


def test_record_episode():

    engine = EpisodeLearningEngine()

    engine.record_episode(
        reward=120,
        win=True,
    )

    assert engine.total_episodes() == 1


def test_average_reward():

    engine = EpisodeLearningEngine()

    engine.record_episode(
        reward=100,
        win=True,
    )

    engine.record_episode(
        reward=200,
        win=False,
    )

    assert engine.average_reward() == 150.0


def test_best_reward():

    engine = EpisodeLearningEngine()

    engine.record_episode(
        reward=75,
        win=False,
    )

    engine.record_episode(
        reward=220,
        win=True,
    )

    assert engine.best_reward() == 220.0


def test_win_rate():

    engine = EpisodeLearningEngine()

    engine.record_episode(
        reward=100,
        win=True,
    )

    engine.record_episode(
        reward=80,
        win=False,
    )

    engine.record_episode(
        reward=150,
        win=True,
    )

    assert engine.win_rate() == (
        2 / 3
    )


def test_empty_engine():

    engine = EpisodeLearningEngine()

    assert engine.total_episodes() == 0
    assert engine.average_reward() == 0.0
    assert engine.best_reward() == 0.0
    assert engine.win_rate() == 0.0