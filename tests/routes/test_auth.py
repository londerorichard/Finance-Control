from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "email": "testinf76ffg@example.com",
            "password": "TestingPassword123!"
        }
    )

    assert response.status_code == 200
