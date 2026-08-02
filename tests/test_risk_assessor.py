from src.risk_assessor import RiskAssessor


def test_risk_value():

    risk = RiskAssessor()

    assert risk.risk("PLANT") == 0.30


def test_safe():

    risk = RiskAssessor()

    assert risk.safe("HARVEST")


def test_dangerous():

    risk = RiskAssessor()

    assert risk.dangerous("BUY_ANIMAL")


def test_safest():

    risk = RiskAssessor()

    actions = [
        "BUY_ANIMAL",
        "PLANT",
        "HARVEST",
    ]

    assert risk.safest(actions) == "HARVEST"


def test_riskiest():

    risk = RiskAssessor()

    actions = [
        "BUY_ANIMAL",
        "PLANT",
        "HARVEST",
    ]

    assert risk.riskiest(actions) == "BUY_ANIMAL"