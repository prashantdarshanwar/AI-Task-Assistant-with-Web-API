"""
API Tests
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))




from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    """
    Test health endpoint.
    """

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "running"


def test_get_tasks():
    """
    Test GET /tasks
    """

    response = client.get("/tasks")

    assert response.status_code == 200

    assert isinstance(response.json(), list)


def test_create_task():
    """
    Test POST /assistant
    """

    payload = {
        "query": "Create task to fix login bug tomorrow high priority"
    }

    response = client.post(
        "/assistant",
        json=payload
    )

    assert response.status_code in [200, 201]

    data = response.json()

    assert "title" in data
    assert "priority" in data
    assert "created_at" in data


def test_invalid_request():

    response = client.post(
        "/assistant",
        json={}
    )

    assert response.status_code in [400, 422]