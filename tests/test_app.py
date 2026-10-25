import pytest

from app import app
from main import greet


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_greet():
    assert greet("World") == "Hello, World! Welcome to DevOps lab."


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello, DevOps!" in response.get_data(as_text=True)


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_version(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert response.get_json() == {"version": "1.1.0"}
