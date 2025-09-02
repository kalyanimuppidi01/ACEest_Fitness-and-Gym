import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# ---------------- Home / UI ----------------
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"ACEst Fitness & Gym" in response.data

# ---------------- Members ----------------
def test_members(client):
    response = client.get("/members")
    assert response.status_code == 200
    data = response.get_json()
    assert "1" in data  # "1" because jsonify(members) converts int keys to strings

def test_single_member(client):
    response = client.get("/membership/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Taylor"

def test_invalid_member(client):
    response = client.get("/membership/999")
    assert response.status_code == 404

# ---------------- Workouts / Trainers / Classes ----------------
def test_workouts(client):
    response = client.get("/workouts")
    assert response.status_code == 200
    data = response.get_json()
    assert any(w["name"] == "Cardio Blast" for w in data)

def test_trainers(client):
    response = client.get("/trainers")
    assert response.status_code == 200
    data = response.get_json()
    assert any(t["name"] == "Coach Mike" for t in data)

def test_classes(client):
    response = client.get("/classes")
    assert response.status_code == 200
    data = response.get_json()
    assert any(c["name"] == "Morning Yoga" for c in data)

# ---------------- BMI ----------------
def test_bmi_valid(client):
    response = client.get("/bmi?weight=70&height=1.75")
    assert response.status_code == 200
    data = response.get_json()
    assert 22 < data["BMI"] < 23  # expected ~22.86

def test_bmi_invalid(client):
    response = client.get("/bmi?weight=abc&height=xyz")
    assert response.status_code == 400

# ---------------- JWT Authentication ----------------
def test_login_success(client):
    response = client.post("/login", json={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    data = response.get_json()
    assert "access_token" in data

def test_login_failure(client):
    response = client.post("/login", json={"username": "wrong", "password": "wrong"})
    assert response.status_code == 401

def test_protected_with_token(client):
    # First login to get token
    login_response = client.post("/login", json={"username": "admin", "password": "admin"})
    token = login_response.get_json()["access_token"]

    # Use token for protected route
    response = client.get("/protected", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.get_json()
    assert "authorized" in data["message"].lower()

def test_protected_without_token(client):
    response = client.get("/protected")
    assert response.status_code == 401
