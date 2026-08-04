from src.training_loop import TrainingLoop


def test_single_episode():

    trainer = TrainingLoop()

    result = trainer.run_episode([1, 2, 3])

    assert result["episode"] == 1
    assert result["steps"] == 3
    assert result["reward"] == 6
    assert result["done"] is True


def test_two_episodes():

    trainer = TrainingLoop()

    history = trainer.run(
        [
            [1],
            [2, 3],
        ]
    )

    assert len(history) == 2
    assert history[0]["episode"] == 1
    assert history[1]["episode"] == 2


def test_reward_accumulation():

    trainer = TrainingLoop()

    result = trainer.run_episode([5, 5, 10])

    assert result["reward"] == 20


def test_zero_rewards():

    trainer = TrainingLoop()

    result = trainer.run_episode([0, 0, 0])

    assert result["reward"] == 0


def test_empty_episode():

    trainer = TrainingLoop()

    result = trainer.run_episode([])

    assert result["steps"] == 0
    assert result["reward"] == 0
    assert result["done"] is True