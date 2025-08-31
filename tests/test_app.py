import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    # check if HTML page contains expected heading
    assert b"ACEst Fitness & Gym" in response.data

def test_members(client):
    response = client.get("/members")
    assert response.status_code == 200
    data = response.get_json()
    assert "1" in data

def test_single_member(client):
    response = client.get("/membership/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Taylor"

def test_invalid_member(client):
    response = client.get("/membership/999")
    assert response.status_code == 404

def test_workouts(client):
    response = client.get("/workouts")
    assert response.status_code == 200
    data = response.get_json()
    assert any(w["name"] == "Cardio Blast" for w in data)

def test_bmi_valid(client):
    response = client.get("/bmi?weight=70&height=1.75")
    assert response.status_code == 200
    data = response.get_json()
    assert 22 < data["BMI"] < 23  # expected BMI range

def test_bmi_invalid(client):
    response = client.get("/bmi?weight=abc&height=xyz")
    assert response.status_code == 400
