from src.workflow_orchestrator import (
    WorkflowOrchestrator,
)


def test_add_step():

    workflow = WorkflowOrchestrator()

    workflow.add_step(
        "load",
        lambda: None,
    )

    assert workflow.total_steps() == 1


def test_run():

    workflow = WorkflowOrchestrator()

    result = []

    workflow.add_step(
        "a",
        lambda: result.append("a"),
    )

    workflow.add_step(
        "b",
        lambda: result.append("b"),
    )

    workflow.run()

    assert result == [
        "a",
        "b",
    ]


def test_completed_steps():

    workflow = WorkflowOrchestrator()

    workflow.add_step(
        "prepare",
        lambda: None,
    )

    workflow.run()

    assert workflow.completed_steps() == [
        "prepare",
    ]


def test_reset():

    workflow = WorkflowOrchestrator()

    workflow.add_step(
        "train",
        lambda: None,
    )

    workflow.run()

    workflow.reset()

    assert workflow.completed_steps() == []


def test_status():

    workflow = WorkflowOrchestrator()

    workflow.add_step(
        "prepare",
        lambda: None,
    )

    workflow.add_step(
        "train",
        lambda: None,
    )

    workflow.run()

    status = workflow.status()

    assert status["finished"]
    assert status["completed_steps"] == 2