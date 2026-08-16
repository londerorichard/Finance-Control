from fastapi import APIRouter, HTTPException, Depends

from app.schemas import (
    UserCreate,
    UserLogin,
    UserUpdate,
    UserResponse,
    PasswordChange,
    Token
)

from app.repositories.auth_repository import (
    email_exists,
    get_user_by_email,
    insert_user,
)

from app.auth.jwt import create_access_token
from app.auth.security import verify_password
from app.auth.dependency import get_current_user
from app.services.user_service import create_user, get_user_by_email, get_user_by_id


router = APIRouter(prefix="/auth", tags=["Authentication"])


# ==========================================================
# ENDPOINTS
# ==========================================================


@router.post("/register", response_model=UserResponse)
def register_user(new_user: UserCreate):

    user = create_user(
        new_user.email,
        new_user.name,
        new_user.password,
    )

    if user is None:
        raise HTTPException(
            status_code=409,
            detail="User already registered",
        )

    return user


@router.post("/login", response_model=Token)
def login_user(user_data: UserLogin):

    user = get_user_by_email(user_data.email)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user_data.password,
        user["password_hash"],
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(user["id"])

    return {
        "access_token": token,
        "token_type": "bearer",
    }


@router.get("/me", response_model=UserResponse)
def get_me(
    current_user = Depends(get_current_user),
):
    return current_user



# @router.post("/auth/logout")
# def logout_user(user: UserAuth):

# @router.put("/auth/change-password")
# def logout_user(user: UserAuth):
#     pass

# PATCH /auth/update
# PATCH /auth/change-password
# DELETE /auth/delete-account