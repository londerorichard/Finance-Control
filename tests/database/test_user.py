from app.services.auth_service import create_user, get_user_by_email, get_user_by_id
from app.auth.security import verify_password


def test_create_user(db_connection):
    email = "te3st43b6ing@gmail.com"
    password = "cowenconew3$"

    user = create_user(email, password)

    # Verify the returned user
    assert user is not None
    assert user.id is not None
    assert user.email == email

    # Verify the user was persisted in the database
    cursor = db_connection.cursor()

    cursor.execute(
        """
        SELECT id, email, password_hash
        FROM users
        WHERE email = ?
        """,
        (email,),
    )

    db_user = cursor.fetchone()

    assert db_user is not None
    assert db_user["id"] == user.id
    assert db_user["email"] == email

    # Verify the password was hashed correctly
    assert db_user["password_hash"] != password
    assert verify_password(password, db_user["password_hash"])


def test_get_user_by_id():
    email = "tes2t_user_id@example.com"
    password = "TestPassword123!"

    created_user = create_user(email, password)

    user = get_user_by_id(created_user.id)

    assert user is not None
    assert user["id"] == created_user.id
    assert user["email"] == email


def test_get_user_by_email():
    email = "t6est_user_email@example.com"
    password = "TestPassword123!"

    created_user = create_user(email, password)

    user = get_user_by_email(email)

    assert user is not None
    assert user["id"] == created_user.id
    assert user["email"] == email




