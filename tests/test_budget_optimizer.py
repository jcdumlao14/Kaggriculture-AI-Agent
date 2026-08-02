from src.budget_optimizer import BudgetOptimizer


def test_can_afford():

    budget = BudgetOptimizer(1000)

    assert budget.can_afford(500)


def test_cannot_afford():

    budget = BudgetOptimizer(300)

    assert not budget.can_afford(250)


def test_spendable():

    budget = BudgetOptimizer(1000)

    assert budget.spendable() == 800


def test_remaining_money():

    budget = BudgetOptimizer(1000)

    assert budget.remaining_after_purchase(250) == 750