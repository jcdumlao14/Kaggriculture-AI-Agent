from src.pipeline_scheduler import (
    PipelineScheduler,
)
from src.workflow_orchestrator import (
    WorkflowOrchestrator,
)


def test_schedule():

    scheduler = PipelineScheduler()

    workflow = WorkflowOrchestrator()

    scheduler.schedule(workflow)

    assert scheduler.pending() == 1


def test_run_next():

    scheduler = PipelineScheduler()

    workflow = WorkflowOrchestrator()

    executed = []

    workflow.add_step(
        "step",
        lambda: executed.append(True),
    )

    scheduler.schedule(workflow)

    scheduler.run_next()

    assert executed == [True]


def test_fifo():

    scheduler = PipelineScheduler()

    first = WorkflowOrchestrator()
    second = WorkflowOrchestrator()

    scheduler.schedule(first)
    scheduler.schedule(second)

    assert scheduler.run_next() is first
    assert scheduler.run_next() is second


def test_clear():

    scheduler = PipelineScheduler()

    scheduler.schedule(
        WorkflowOrchestrator(),
    )

    scheduler.clear()

    assert scheduler.pending() == 0


def test_empty():

    scheduler = PipelineScheduler()

    assert scheduler.is_empty()

    scheduler.schedule(
        WorkflowOrchestrator(),
    )

    assert not scheduler.is_empty()