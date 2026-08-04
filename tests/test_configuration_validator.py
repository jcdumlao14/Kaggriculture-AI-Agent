from src.configuration_validator import (
    ConfigurationValidator,
)


def test_valid_configuration():

    validator = ConfigurationValidator()

    schema = {
        "host": str,
        "port": int,
    }

    config = {
        "host": "localhost",
        "port": 8000,
    }

    assert validator.validate(
        config,
        schema,
    )


def test_missing_key():

    validator = ConfigurationValidator()

    schema = {
        "host": str,
        "port": int,
    }

    config = {
        "host": "localhost",
    }

    assert not validator.validate(
        config,
        schema,
    )

    assert validator.error_count() == 1


def test_invalid_type():

    validator = ConfigurationValidator()

    schema = {
        "port": int,
    }

    config = {
        "port": "8000",
    }

    assert not validator.validate(
        config,
        schema,
    )


def test_errors():

    validator = ConfigurationValidator()

    validator.validate(
        {},
        {"host": str},
    )

    assert len(
        validator.errors()
    ) == 1


def test_has_errors():

    validator = ConfigurationValidator()

    validator.validate(
        {},
        {"host": str},
    )

    assert validator.has_errors()