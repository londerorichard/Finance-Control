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

    data = response.json()

    assert data["email"] == "test@example.com"
    assert "password_hash" not in data


def test_get_existing_user_by_id(client, user):
    response = client.get(f"/users/get_by_id/{user['id']}")

    assert response.status_code == 200
    assert response.json()["email"] == user["email"]


def test_get_nonexistent_user_by_id(client):
    response = client.get("/users/get_by_id/999999")

    assert response.status_code == 404




# Password Changes
# [ ] A user can change their password with valid input.
# [ ] The new password is stored as a hash.
# [ ] The new password can be verified successfully.
# [ ] The old password no longer matches the updated hash.
# [ ] An incorrect current password prevents the change, if your application requires current-password verification.


# | Test                                                | Service test | Endpoint test |
# | --------------------------------------------------- | :----------: | :-----------: |
# | A user can change their password with valid input   |       ✅      |       ✅       |
# | The new password is stored as a hash                |       ✅      |       —       |
# | The new password can be verified successfully       |       ✅      |       —       |
# | The old password no longer matches the updated hash |       ✅      |       —       |
# | An incorrect current password prevents the change   |       ✅      |       ✅       |
