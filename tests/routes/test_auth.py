def test_login_valid_credentials(client, test_user):
    response = client.post(
        "/auth/login",
        data={
            "username": test_user.email,
            "password": "MyPassword123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_access_protected_endpoint_without_token(client):
    response = client.get("/auth/me")

    assert response.status_code == 401


def test_access_protected_endpoint_with_invalid_token(client):
    response = client.get(
        "/auth/me",
        headers={
            "Authorization": "Bearer invalid-token"
        }
    )

    assert response.status_code == 401


# |---|---|
# | Register valid user | 201 Created |
# | Register duplicate email | 409 Conflict (or your chosen error status) |
# | Login with valid credentials | 200 OK + access token |
# | Login with wrong password | 401 Unauthorized |
# | Login with nonexistent email | 401 Unauthorized |
# | Access protected endpoint without token | 401 Unauthorized |
# | Access protected endpoint with invalid token | 401 Unauthorized |
# | Access protected endpoint with valid token | 200 OK |


# Authentication
# POST /auth/register

#     [ ] valid registration
#     [ ] invalid email
#     [ ] invalid password
#     [ ] duplicate email

# Then:

# POST /auth/login

#     [ ] correct credentials
#     [ ] wrong password
#     [ ] nonexistent user