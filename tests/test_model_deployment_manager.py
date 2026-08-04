from src.model_deployment_manager import (
    ModelDeploymentManager,
)


def test_deploy():

    manager = ModelDeploymentManager()

    manager.deploy(
        "Policy",
        "v1",
    )

    assert manager.is_deployed("Policy")


def test_get():

    manager = ModelDeploymentManager()

    manager.deploy(
        "Policy",
        "v2",
    )

    deployment = manager.get("Policy")

    assert deployment["version"] == "v2"


def test_status():

    manager = ModelDeploymentManager()

    manager.deploy(
        "Policy",
        "v1",
    )

    assert manager.status("Policy") == "deployed"


def test_rollback():

    manager = ModelDeploymentManager()

    manager.deploy(
        "Policy",
        "v2",
    )

    manager.rollback(
        "Policy",
        "v1",
    )

    assert (
        manager.get("Policy")["version"]
        == "v1"
    )


def test_undeploy():

    manager = ModelDeploymentManager()

    manager.deploy(
        "Policy",
        "v1",
    )

    manager.undeploy("Policy")

    assert not manager.is_deployed(
        "Policy"
    )