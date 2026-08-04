from src.episode_manager import EpisodeManager


def test_start_episode():

    manager = EpisodeManager()

    manager.start_episode()

    assert manager.episode == 1
    assert manager.steps == 0
    assert manager.total_reward == 0


def test_add_reward():

    manager = EpisodeManager()

    manager.start_episode()

    manager.add_reward(15)

    assert manager.total_reward == 15


def test_step():

    manager = EpisodeManager()

    manager.start_episode()

    manager.step()
    manager.step()

    assert manager.steps == 2


def test_finish():

    manager = EpisodeManager()

    manager.start_episode()

    manager.finish()

    assert manager.done


def test_summary():

    manager = EpisodeManager()

    manager.start_episode()

    manager.step()
    manager.add_reward(8)
    manager.finish()

    summary = manager.summary()

    assert summary["episode"] == 1
    assert summary["steps"] == 1
    assert summary["reward"] == 8
    assert summary["done"] is True