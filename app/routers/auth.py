from fastapi import APIRouter, HTTPException, Depends

from app.schemas import (
    UserCreate,
    UserLogin,
    UserUpdate,
    UserResponse,
    PasswordChange,
    Token
)

from app.auth.jwt import create_access_token
from app.auth.dependency import get_current_user
from app.services.auth_service import create_user, change_password, login_user
import sqlite3

router = APIRouter(prefix="/auth", tags=["Authentication"])


# ==========================================================
# ENDPOINTS
# ==========================================================


@router.post("/register", response_model=UserResponse)
def register_user(new_user: UserCreate):

    try:
        return create_user(
            new_user.email,
            new_user.password
        )

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )


@router.post("/login", response_model=Token)
def login_user_endpoint(user_data: UserLogin):

    user = login_user(
        user_data.email,
        user_data.password
    )

    token = create_access_token(user["id"])

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/me", response_model=UserResponse)
def get_me(
    current_user = Depends(get_current_user),
):
    return current_user


@router.put("/change-password")
def change_password_endpoint(
    password_data: PasswordChange,
    current_user=Depends(get_current_user)
):

    change_password(
        current_user["id"],
        password_data.current_password,
        password_data.new_password
    )

    return {"message": "Password changed successfully"}


# @router.post("/auth/logout")
# def logout_user(user: UserAuth):

# PATCH /auth/update
# DELETE /auth/delete-account

