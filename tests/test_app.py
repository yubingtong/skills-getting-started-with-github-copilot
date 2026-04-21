import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_signup_activity_success():
    # Arrange
    activity_name = "Chess Club"
    email = "student1@mergington.edu"
    # Ensure activity exists (depends on app's initial state)
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert
    assert response.status_code == 200
    assert f"Signed up {email}" in response.json()["message"]

def test_signup_activity_duplicate():
    # Arrange
    activity_name = "Chess Club"
    email = "student2@mergington.edu"
    # Act
    client.post(f"/activities/{activity_name}/signup?email={email}")
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert
    assert response.status_code == 400 or response.status_code == 409
    assert "already registered" in response.json().get("detail", "").lower() or response.status_code == 400
