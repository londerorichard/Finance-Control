from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Depends
from app.schemas import (
    TransactionCreate,
    TransactionResponse,
    TransactionUpdate
)
from app.services.transaction_service import (
    create_transaction, 
    list_transactions, 
    calculate_balance,
    get_single_transaction,
    update_transaction,
    delete_transaction)

from app.services.categories_service import get_category_for_user
from app.auth.dependency import get_current_user


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.post("/create", response_model=TransactionResponse)
def create_transaction_endpoint(
    new_transaction: TransactionCreate,
    current_user=Depends(get_current_user)
):
    user_id = current_user["id"]

    if new_transaction.category_id is not None:
        category = get_category_for_user(
            new_transaction.category_id,
            user_id
        )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

    transaction_id = create_transaction(
        user_id=user_id,
        amount=new_transaction.amount,
        transaction_type=new_transaction.transaction_type,
        description=new_transaction.description,
        category_id=new_transaction.category_id,
        account=new_transaction.account
    )

    return TransactionResponse(
        id=transaction_id,
        user_id=user_id,
        amount=new_transaction.amount,
        transaction_type=new_transaction.transaction_type,
        description=new_transaction.description,
        category_id=new_transaction.category_id,
        account=new_transaction.account
    )


@router.get("/list", response_model=list[TransactionResponse])
def list_transaction_endpoint(
    current_user=Depends(get_current_user)
):
    user_id = current_user["id"]

    transactions = list_transactions(user_id)

    return [
        TransactionResponse(
            id=transaction["id"],
            user_id=transaction["user_id"],
            amount=transaction["amount"],
            transaction_type=transaction["transaction_type"],
            description=transaction["description"],
            category_id=transaction["category_id"],
            account=transaction["account"]
        )
        for transaction in transactions
    ]


@router.get("/balance")
def get_balance_endpoint(current_user=Depends(get_current_user)):
    user_id = current_user["id"]

    balance = calculate_balance(user_id)

    return {
        "balance": balance
    }


@router.get("/transactions/{transaction_id}",response_model=TransactionResponse)
def get_single_transaction_endpoint(
    transaction_id: int,
    current_user=Depends(get_current_user)
):
    user_id = current_user["id"]

    transaction = get_single_transaction(
        user_id,
        transaction_id
    )

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return TransactionResponse(
        id=transaction["id"],
        user_id=transaction["user_id"],
        amount=transaction["amount"],
        transaction_type=transaction["transaction_type"],
        description=transaction["description"],
        category_id=transaction["category_id"],
        account=transaction["account"]
    )


@router.patch("/update/{transaction_id}", response_model=TransactionResponse)
def update_transaction_endpoint(
    transaction_id: int,
    updated_transaction: TransactionUpdate,
    current_user=Depends(get_current_user)
):
    update_data = updated_transaction.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No fields provided for update"
        )

    user_id = current_user["id"]

    transaction = get_single_transaction(
        user_id,
        transaction_id
    )

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    if "category_id" in update_data and update_data["category_id"] is not None:
        category = get_category_for_user(
            update_data["category_id"],
            user_id
        )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

    updated = update_transaction(
        user_id=user_id,
        transaction_id=transaction_id,
        **update_data
    )

    return TransactionResponse(**dict(updated))


@router.delete("/delete/{transaction_id}")
def delete_transaction_endpoint(transaction_id: int,current_user=Depends(get_current_user)):
    user_id = current_user["id"]

    transaction = get_single_transaction(
        user_id,
        transaction_id
    )

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    delete_transaction(
        user_id,
        transaction_id
    )

    return {
        "success": f"Transaction {transaction_id} successfully deleted"
    }