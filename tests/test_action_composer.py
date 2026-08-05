from src.action_composer import ActionComposer


def test_compose():

    composer = ActionComposer()

    action = composer.compose(
        farmer_actions=[["HARVEST"]],
        hand_actions=[],
        market_actions=[],
    )

    assert action["farmer"] == ["HARVEST"]


def test_market():

    composer = ActionComposer()

    action = composer.compose(
        farmer_actions=[["PASS"]],
        market_actions=[
            ["SELL", "MELON", 4]
        ],
    )

    assert action["market"][0][0] == "SELL"


def test_hands():

    composer = ActionComposer()

    action = composer.compose(
        hand_actions=[
            ["PASS"]
        ]
    )

    assert len(action["hands"]) == 1


def test_default():

    composer = ActionComposer()

    action = composer.empty()

    assert action == {
        "farmer": ["PASS"],
        "hands": [],
        "market": [],
    }


def test_return_type():

    composer = ActionComposer()

    assert isinstance(
        composer.compose(),
        dict,
    )