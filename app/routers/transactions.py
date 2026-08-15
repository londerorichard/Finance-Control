from fastapi import APIRouter, HTTPException
from app.schemas import (
    TransactionCreate,
    TransactionResponse
)
from app.services.transaction_service import create_transaction


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.post("/create", response_model=TransactionResponse)
def create_transaction_endpoint(new_transaction: TransactionCreate):

    transaction_id = create_transaction(
        user_id=new_transaction.user_id,
        amount=new_transaction.amount,
        transaction_type=new_transaction.transaction_type,
        description=new_transaction.description,
        category_id=new_transaction.category_id,
        account=new_transaction.account
    )

    return TransactionResponse(
        id=transaction_id,
        user_id=new_transaction.user_id,
        amount=new_transaction.amount,
        transaction_type=new_transaction.transaction_type,
        description=new_transaction.description,
        category_id=new_transaction.category_id,
        account=new_transaction.account
    )