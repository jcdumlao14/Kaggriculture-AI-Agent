from src.decision_pipeline import DecisionPipeline


def test_context():

    pipeline = DecisionPipeline()

    observation = {
        "player": 0,
        "day": 2,
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

    context = pipeline.build_context(
        observation,
    )

    assert "algorithm" in context


def test_best_action_none():

    pipeline = DecisionPipeline()

    observation = {
        "farms": [
            {
                "tiles": [],
            }
        ]
    }

    assert (
        pipeline.best_action(
            observation,
        )
        is None
    )


def test_rank_returns_list():

    pipeline = DecisionPipeline()

    observation = {
        "farms": [
            {
                "tiles": [],
            }
        ]
    }

    assert isinstance(
        pipeline.rank_actions(
            observation,
        ),
        list,
    )


def test_score():

    pipeline = DecisionPipeline()

    value = pipeline.score(
        {
            "action": "PASS",
        }
    )

    assert isinstance(
        value,
        (int, float),
    )


def test_legal_actions():

    pipeline = DecisionPipeline()

    observation = {
        "farms": [
            {
                "tiles": [],
            }
        ]
    }

    actions = pipeline.legal_actions(
        observation,
    )

    assert isinstance(
        actions,
        list,
    )