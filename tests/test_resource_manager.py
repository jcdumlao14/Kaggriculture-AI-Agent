from src.resource_manager import ResourceManager


def test_register():

    manager = ResourceManager()

    manager.register("gpu", "GPU-0")

    assert manager.count() == 1


def test_allocate():

    manager = ResourceManager()

    manager.register("worker", "Worker-1")

    assert manager.allocate("worker") == "Worker-1"


def test_allocate_twice():

    manager = ResourceManager()

    manager.register("gpu", "GPU-0")

    manager.allocate("gpu")

    assert manager.allocate("gpu") is None


def test_release():

    manager = ResourceManager()

    manager.register("gpu", "GPU-0")

    manager.allocate("gpu")

    manager.release("gpu")

    assert not manager.is_allocated("gpu")


def test_remove():

    manager = ResourceManager()

    manager.register("worker", object())

    manager.remove("worker")

    assert manager.count() == 0