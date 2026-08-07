from src.base_workflow_coordinator import (
    BaseWorkflowCoordinator,
)


class DummyCoordinator(
    BaseWorkflowCoordinator,
):

    def prepare_features(
        self,
        *,
        state_id,
        game_state,
        maximums=None,
        selected=None,
    ):
        return game_state

    def clear_cache(
        self,
    ):
        pass


def test_interface():

    coordinator = DummyCoordinator()

    result = coordinator.prepare_features(
        state_id="1",
        game_state={
            "money": 100,
        },
    )

    assert result["money"] == 100


def test_clear_cache():

    coordinator = DummyCoordinator()

    assert coordinator.clear_cache() is None


def test_inheritance():

    coordinator = DummyCoordinator()

    assert isinstance(
        coordinator,
        BaseWorkflowCoordinator,
    )


def test_multiple_calls():

    coordinator = DummyCoordinator()

    first = coordinator.prepare_features(
        state_id="a",
        game_state={
            "x": 1,
        },
    )

    second = coordinator.prepare_features(
        state_id="b",
        game_state={
            "y": 2,
        },
    )

    assert first["x"] == 1
    assert second["y"] == 2


def test_empty():

    coordinator = DummyCoordinator()

    result = coordinator.prepare_features(
        state_id="z",
        game_state={},
    )

    assert result == {}