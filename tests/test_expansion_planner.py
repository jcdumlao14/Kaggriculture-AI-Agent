from src.expansion_planner import ExpansionPlanner


def test_can_expand():

    planner = ExpansionPlanner()

    assert planner.can_expand(
        money=10000,
        available_land=3,
    )


def test_cannot_expand_without_money():

    planner = ExpansionPlanner()

    assert not planner.can_expand(
        money=2000,
        available_land=3,
    )


def test_cannot_expand_without_land():

    planner = ExpansionPlanner()

    assert not planner.can_expand(
        money=10000,
        available_land=0,
    )


def test_priority():

    planner = ExpansionPlanner()

    score = planner.expansion_priority(
        money=10000,
        available_land=2,
    )

    assert score > 0


def test_should_expand():

    planner = ExpansionPlanner()

    assert planner.should_expand(
        money=15000,
        available_land=5,
    )


def test_recommended_land():

    planner = ExpansionPlanner()

    plots = planner.recommended_land(
        money=15000,
        available_land=5,
    )

    assert plots == 3