from fastapi import HTTPException, APIRouter
from app.schemas import UserUpdate, UserResponse
from app.repositories.user_repository import get_user_by_id, update_user_profile, delete_user_account

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/get_by_id/{user_id}", response_model=UserResponse)
def get_user_by_id_endpoint(user_id: int):

    user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=404, detail="User not found"
        )

    return {
        "id": user["id"],
        "email": user["email"]
    }


@router.put("/update/{user_id}", response_model=UserUpdate)
def update_user_profile_endpoint(user_id: int, new_email: str):

    user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=404, detail="User not found"
        )

    user = update_user_profile(user_id, new_email)

    return {
        "id": user["id"],
        "email": user["email"]
    }


@router.delete("/delete_profile/{user_id}")
def delete_user_profile_endpoint(user_id: int):

    user = get_user_by_id(user_id)
    
    if not user:
        raise HTTPException(
            status_code=404, detail="User not found"
        )

    return delete_user_account(user_id)