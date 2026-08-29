from fastapi import APIRouter, HTTPException
from app.schemas import (CreateCategory, UpdateCategory, ResponseCategory)
from app.services.categories_service import (
    create_category, 
    list_categories, 
    get_category_by_id, 
    get_category_by_name,
    update_category,
    delete_category)


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
def get_category_by_name_endpoint(category_name: str):

    category = get_category_by_name(category_name)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return ResponseCategory(
        id=category["id"], 
        name=category["name"]
    )


@router.get("/get-by-id/{id}", response_model=ResponseCategory)
def get_category_by_id_endpoint(category_id: int):

    category = get_category_by_id(category_id)
    
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return ResponseCategory(
        id=category["id"],
        name=category["name"]
    )


@router.put("/update-category/{category_id}", response_model=ResponseCategory)
def update_category(category_id: int, category_updated: UpdateCategory):
    
    category = get_category_by_id(category_id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    update_category(category_id, category_updated)

    updated_category = get_category_by_id(category_id)

    return ResponseCategory(
        id=updated_category["id"],
        name=updated_category["name"]
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
