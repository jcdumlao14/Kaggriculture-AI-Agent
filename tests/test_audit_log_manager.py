from src.audit_log_manager import AuditLogManager


def test_log():

    manager = AuditLogManager()

    manager.log(
        "deploy",
        "alice",
        "Deployed Policy v1",
    )

    assert manager.count() == 1


def test_all_logs():

    manager = AuditLogManager()

    manager.log(
        "login",
        "alice",
        "Successful login",
    )

    logs = manager.all_logs()

    assert len(logs) == 1
    assert logs[0]["event"] == "login"


def test_filter_by_event():

    manager = AuditLogManager()

    manager.log(
        "deploy",
        "alice",
        "Policy v1",
    )

    manager.log(
        "predict",
        "bob",
        "Prediction request",
    )

    manager.log(
        "deploy",
        "charlie",
        "Policy v2",
    )

    deploy_logs = manager.filter_by_event(
        "deploy"
    )

    assert len(deploy_logs) == 2


def test_clear():

    manager = AuditLogManager()

    manager.log(
        "login",
        "alice",
        "Logged in",
    )

    manager.clear()

    assert manager.count() == 0


def test_timestamp():

    manager = AuditLogManager()

    manager.log(
        "deploy",
        "alice",
        "Policy",
    )

    log = manager.all_logs()[0]

    assert "timestamp" in log