from fastapi import APIRouter, HTTPException
from app.services.user_service import (create_user, get_user_by_id, list_users)
from app.schemas import (UserCreate, UserLogin, UserResponse)


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def register_user(email: str, password: str):

    user_id = create_user(email, password)

    if user_id is None:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    return {
        "message": "User created",
        "id": user_id
    }


# POST	/auth/register	Register a new user
# POST	/auth/login	Authenticate user
# POST	/auth/logout	Logout current user
# GET	/auth/me	Get authenticated user information
# PUT	/auth/change-password	Change user password