import pytest

from src.job_manager import JobManager


def test_submit():

    manager = JobManager()

    manager.submit("job1", lambda: 1)

    assert manager.jobs() == ["job1"]


def test_run():

    manager = JobManager()

    manager.submit("double", lambda: 8)

    assert manager.run("double") == 8


def test_completed_status():

    manager = JobManager()

    manager.submit("job", lambda: 10)

    manager.run("job")

    assert manager.status("job") == "completed"


def test_failed_status():

    manager = JobManager()

    def bad():
        raise RuntimeError()

    manager.submit("bad", bad)

    with pytest.raises(RuntimeError):
        manager.run("bad")

    assert manager.status("bad") == "failed"


def test_remove():

    manager = JobManager()

    manager.submit("job", lambda: 1)

    manager.remove("job")

    assert manager.jobs() == []