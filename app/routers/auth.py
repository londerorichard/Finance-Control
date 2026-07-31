from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, Field

router = APIRouter(prefix="/auth", tags=["Authentication"])

# ==========================================================
# CLASSES
# ==========================================================


class UserCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
        description="User full name",
        examples=["Richard"]
    ) 
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=64,
        description="User password",
        examples=["MyPassword123"]
    )


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=64,
        description="User password",
        examples=["MyPassword123"]
    )


class UserResponse(BaseModel):
    id: int
    name: str = Field(
        min_length=2,
        max_length=50,
        description="User full name",
        examples=["Richard"]
    )
    email: EmailStr


class PasswordChange(BaseModel):
    current_password: str
    new_password: str = Field(min_length=8)


class UserUpdate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
        description="User full name",
        examples=["Richard"]
    )
    email: EmailStr | None = None


# class RefreshToken(BaseModel):
#     refresh_token: str


users = {
    1: {
        "name": "andrew",
        "email": "andrew@gmail.com"
    }
}


@router.post("/auth/register")
def register_user(new_user: UserCreate):

    # Check if the email already exists
    for user in users.values():
        if user["email"] == new_user.email:
            return {"data": "User already registered"}

    # Generate the next ID
    new_id = max(users.keys()) + 1 if users else 1

    # Save the new user
    users[new_id] = {
        "name": new_user.name,
        "email": new_user.email
    }

    # Return the created user
    return {
        "id": new_id,
        "name": new_user.name,
        "email": new_user.email
    }

# @router.post("/auth/login")
# def login_user(new_user: UserAuth):
#     pass
# Make this once you have learned SQL persistence


# @router.post("/auth/logout")
# def logout_user(user: UserAuth):
#     pass


# @router.get("/auth/me")
# def logout_user(user: UserAuth):
#     pass
# Get authenticated user information


# @router.put("/auth/change-password")
# def logout_user(user: UserAuth):
#     pass
