from src.decision_workflow_coordinator import (
    DecisionWorkflowCoordinator,
)


def test_evaluate():

    workflow = DecisionWorkflowCoordinator()

    score = workflow.evaluate(
        state_id="a",
        game_state={"money": 100},
        action="MOVE",
    )

    assert isinstance(score, float)


def test_record():

    workflow = DecisionWorkflowCoordinator()

    workflow.record(
        turn=1,
        action="MOVE",
        score=5.0,
    )

    assert len(workflow.history()) == 1


def test_history():

    workflow = DecisionWorkflowCoordinator()

    workflow.record(
        turn=2,
        action="WAIT",
        score=3.0,
    )

    assert workflow.history()[0]["action"] == "WAIT"


def test_clear_cache():

    workflow = DecisionWorkflowCoordinator()

    workflow.service.feature_service.features(
        state_id="x",
        game_state={},
    )

    workflow.clear_cache()

    assert (
        workflow.service.feature_service.pipeline.cache.size()
        == 0
    )


def test_multiple_records():

    workflow = DecisionWorkflowCoordinator()

    workflow.record(
        turn=1,
        action="MOVE",
        score=1.0,
    )

    workflow.record(
        turn=2,
        action="HARVEST",
        score=2.0,
    )

    assert len(workflow.history()) == 2