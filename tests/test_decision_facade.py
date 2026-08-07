from src.decision_facade import (
    DecisionFacade,
)


def test_evaluate():

    facade = DecisionFacade()

    score = facade.evaluate(
        state_id="a",
        game_state={"money": 100},
        action="MOVE",
    )

    assert isinstance(score, float)


def test_history():

    facade = DecisionFacade()

    assert facade.history() == []


def test_clear_cache():

    facade = DecisionFacade()

    facade.workflow.service.feature_service.features(
        state_id="x",
        game_state={},
    )

    facade.clear_cache()

    assert (
        facade.workflow.service.feature_service.pipeline.cache.size()
        == 0
    )


def test_multiple_calls():

    facade = DecisionFacade()

    first = facade.evaluate(
        state_id="a",
        game_state={},
        action="MOVE",
    )

    second = facade.evaluate(
        state_id="b",
        game_state={},
        action="WAIT",
    )

    assert isinstance(first, float)
    assert isinstance(second, float)


def test_default_search_algorithm():

    facade = DecisionFacade()

    score = facade.evaluate(
        state_id="z",
        game_state={},
        action="MOVE",
    )

    assert isinstance(score, float)