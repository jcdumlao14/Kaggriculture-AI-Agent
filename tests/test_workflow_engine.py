from src.workflow_engine import WorkflowEngine


def test_register():

    engine = WorkflowEngine()

    engine.register("double", lambda x: x * 2)

    assert engine.exists("double")


def test_run():

    engine = WorkflowEngine()

    engine.register("increment", lambda x: x + 1)

    assert engine.run("increment", 10) == 11


def test_unregister():

    engine = WorkflowEngine()

    engine.register("sample", lambda x: x)

    engine.unregister("sample")

    assert not engine.exists("sample")


def test_list_workflows():

    engine = WorkflowEngine()

    engine.register("b", lambda x: x)
    engine.register("a", lambda x: x)

    assert engine.list_workflows() == ["a", "b"]


def test_clear():

    engine = WorkflowEngine()

    engine.register("workflow", lambda x: x)

    engine.clear()

    assert engine.list_workflows() == []