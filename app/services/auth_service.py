from fastapi import HTTPException

from app.auth.security import hash_password, verify_password

from app.repositories.user_repository import (
    email_exists,
    create_user,
    get_user_by_email,
    get_user_by_id,
    update_password_hash,
)

from app.schemas import UserCreate, UserResponse


def register_user(user: UserCreate) -> UserResponse:
    if email_exists(user.email):
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    password_hash = hash_password(user.password)

    return create_user(user.email, password_hash)


def login_user(email: str, password: str) -> UserResponse:
    user = get_user_by_email(email)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(password, user["password_hash"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return UserResponse(
        id=user["id"],
        email=user["email"]
    )


def change_password(
        user_id: int,
        current_password: str,
        new_password: str
    ) -> bool:

    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    stored_password_hash = user["password_hash"]

    if not verify_password(current_password, stored_password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    new_password_hash = hash_password(new_password)

    return update_password_hash(user_id, new_password_hash)

