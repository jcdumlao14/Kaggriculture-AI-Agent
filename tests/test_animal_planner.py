from src.animal_planner import AnimalPlanner


def test_feed():

    planner = AnimalPlanner()

    animal = {
        "hungry": True,
    }

    assert planner.can_feed(animal)


def test_collect():

    planner = AnimalPlanner()

    animal = {
        "product_ready": True,
    }

    assert planner.can_collect(animal)


def test_harvest():

    planner = AnimalPlanner()

    animal = {
        "harvest_ready": True,
    }

    assert planner.can_harvest(animal)


def test_priority():

    planner = AnimalPlanner()

    animal = {
        "hungry": True,
        "product_ready": True,
    }

    assert planner.priority(animal) == 70.0


def test_best_action():

    planner = AnimalPlanner()

    animal = {
        "harvest_ready": True,
    }

    assert planner.best_action(animal) == "HARVEST"