from src.decision_engine_v2 import (
    DecisionEngineV2,
)


def test_choose_none():

    engine = DecisionEngineV2()

    observation = {
        "farm": {
            "tiles": []
        }
    }

    assert engine.choose_action(observation) is None


def test_choose_harvest():

    engine = DecisionEngineV2()

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

    action = engine.choose_action(observation)

    assert action["action"] == "HARVEST"


def test_choose_actions():

    engine = DecisionEngineV2()

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

    actions = engine.choose_actions(observation)

    assert len(actions) == 1


def test_action_position():

    engine = DecisionEngineV2()

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

    action = engine.choose_action(observation)

    assert action["position"] == (0, 0)


def test_multiple_tiles():

    engine = DecisionEngineV2()

    observation = {
        "farm": {
            "tiles": [
                [
                    {
                        "kind": "PLANT",
                        "mature": True,
                    },
                    {
                        "kind": "PLANT",
                        "mature": True,
                    },
                ]
            ]
        }
    }

    actions = engine.choose_actions(observation)

    assert len(actions) == 2

def test_endgame_sell_priority():
    ...

def test_late_turn_priority():
    ...

def test_midgame_behavior():
    ...

def test_early_game_behavior():
    ...

def test_phase_context_available():
    ...
  