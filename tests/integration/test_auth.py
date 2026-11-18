from app.auth.jwt import create_access_token
from app.services.auth_service import create_user, login_user
from app.auth.dependency import get_current_user

def test_register_user(db_session):
    email = "newuser@example.com"
    password = "TestingPassword123!"

    user = create_user(
        db_session,
        email=email,
        password=password,
    )

    assert user is not None
    assert user.email == email
    assert user.password_hash != password


def test_login_valid_credentials(db_session, test_user):
    user = login_user(
        db_session,
        email=test_user.email,
        password="MyPassword123",
    )

    assert user is not None
    assert user.email == test_user.email


def test_login_wrong_password(db_session, test_user):
    user = login_user(
        db_session,
        email=test_user.email,
        password="WrongPassword123",
    )

    assert user is None


def test_login_nonexistent_email(db_session):
    user = login_user(
        db_session,
        email="nonexistent@example.com",
        password="MyPassword123",
    )

    assert user is None


def test_token_for_nonexistent_user(db_session):
    token = create_access_token(999999)

    user = get_current_user(
        db_session,
        token=token,
    )

    assert user is None


def test_deleted_user_cannot_use_old_token(db_session, test_user):
    token = create_access_token(test_user.id)

    db_session.delete(test_user)
    db_session.commit()

    user = get_current_user(
        db_session,
        token=token,
    )

    assert user is None


