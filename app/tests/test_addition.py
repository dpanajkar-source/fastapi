from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime
import pytest

client = TestClient(app)

def test_addition_endpoint():
    request_payload = {
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }
    response = client.post("/addition", json=request_payload)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["batchid"] == "id0101"
    assert response_data["response"] == [3, 7]
    assert response_data["status"] == "complete"
    assert "started_at" in response_data
    assert "completed_at" in response_data

def test_invalid_payload():
    request_payload = {
        "batchid": "id0102",
        "payload": "invalid"
    }
    response = client.post("/addition", json=request_payload)
    assert response.status_code == 422
