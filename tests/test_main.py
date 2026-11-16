from fastapi.testclient import TestClient

from fastapi_cicd import __version__
from fastapi_cicd.main import app

client = TestClient(app)


def test_read_root_returns_service_metadata() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "service": "fastapi-cicd",
        "version": __version__,
        "status": "running",
    }


def test_health_check_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
