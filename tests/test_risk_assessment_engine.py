from src.risk_assessment_engine import (
    RiskAssessmentEngine,
)


def test_risk():

    engine = RiskAssessmentEngine()

    assert engine.risk("HARVEST") == 10.0


def test_safest():

    engine = RiskAssessmentEngine()

    action = engine.safest_action(
        [
            "BUY",
            "HARVEST",
            "PLANT",
        ]
    )

    assert action == "HARVEST"


def test_highest():

    engine = RiskAssessmentEngine()

    action = engine.highest_risk(
        [
            "BUY",
            "HARVEST",
            "PLANT",
        ]
    )

    assert action == "BUY"


def test_safe():

    engine = RiskAssessmentEngine()

    assert engine.is_safe("SELL")


def test_supported():

    engine = RiskAssessmentEngine()

    assert "HARVEST" in engine.supported_actions()