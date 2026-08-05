from src.candidate_action_generator import (
    CandidateActionGenerator,
)


def test_generate():

    generator = CandidateActionGenerator()

    actions = generator.generate({})

    assert len(actions) == 7


def test_supports():

    generator = CandidateActionGenerator()

    assert generator.supports("PLANT")


def test_not_supported():

    generator = CandidateActionGenerator()

    assert not generator.supports("FLY")


def test_action_count():

    generator = CandidateActionGenerator()

    assert generator.action_count() == 7


def test_actions():

    generator = CandidateActionGenerator()

    actions = generator.actions()

    assert "HARVEST" in actions
    assert "BUY" in actions