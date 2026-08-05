from src.legal_action_generator import (
    LegalActionGenerator,
)


def test_single_harvest():

    generator = LegalActionGenerator()

    observation = {
        "farm": {
            "tiles": [
                [
                    {
                        "kind": "PLANT",
                        "mature": True,
                    }
                ]
            ]
        }
    }

    actions = generator.generate(observation)

    assert len(actions) == 1

    assert actions[0]["action"] == "HARVEST"


def test_no_actions():

    generator = LegalActionGenerator()

    observation = {
        "farm": {
            "tiles": [
                [
                    {
                        "kind": "PLANT",
                        "mature": False,
                    }
                ]
            ]
        }
    }

    assert generator.generate(observation) == []


def test_count():

    generator = LegalActionGenerator()

    observation = {
        "farm": {
            "tiles": [
                [
                    {
                        "kind": "PLANT",
                        "mature": True,
                    }
                ]
            ]
        }
    }

    assert generator.count(observation) == 1


def test_has_actions():

    generator = LegalActionGenerator()

    observation = {
        "farm": {
            "tiles": [
                [
                    {
                        "kind": "PLANT",
                        "mature": True,
                    }
                ]
            ]
        }
    }

    assert generator.has_actions(observation)


def test_empty_farm():

    generator = LegalActionGenerator()

    observation = {
        "farm": {
            "tiles": []
        }
    }

    assert generator.generate(observation) == []