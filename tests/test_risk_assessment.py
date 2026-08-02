from src.risk_assessment import RiskAssessment


def test_price_volatility():

    risk = RiskAssessment()

    history = [100, 110, 120]

    assert risk.price_volatility(history) == 20


def test_market_is_stable():

    risk = RiskAssessment()

    history = [100, 102, 101, 103]

    assert risk.is_stable(history)


def test_market_not_stable():

    risk = RiskAssessment()

    history = [100, 160, 80]

    assert not risk.is_stable(history)


def test_low_risk_investment():

    risk = RiskAssessment()

    history = [100, 102, 101, 99]

    assert risk.should_invest(history)


def test_high_risk_investment():

    risk = RiskAssessment()

    history = [100, 180, 60]

    assert not risk.should_invest(history)