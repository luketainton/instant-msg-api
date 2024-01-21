from fastapi.testclient import TestClient

from app import api

client = TestClient(api.webapp)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"detail": "App is alive."}
