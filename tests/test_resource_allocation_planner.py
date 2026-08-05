from src.resource_allocation_planner import (
    ResourceAllocationPlanner,
)


def test_can_afford():

    planner = ResourceAllocationPlanner()

    assert planner.can_afford(
        money=500,
        cost=300,
    )


def test_cannot_afford():

    planner = ResourceAllocationPlanner()

    assert not planner.can_afford(
        money=100,
        cost=300,
    )


def test_remaining_budget():

    planner = ResourceAllocationPlanner()

    assert (
        planner.remaining_budget(
            money=500,
            cost=120,
        )
        == 380
    )


def test_spend():

    planner = ResourceAllocationPlanner()

    assert (
        planner.spend(
            money=500,
            cost=200,
        )
        == 300
    )


def test_spend_not_affordable():

    planner = ResourceAllocationPlanner()

    assert (
        planner.spend(
            money=50,
            cost=100,
        )
        == 50
    )