from src.workflow_executor import (
    WorkflowExecutor,
)
from src.workflow_orchestrator import (
    WorkflowOrchestrator,
)


def test_execute():

    workflow = WorkflowOrchestrator()

    executed = []

    workflow.add_step(
        "step",
        lambda: executed.append(True),
    )

    executor = WorkflowExecutor()

    executor.execute(workflow)

    assert executed == [True]


def test_completed():

    workflow = WorkflowOrchestrator()

    workflow.add_step(
        "step",
        lambda: None,
    )

    executor = WorkflowExecutor()

    executor.execute(workflow)

    assert executor.succeeded()


def test_failed():

    workflow = WorkflowOrchestrator()

    def broken():
        raise RuntimeError("failure")

    workflow.add_step(
        "broken",
        broken,
    )

    executor = WorkflowExecutor()

    executor.execute(workflow)

    assert executor.failed()


def test_exception():

    workflow = WorkflowOrchestrator()

    error = RuntimeError("boom")

    def broken():
        raise error

    workflow.add_step(
        "broken",
        broken,
    )

    executor = WorkflowExecutor()

    executor.execute(workflow)

    assert executor.exception() is error


def test_reset():

    executor = WorkflowExecutor()

    executor.reset()

    assert executor.status() == WorkflowExecutor.PENDING