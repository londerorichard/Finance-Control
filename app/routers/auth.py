from fastapi import APIRouter, HTTPException

from schemas import (
    UserCreate,
    UserLogin,
    UserUpdate,
    UserResponse,
    PasswordChange,
)

from repositories.auth_repository import (
    email_exists,
    get_user_by_email,
    insert_user,
)


router = APIRouter(prefix="/auth", tags=["Authentication"])


# ==========================================================
# ENDPOINTS
# ==========================================================


@router.post("/register", response_model=UserResponse)
def register_user(new_user: UserCreate):

    if email_exists(new_user.email):
        raise HTTPException(
            status_code=409,
            detail="User already registered"
        )

    return insert_user(new_user)


@router.post("/login", response_model=UserResponse)
def login_user(user: UserLogin):

    stored_user = get_user_by_email(user.email)

    if stored_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if stored_user["password_hash"] != user.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return UserResponse(
        id=stored_user["id"],
        name=stored_user["name"],
        email=stored_user["email"]
    )


# @router.get("/me")
# def get_me(
#     current_user = Depends(get_current_user)
# ):
#     ...




    
# @router.post("/auth/logout")
# def logout_user(user: UserAuth):

# @router.put("/auth/change-password")
# def logout_user(user: UserAuth):
#     pass

# PATCH /auth/update
# PATCH /auth/change-password
# DELETE /auth/delete-account