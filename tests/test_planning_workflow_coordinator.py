from src.planning_workflow_coordinator import (
    PlanningWorkflowCoordinator,
)


def test_prepare_features():

    workflow = PlanningWorkflowCoordinator()

    features = workflow.prepare_features(
        state_id="a",
        game_state={
            "money": 500,
        },
    )

    assert features["money"] == 500


def test_normalized():

    workflow = PlanningWorkflowCoordinator()

    features = workflow.prepare_features(
        state_id="b",
        game_state={
            "money": 50,
        },
        maximums={
            "money": 100,
        },
    )

    assert features["money"] == 0.5


def test_selected():

    workflow = PlanningWorkflowCoordinator()

    features = workflow.prepare_features(
        state_id="c",
        game_state={
            "money": 100,
            "day": 2,
        },
        selected=["money"],
    )

    assert "money" in features
    assert "day" not in features


def test_cache():

    workflow = PlanningWorkflowCoordinator()

    first = workflow.prepare_features(
        state_id="x",
        game_state={
            "money": 100,
        },
    )

    second = workflow.prepare_features(
        state_id="x",
        game_state={
            "money": 999,
        },
    )

    assert first == second


def test_clear_cache():

    workflow = PlanningWorkflowCoordinator()

    workflow.prepare_features(
        state_id="z",
        game_state={},
    )

    workflow.clear_cache()

    assert (
        workflow.service.feature_service.pipeline.cache.size()
        == 0
    )