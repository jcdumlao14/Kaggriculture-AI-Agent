from src.task_scoring import TaskScoring


class FakeSeason:

    def remaining_days(self):
        return 5


class FakeProfit:

    def profit(self, crop):
        return 120


class FakeMoney:

    def should_save(self):
        return False

    def can_afford(self, cost):
        return True


class FakeInventory:

    def should_sell(self, product):
        return True


def make_scoring():

    return TaskScoring(
        FakeSeason(),
        FakeProfit(),
        FakeMoney(),
        FakeInventory(),
    )


def test_harvest_score():

    scoring = make_scoring()

    assert scoring.harvest_score() >= 100


def test_plant_score():

    scoring = make_scoring()

    assert scoring.plant_score("WHEAT") > 0


def test_sell_score():

    scoring = make_scoring()

    assert scoring.sell_score("WHEAT") > 50


def test_buy_score():

    scoring = make_scoring()

    assert scoring.buy_score(100) > 0