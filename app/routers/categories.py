from fastapi import APIRouter, HTTPException
from app.schemas import (CreateCategory, UpdateCategory, ResponseCategory)
from app.services.categories_service import create_category, list_categories


router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/create", response_model=ResponseCategory, status_code=201)
def create_category_endpoint(new_category: CreateCategory):

    category_id = create_category(
        name=new_category.name,
        user_id=new_category.user_id
    )

    return ResponseCategory(
        id=category_id,
        name=new_category.name
    )


@router.get("/list", response_model=ResponseCategory)
def list_categories_endpoint():

    return list_categories()


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

    if id not in categories:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    category = categories[id]

    return ResponseCategory(
        id=id,
        name=category["category_name"]
    )


@router.put("/update-category/{id}", response_model=ResponseCategory)
def update_category(id: int, category_updated: UpdateCategory):

    if id not in categories:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    categories[id]["category_name"] = category_updated.name

    return ResponseCategory(
        id=id,
        name=category_updated.name
    )


@router.delete("/delete-category/{id}")
def delete_category(category_id: int):

    if category_id not in categories:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    category_name = categories[category_id]["category_name"]

    del categories[category_id]

    return {
        "success": f"{category_name} successfully deleted"
    }
