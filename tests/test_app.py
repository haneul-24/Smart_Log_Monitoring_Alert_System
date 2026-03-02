import pytest 
from fastapi.testclient import TestClient
from src.python_API import app


client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_health():
    response = client.get("health/")
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}


def test_create_and_delete_log():
    log_data = {
        "service": "Order-service",
        "level": "info",
        "meassage": "This is a test log"
    }

    create_response = client.post("/logs", json=log_data)
    assert create_response.status_code in [200, 409]

    if create_response.status_code == 200:
        log_id = create_response.json()["id"]

    delete_reponse = client.delete(f"/logs/{log_id}")
    assert delete_reponse.status_code == 200
    assert delete_reponse.json()["message"] == "Deleted Successfully.."


