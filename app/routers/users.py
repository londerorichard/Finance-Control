from fastapi import APIRouter, HTTPException
from services.user_service import create_user, get_user_by_id, list_users


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