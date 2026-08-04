from src.self_play_trainer import SelfPlayTrainer


def test_record():

    trainer = SelfPlayTrainer()

    trainer.record(120)

    assert trainer.games_played() == 1


def test_average_reward():

    trainer = SelfPlayTrainer()

    trainer.record(100)
    trainer.record(200)

    assert trainer.average_reward() == 150


def test_best_reward():

    trainer = SelfPlayTrainer()

    trainer.record(100)
    trainer.record(350)
    trainer.record(250)

    assert trainer.best_reward() == 350


def test_empty_average():

    trainer = SelfPlayTrainer()

    assert trainer.average_reward() == 0


def test_reset():

    trainer = SelfPlayTrainer()

    trainer.record(100)

    trainer.reset()

    assert trainer.games_played() == 0