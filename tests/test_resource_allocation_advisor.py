from src.resource_allocation_advisor import (
    ResourceAllocationAdvisor,
)


def test_allocate():

    advisor = ResourceAllocationAdvisor()

    allocation = advisor.allocate(
        money=1000,
        crop_need=2,
        animal_need=1,
        expansion_need=1,
    )

    assert allocation["crops"] == 500.0
    assert allocation["animals"] == 250.0
    assert allocation["expansion"] == 250.0


def test_zero_need():

    advisor = ResourceAllocationAdvisor()

    allocation = advisor.allocate(
        money=1000,
        crop_need=0,
        animal_need=0,
        expansion_need=0,
    )

    assert allocation["crops"] == 0.0
    assert allocation["animals"] == 0.0
    assert allocation["expansion"] == 0.0


def test_highest_priority():

    advisor = ResourceAllocationAdvisor()

    allocation = {
        "crops": 300,
        "animals": 500,
        "expansion": 200,
    }

    assert (
        advisor.highest_priority(allocation)
        == "animals"
    )


def test_remaining():

    advisor = ResourceAllocationAdvisor()

    allocation = {
        "crops": 400,
        "animals": 300,
        "expansion": 200,
    }

    assert (
        advisor.remaining(
            money=1000,
            allocation=allocation,
        )
        == 100.0
    )


def test_no_remaining():

    advisor = ResourceAllocationAdvisor()

    allocation = advisor.allocate(
        money=1000,
        crop_need=2,
        animal_need=2,
        expansion_need=2,
    )

    assert (
        advisor.remaining(
            money=1000,
            allocation=allocation,
        )
        == 0.0
    )