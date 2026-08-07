from src.farm_economy_planner import (
    FarmEconomyPlanner,
)


def test_reserve():

    planner = FarmEconomyPlanner()

    assert (
        planner.reserve_cash(
            money=1000,
        )
        == 200
    )


def test_spendable():

    planner = FarmEconomyPlanner()

    assert (
        planner.spendable_cash(
            money=1000,
        )
        == 800
    )


def test_afford():

    planner = FarmEconomyPlanner()

    assert planner.can_afford(
        money=1000,
        cost=700,
    )


def test_not_afford():

    planner = FarmEconomyPlanner()

    assert not planner.can_afford(
        money=1000,
        cost=900,
    )


def test_investment_ratio():

    planner = FarmEconomyPlanner()

    assert (
        planner.investment_ratio(
            money=1000,
            investment=250,
        )
        == 0.25
    )
    