from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/categories", tags=["Categories"])

# ==========================================================
# CLASSES
# ==========================================================

class Category(BaseModel):
    name: str = Field(
            min_length=2,
            max_length=50,
            description="User full name",
            examples=["Income"]
        )

    user_id: int 

class CreateCategory(BaseModel):
    name: str = Field(
            min_length=2,
            max_length=50,
            description="User full name",
            examples=["Income"]
        )
    
class UpdateCategory(BaseModel):
    name: str = Field(
            min_length=2,
            max_length=50,
            description="User full name",
            examples=["Income"]
        )
    
class ResponseCategory(BaseModel):
    id: int
    name: str


categories = {
    1: {
        "category_name": "Food",
        "user_id": 1
    },
    2: {
        "category_name": "Transport",
        "user_id": 1
    }
}

@router.get("/list")
def list_categories():
    return categories


@router.get("/get-by-name", response_model=ResponseCategory)
def get_category_by_name(category_name: str):

    for category_id, category in categories.items():
        if category["category_name"] == category_name:
            return ResponseCategory(
                id=category_id,
                name=category["category_name"]
            )

    raise HTTPException(
        status_code=404,
        detail="Category not found"
    )


@router.get("/get-by-id/{id}", response_model=ResponseCategory)
def get_category_by_id(id: int):

    if id not in categories.keys():



# GET	/categories/{id}	Get category
# POST	/categories	Create category
# PUT	/categories/{id}	Update category
# DELETE	/categories/{id}	Delete category"