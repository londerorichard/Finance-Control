from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from enum import Enum


# ==========================================================
# USER SCHEMAS
# ==========================================================

class UserCreate(BaseModel):
    email: EmailStr = Field(
        description="User email address",
        examples=["user@email.com"]
    )

    password: str = Field(
        min_length=8,
        max_length=64,
        description="User password",
        examples=["MyPassword123"]
    )


class UserLogin(BaseModel):
    email: EmailStr = Field(
        description="User email address",
        examples=["user@email.com"]
    )

    password: str = Field(
        min_length=8,
        max_length=64,
        description="User password",
        examples=["MyPassword123"]
    )


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


# ==========================================================
# TRANSACTION SCHEMAS
# ==========================================================

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"

class TransactionCreate(BaseModel):
    user_id: int = Field(gt=0)
    amount: float = Field(gt=0)
    transaction_type: TransactionType
    description: str = Field(
        min_length=1,
        max_length=200
    )
    category_id: int = Field(gt=0)
    account: str = Field(
        min_length=1,
        max_length=50
    )


class TransactionResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    transaction_type: TransactionType
    description: str
    created_at: datetime
    category_id: int
    account: str


# ==========================================================
# CATEGORY SCHEMAS
# ==========================================================

# CategoryCreate
# CategoryResponse




# ==========================================================
# GOAL SCHEMAS
# ==========================================================




# GoalCreate
# GoalResponse