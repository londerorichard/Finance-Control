from fastapi import APIRouter, HTTPException, Depends, Request, Response
from fastapi.responses import RedirectResponse
from app.auth.oauth import oauth
from app.auth.jwt import create_access_token
from app.auth.dependency import get_current_user
import sqlite3
from app.schemas import (
    UserCreate,
    UserLogin,
    UserUpdate,
    UserResponse,
    PasswordChange,
    Token
)
from app.services.auth_service import (
    create_user, 
    change_password, 
    login_user, 
    get_user_by_google_id, 
    get_user_by_email,
    create_google_user
    )


router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=201)
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


@router.post("/login")
def login_user_endpoint(
    user_data: UserLogin,
    response: Response
):
    user = login_user(
        user_data.email,
        user_data.password
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(user["id"])

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,  # Development only: use HTTPS and True in production
        samesite="lax",
        max_age=60 * 60 * 24 * 7,
        path="/"
    )

    return {"message": "Login successful"}


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


@router.get("/google")
async def google_login(request: Request):
    redirect_uri = request.url_for("google_callback")

    return await oauth.google.authorize_redirect(
        request,
        redirect_uri
    )


@router.get("/google/callback", name="google_callback")
async def google_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)

    user_info = token.get("userinfo")

    if not user_info:
        return RedirectResponse(
            url="/login?error=google_auth_failed",
            status_code=303,
        )

    google_id = user_info.get("sub")
    email = user_info.get("email")
    email_verified = user_info.get("email_verified", False)

    if not google_id or not email or not email_verified:
        return RedirectResponse(
            url="/login?error=google_auth_failed",
            status_code=303,
        )

    user = get_user_by_google_id(google_id)

    if user is None:
        existing_user = get_user_by_email(email)

        if existing_user is not None:
            return RedirectResponse(
                url="/login?error=account_exists",
                status_code=303,
            )

        user = create_google_user(email, google_id)

    user_id = user["id"]

    access_token = create_access_token(user_id)

    response = RedirectResponse(
        url="/dashboard",
        status_code=303,
    )

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,  # Use True in production with HTTPS
        samesite="lax",
        max_age=30 * 60,
        path="/",
    )

    return response


@router.post("/logout")
def logout_user_endpoint(response: Response):
    response.delete_cookie(
        key="access_token",
        path="/",
        secure=False,  # Match the development cookie settings
        httponly=True,
        samesite="lax"
    )

    return {"message": "Logged out successfully"}



# PATCH /auth/update
# DELETE /auth/delete-account

