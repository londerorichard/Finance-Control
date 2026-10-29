from tests.conftest import client


def test_create_user_endpoint(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "password": "SecurePassword123!"
        }
    )

    assert response.status_code == 201