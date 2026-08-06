from src.opportunity_assessment_engine import (
    OpportunityAssessmentEngine,
)


def test_value():

    engine = OpportunityAssessmentEngine()

    assert engine.value("HARVEST") == 90.0


def test_best():

    engine = OpportunityAssessmentEngine()

    action = engine.best_action(
        [
            "BUY",
            "HARVEST",
            "PLANT",
        ]
    )

    assert action == "HARVEST"


def test_worst():

    engine = OpportunityAssessmentEngine()

    action = engine.worst_action(
        [
            "BUY",
            "HARVEST",
            "PLANT",
        ]
    )

    assert action == "BUY"


def test_worthwhile():

    engine = OpportunityAssessmentEngine()

    assert engine.worthwhile("SELL")


def test_supported():

    engine = OpportunityAssessmentEngine()

    assert "HARVEST" in engine.supported_actions()