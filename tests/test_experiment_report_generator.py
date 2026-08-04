from src.experiment_report_generator import (
    ExperimentReportGenerator,
)


def sample():
    return {
        "count": 3,
        "best": 0.95,
        "average": 0.90,
        "worst": 0.85,
    }


def test_generate():

    generator = ExperimentReportGenerator()

    report = generator.generate(sample())

    assert report["best"] == 0.95


def test_to_text():

    generator = ExperimentReportGenerator()

    text = generator.to_text(sample())

    assert "Experiments: 3" in text


def test_has_data():

    generator = ExperimentReportGenerator()

    assert generator.has_data(sample())


def test_metric_count():

    generator = ExperimentReportGenerator()

    assert generator.metric_count(sample()) == 3


def test_empty_report():

    generator = ExperimentReportGenerator()

    report = generator.empty_report()

    assert report["count"] == 0