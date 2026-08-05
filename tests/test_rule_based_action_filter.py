from src.rule_based_action_filter import (
    RuleBasedActionFilter,
)


def test_buy_removed():

    filt = RuleBasedActionFilter()

    actions = [
        {"action": "BUY"},
        {"action": "SELL"},
    ]

    observation = {
        "farm": {
            "money": 0,
        }
    }

    result = filt.filter_actions(
        actions,
        observation,
    )

    assert len(result) == 1
    assert result[0]["action"] == "SELL"


def test_buy_allowed():

    filt = RuleBasedActionFilter()

    actions = [
        {"action": "BUY"},
    ]

    observation = {
        "farm": {
            "money": 100,
        }
    }

    result = filt.filter_actions(
        actions,
        observation,
    )

    assert len(result) == 1


def test_count():

    filt = RuleBasedActionFilter()

    actions = [
        {"action": "BUY"},
    ]

    observation = {
        "farm": {
            "money": 0,
        }
    }

    assert (
        filt.count(
            actions,
            observation,
        )
        == 0
    )


def test_has_actions_false():

    filt = RuleBasedActionFilter()

    actions = [
        {"action": "BUY"},
    ]

    observation = {
        "farm": {
            "money": 0,
        }
    }

    assert not filt.has_actions(
        actions,
        observation,
    )


def test_has_actions_true():

    filt = RuleBasedActionFilter()

    actions = [
        {"action": "SELL"},
    ]

    observation = {
        "farm": {
            "money": 0,
        }
    }

    assert filt.has_actions(
        actions,
        observation,
    )