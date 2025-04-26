from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test cases for the transaction listing API with no transactions
def test_list_transactions_empty():
    user_id = "no_transactions_user"
    response = client.get(f"/api/transactions/{user_id}")
    assert response.status_code == 200
    assert response.json() == []

# Test cases for the transaction listing API with transactions
def test_list_transactions():
    user_id = "user_test"
    client.post("/api/convert", json={
        "user_id": user_id,
        "source_currency": "EUR",
        "source_amount": 20,
        "target_currency": "USD"
    })

    response = client.get(f"/api/transactions/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["user_id"] == user_id
