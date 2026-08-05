from src.decision_executor import (
    DecisionExecutor,
)


def make_observation():

    return {
        "player": 0,
        "day": 1,
        "hour": 0,
        "farms": [
            {
                "money": 1000,
                "tiles": [],
                "hands": [],
            }
        ],
        "private": {
            "shed": {},
        },
    }


def test_context():

    executor = DecisionExecutor()

    context = executor.context(
        make_observation(),
    )

    assert "algorithm" in context


def test_ranked_actions():

    executor = DecisionExecutor()

    assert isinstance(
        executor.ranked_actions(
            make_observation(),
        ),
        list,
    )


def test_action_count():

    executor = DecisionExecutor()

    assert isinstance(
        executor.action_count(
            make_observation(),
        ),
        int,
    )


def test_has_action():

    executor = DecisionExecutor()

    assert isinstance(
        executor.has_action(
            make_observation(),
        ),
        bool,
    )


def test_execute():

    executor = DecisionExecutor()

    action = executor.execute(
        make_observation(),
    )

    assert (
        action is None
        or isinstance(action, dict)
    )