from src.rl_environment import RLEnvironment


def test_reset():

    env = RLEnvironment()

    state = env.reset()

    assert state["step"] == 0


def test_step():

    env = RLEnvironment()

    env.reset()

    state, reward, done = env.step("MOVE")

    assert reward == 1.0
    assert state["step"] == 1
    assert not done


def test_episode_end():

    env = RLEnvironment(max_steps=2)

    env.reset()

    env.step("A")

    _, _, done = env.step("B")

    assert done


def test_is_done():

    env = RLEnvironment(max_steps=1)

    env.reset()

    env.step("MOVE")

    assert env.is_done()


def test_total_reward():

    env = RLEnvironment(max_steps=3)

    env.reset()

    env.step("A")
    env.step("B")

    assert env.total_reward == 2.0