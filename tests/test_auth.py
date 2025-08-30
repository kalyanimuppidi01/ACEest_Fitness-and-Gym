import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_login_success(client):
    response = client.post("/login", json={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    data = response.get_json()
    assert "access_token" in data

def test_login_failure(client):
    response = client.post("/login", json={"username": "wrong", "password": "wrong"})
    assert response.status_code == 401
    data = response.get_json()
    assert "error" in data

def test_protected_route(client):
    # First login to get token
    login_resp = client.post("/login", json={"username": "admin", "password": "admin"})
    token = login_resp.get_json()["access_token"]

    # Access protected route
    response = client.get("/protected", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.get_json()
    assert "authorized" in data["message"].lower()
