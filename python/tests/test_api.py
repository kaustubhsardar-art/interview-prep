import pytest

from api.api import app


def test_greeting():
    resp = app.test_client().get("/greeting/oooo")
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Welcome to Verkada !"}


def test_unknown_route_returns_404():
    assert app.test_client().get("/nope").status_code == 404


def test_greeting_accepts_post():
    resp = app.test_client().post("/greeting/oooo")
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Welcome to Verkada !"}


def test_post_greeting_with_name():
    resp = app.test_client().post("/greeting", json={"name": "x"})
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Hello x"}


@pytest.mark.parametrize(
    "kwargs",
    [
        {"json": {}},
        {"json": {"name": ""}},
        {"json": {"name": "   "}},
        {"json": {"name": 5}},
        {"json": ["x"]},
        {"data": "not json"},
        {},
    ],
)
def test_post_greeting_bad_input(kwargs):
    resp = app.test_client().post("/greeting", **kwargs)
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_post_greeting_rejects_get():
    assert app.test_client().get("/greeting").status_code == 405


@pytest.mark.parametrize("path", ["/greeting", "/greeting/"])
def test_post_greeting_trailing_slash(path):
    resp = app.test_client().post(path, json={"name": "x"})
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Hello x"}
