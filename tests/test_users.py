"""Tests for user endpoints."""

from fastapi.testclient import TestClient


def test_create_user(client: TestClient) -> None:
    """Test creating a user."""
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "full_name": "Test User",
    }
    response = client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["username"] == user_data["username"]
    assert "id" in data


def test_list_users(client: TestClient) -> None:
    """Test listing users."""
    # Create a user first
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "full_name": "Test User",
    }
    client.post("/api/v1/users/", json=user_data)

    # List users
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_user(client: TestClient) -> None:
    """Test getting a user by ID."""
    # Create a user first
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "full_name": "Test User",
    }
    create_response = client.post("/api/v1/users/", json=user_data)
    user_id = create_response.json()["id"]

    # Get the user
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["email"] == user_data["email"]


def test_get_nonexistent_user(client: TestClient) -> None:
    """Test getting a user that doesn't exist."""
    response = client.get("/api/v1/users/99999")
    assert response.status_code == 404


def test_delete_user(client: TestClient) -> None:
    """Test deleting a user."""
    # Create a user first
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "full_name": "Test User",
    }
    create_response = client.post("/api/v1/users/", json=user_data)
    user_id = create_response.json()["id"]

    # Delete the user
    response = client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 204

    # Verify user is deleted
    get_response = client.get(f"/api/v1/users/{user_id}")
    assert get_response.status_code == 404
