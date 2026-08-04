from src.experience_replay import ExperienceReplay


def test_add():

    replay = ExperienceReplay()

    replay.add(1, 2, 3, 4, False)

    assert replay.size() == 1


def test_sample():

    replay = ExperienceReplay()

    replay.add(1, 2, 3, 4, False)
    replay.add(5, 6, 7, 8, True)

    batch = replay.sample(1)

    assert len(batch) == 1


def test_capacity():

    replay = ExperienceReplay(capacity=2)

    replay.add(1, 1, 1, 1, False)
    replay.add(2, 2, 2, 2, False)
    replay.add(3, 3, 3, 3, False)

    assert replay.size() == 2


def test_clear():

    replay = ExperienceReplay()

    replay.add(1, 2, 3, 4, False)

    replay.clear()

    assert replay.size() == 0


def test_sample_all():

    replay = ExperienceReplay()

    replay.add(1, 2, 3, 4, False)

    batch = replay.sample(10)

    assert len(batch) == 1