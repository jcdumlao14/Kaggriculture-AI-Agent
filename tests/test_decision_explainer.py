from src.decision_explainer import DecisionExplainer


def test_explain_returns_dict():

    explainer = DecisionExplainer()

    result = explainer.explain(
        "PLANT",
        utility=82.5,
        profit=90,
        risk=10,
        season="EARLY",
        reason="Highest profit",
    )

    assert isinstance(result, dict)


def test_summary_contains_action():

    explainer = DecisionExplainer()

    result = explainer.explain(
        "HARVEST",
        utility=95,
        profit=100,
        risk=5,
        season="MID",
        reason="Ready to harvest",
    )

    summary = explainer.summary(result)

    assert "HARVEST" in summary


def test_best_reason():

    explainer = DecisionExplainer()

    assert explainer.best_reason() == "Highest overall utility score."


def test_summary_returns_string():

    explainer = DecisionExplainer()

    result = explainer.explain(
        "SELL",
        utility=75,
        profit=70,
        risk=15,
        season="LATE",
        reason="High market price",
    )

    assert isinstance(explainer.summary(result), str)


def test_profit_value():

    explainer = DecisionExplainer()

    result = explainer.explain(
        "PLANT",
        profit=88.8,
    )

    assert result["profit"] == 88.8