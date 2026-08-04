from src.training_logger import TrainingLogger


def test_log_exists(tmp_path):

    file = tmp_path / "training.jsonl"

    logger = TrainingLogger(file)

    logger.log(1, 100, 50)

    assert logger.exists()


def test_count(tmp_path):

    file = tmp_path / "training.jsonl"

    logger = TrainingLogger(file)

    logger.log(1, 10, 5)
    logger.log(2, 20, 6)

    assert logger.count() == 2


def test_clear(tmp_path):

    file = tmp_path / "training.jsonl"

    logger = TrainingLogger(file)

    logger.log(1, 10, 5)

    logger.clear()

    assert not logger.exists()


def test_size(tmp_path):

    file = tmp_path / "training.jsonl"

    logger = TrainingLogger(file)

    logger.log(1, 50, 10)

    assert logger.size() > 0


def test_multiple_logs(tmp_path):

    file = tmp_path / "training.jsonl"

    logger = TrainingLogger(file)

    for i in range(5):
        logger.log(i, i * 10, i)

    assert logger.count() == 5