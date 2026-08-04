from src.experiment_repository import ExperimentRepository


def test_save():

    repo = ExperimentRepository()

    repo.save("exp1", {"score": 10})

    assert repo.get("exp1") == {"score": 10}


def test_update():

    repo = ExperimentRepository()

    repo.save("exp", {"score": 5})

    repo.update("exp", {"score": 20})

    assert repo.get("exp")["score"] == 20


def test_delete():

    repo = ExperimentRepository()

    repo.save("exp", {})

    repo.delete("exp")

    assert repo.get("exp") is None


def test_list():

    repo = ExperimentRepository()

    repo.save("b", {})
    repo.save("a", {})

    assert repo.list_experiments() == ["a", "b"]


def test_clear():

    repo = ExperimentRepository()

    repo.save("exp", {})

    repo.clear()

    assert repo.list_experiments() == []