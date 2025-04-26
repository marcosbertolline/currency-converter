import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test cases for the conversion API
def test_conversion_success():
    response = client.post("/api/convert", json={
        "user_id": "user_test",
        "source_currency": "EUR",
        "source_amount": 10,
        "target_currency": "USD"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "user_test"
    assert data["source_currency"] == "EUR"
    assert data["target_currency"] == "USD"
    assert "conversion_rate" in data
    assert "target_amount" in data

# Test cases for the conversion API with missing EUR currency
def test_conversion_error_missing_eur():
    response = client.post("/api/convert", json={
        "user_id": "user_test",
        "source_currency": "USD",
        "source_amount": 10,
        "target_currency": "JPY"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "At least one of the currencies must be EUR."

# Test cases for the conversion API with invalid data currency
def test_conversion_unsupported_currency():
    response = client.post("/api/convert", json={
        "user_id": "user_test",
        "source_currency": "EUR",
        "source_amount": 10,
        "target_currency": "ABC"
    })
    assert response.status_code == 400
