from src.opportunity_analyzer import OpportunityAnalyzer


def test_score():

    analyzer = OpportunityAnalyzer()

    score = analyzer.score(
        reward=100,
        risk=20,
        urgency=10,
    )

    assert score == 90


def test_best():

    analyzer = OpportunityAnalyzer()

    opportunities = [
        {"task": "PLANT", "score": 50},
        {"task": "SELL", "score": 90},
        {"task": "HARVEST", "score": 120},
    ]

    best = analyzer.best(opportunities)

    assert best["task"] == "HARVEST"


def test_rank():

    analyzer = OpportunityAnalyzer()

    opportunities = [
        {"task": "A", "score": 30},
        {"task": "B", "score": 90},
        {"task": "C", "score": 60},
    ]

    ranked = analyzer.rank(opportunities)

    assert ranked[0]["task"] == "B"
    assert ranked[1]["task"] == "C"
    assert ranked[2]["task"] == "A"