import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to ACEest Fitness & Gym!" in response.data

def test_members(client):
    response = client.get('/members')
    assert response.status_code == 200
    assert b"Taylor" in response.data
