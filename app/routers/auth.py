from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Authentication"])

class UserAuth(BaseModel):
    name: str
    email: str


users = {
    1: {
        "name": "andrew",
        "email": "andrew@gmail.com"
    }
}


@router.post("/auth/register")
def register_user(new_user: UserAuth):

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