from src.dependency_container import DependencyContainer


class DummyService:

    def __init__(self):
        self.value = 123


def test_register():

    container = DependencyContainer()

    container.register("service", DummyService)

    assert container.exists("service")


def test_resolve_factory():

    container = DependencyContainer()

    container.register("service", DummyService)

    service = container.resolve("service")

    assert isinstance(service, DummyService)


def test_register_instance():

    container = DependencyContainer()

    instance = DummyService()

    container.register_instance("singleton", instance)

    assert container.resolve("singleton") is instance


def test_clear():

    container = DependencyContainer()

    container.register("service", DummyService)

    container.clear()

    assert not container.exists("service")


def test_unknown_service():

    container = DependencyContainer()

    try:
        container.resolve("missing")
        assert False
    except KeyError:
        assert True