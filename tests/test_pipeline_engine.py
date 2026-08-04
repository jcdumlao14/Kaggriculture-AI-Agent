from src.pipeline_engine import PipelineEngine


def test_add_stage():

    pipeline = PipelineEngine()

    pipeline.add_stage(lambda x: x + 1)

    assert pipeline.stage_count() == 1


def test_run_single_stage():

    pipeline = PipelineEngine()

    pipeline.add_stage(lambda x: x * 2)

    assert pipeline.run(5) == 10


def test_run_multiple_stages():

    pipeline = PipelineEngine()

    pipeline.add_stage(lambda x: x + 2)
    pipeline.add_stage(lambda x: x * 3)
    pipeline.add_stage(lambda x: x - 4)

    assert pipeline.run(5) == 17


def test_clear():

    pipeline = PipelineEngine()

    pipeline.add_stage(lambda x: x)

    pipeline.clear()

    assert pipeline.stage_count() == 0


def test_stage_list():

    pipeline = PipelineEngine()

    pipeline.add_stage(lambda x: x)

    assert len(pipeline.stages()) == 1