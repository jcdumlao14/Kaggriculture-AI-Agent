from src.resource_pool import ResourcePool


def test_add():

    pool = ResourcePool()

    pool.add("GPU")

    assert pool.available() == 1


def test_acquire():

    pool = ResourcePool()

    pool.add("Worker")

    assert pool.acquire() == "Worker"


def test_release():

    pool = ResourcePool()

    pool.add("GPU")

    resource = pool.acquire()

    pool.release(resource)

    assert pool.available() == 1


def test_clear():

    pool = ResourcePool()

    pool.add("A")
    pool.add("B")

    pool.clear()

    assert pool.available() == 0


def test_empty_pool():

    pool = ResourcePool()

    assert pool.acquire() is None