from src.inference_request_router import (
    InferenceRequestRouter,
)


def double(payload):

    return payload * 2


def test_register():

    router = InferenceRequestRouter()

    router.register(
        "/predict",
        double,
    )

    assert router.exists("/predict")


def test_dispatch():

    router = InferenceRequestRouter()

    router.register(
        "/predict",
        double,
    )

    assert (
        router.dispatch(
            "/predict",
            10,
        )
        == 20
    )


def test_remove():

    router = InferenceRequestRouter()

    router.register(
        "/predict",
        double,
    )

    router.remove("/predict")

    assert not router.exists("/predict")


def test_list_routes():

    router = InferenceRequestRouter()

    router.register("/a", double)
    router.register("/b", double)

    assert router.list_routes() == [
        "/a",
        "/b",
    ]


def test_clear():

    router = InferenceRequestRouter()

    router.register("/a", double)
    router.register("/b", double)

    router.clear()

    assert router.list_routes() == []